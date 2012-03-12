#!/usr/bin/env python

import exp.rest.base.client
import exp.rest.base.util
import urllib2
import json
import copy

BaseClient = exp.rest.base.client.BaseClient

class Auth1_1Client(BaseClient):
    util = exp.rest.base.util.BaseUtil
    def __init__(self,*args,**kw):
        self.username = kw.pop("username")
        self.key  = kw.pop("key")
        self.auth_resp = kw.pop("auth_resp",None)
        BaseClient.__init__(self,*args,**kw)

    def addXauthHeaders(self,**kw):
        kw["extra_headers"] = kw.pop("extra_headers",{})
        kw["extra_headers"]["x-auth-token"] = self.getToken()
        return kw


    def fetchAuth(self):
        self.auth_resp = None
        cred = {"credentials":{"username":self.username,"key":self.key}}
        kw = {}
        uri = "/auth"
        jdata = json.dumps(cred,indent=4)
        req = self.postReq(uri,data=jdata)
        resp = urllib2.urlopen(req)
        self.auth_resp = json.loads(resp.read())
        return copy.deepcopy(self.auth_resp)

    def getTokenExpire(self):
        return self.util.isodt2dt(self.auth_resp["auth"]["token"]["expires"])

    def getToken(self):
        return self.auth_resp["auth"]["token"]["id"]

    def getServiceCatalog(self):
        return copy.deepcopy(self.auth_resp["auth"]["serviceCatalog"])



