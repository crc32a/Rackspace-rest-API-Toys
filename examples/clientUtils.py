#!/usr/bin/env python

import rackspace.exp.rest.base.util
import rackspace.exp.rest.auth.client.auth1_1
import rackspace.exp.rest.dns.client
import rackspace.exp.rest.lbaas.client.lbaas1_0
import os

util = rackspace.exp.rest.base.util.BaseUtil
AuthClient = rackspace.exp.rest.auth.client.auth1_1.Auth1_1Client
DnsClient = rackspace.exp.rest.dns.client.DnsClient
LbaasClient = rackspace.exp.rest.lbaas.client.lbaas1_0.LbaasClient1_0

def attrStrs(obj,*attrNames):
    out = ""
    for attrName in attrNames[:-1]:
        out += "%s=%s, "%(attrName,getattr(obj,attrName))
    for attrName in attrNames[-1:]:
        out += "%s=%s"%(attrName,getattr(obj,attrName))
    return out

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

#if you want XML use this. Json is used by default
xmlHdrs = {"accept":"application/xml","content-type":"application/xml"}

auth = AuthClient(**auth_conf)
dns = DnsClient(uri=dnsep,account=account,auth=auth,headers=xmlHdrs)
lbaas = LbaasClient(uri=lbaasep,account=account,auth=auth,headers=xmlHdrs)

