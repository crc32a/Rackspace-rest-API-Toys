import exp.rest.base.client
import urllib2
import json
import copy

BaseClient = exp.rest.base.client.BaseClient

class LbaasClient1_0(BaseClient):
    def __init__(self,*args,**kw):
        self.auth = kw.pop("auth")
        self.account = kw.pop("account")
        BaseClient.__init__(self,*args,**kw)

    def _defaultArgs(self,*args,**kw):
        kw = self.auth.addXauthHeaders(**kw)
        (kw,pageArgs) =  self.queryArgsFromKw("limit","offset",**kw)
        qStr = self.encodeQueryParams(pageArgs)
        return (kw,qStr)

    def getLoadBalancers(self,*args,**kw):
        (kw,qStr) = self._defaultArgs(*args,**kw)
        uri_tail = "/%i/loadbalancers%s"%(self.account,qStr)
        req = self.request(uri_tail,**kw)
        resp = urllib2.urlopen(req)
        return json.loads(resp.read())

