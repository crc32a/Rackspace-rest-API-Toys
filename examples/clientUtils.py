#!/usr/bin/env python

import exp.rest.base.util
import exp.rest.auth.client.auth1_1
import exp.rest.dns.client
import exp.rest.lbaas.client.lbaas1_0
import os

util = exp.rest.base.util.BaseUtil
AuthClient = exp.rest.auth.client.auth1_1.Auth1_1Client
DnsClient = exp.rest.dns.client.DnsClient
LbaasClient = exp.rest.lbaas.client.lbaas1_0.LbaasClient1_0

#Git the filepath relative to this module.
def rp(file_path):
    try:
        module_dir = os.path.dirname(__file__)
    except NameError:           #If this is run from the python comand line
        module_dir = os.getcwd()#Just assume your json files are in this dir
    return os.path.join(module_dir,file_path)


#run getauth first
auth_resp = util.load_json(rp("auth_resp.json"))
auth_conf = util.load_json(rp("curr_auth.json"))
auth_conf.update({"auth_resp":auth_resp})

#Run the setAccount setDNsEndpoint and setLbaasEndpoint scripts
#to populate the conf.json file in this directory.
conf = util.load_json(rp("conf.json"))
account = conf["account"]
dnsep = conf["dnsEndPoint"]
lbaasep = conf["lbaasEndPoint"]

auth = AuthClient(**auth_conf)
dns = DnsClient(uri=dnsep,account=account,auth=auth)
lbaas = LbaasClient(uri=lbaasep,account=account,auth=auth)

