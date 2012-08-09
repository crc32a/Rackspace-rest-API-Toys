import rackspace.exp.rest.base.client
import urllib2
import copy

BaseClient = rackspace.exp.rest.base.client.BaseClient

class DnsClient(BaseClient):
    def __init__(self,*args,**kw):
        self.auth = kw.pop("auth")
        self.account = kw.pop("account")
        BaseClient.__init__(self,*args,**kw)

    def _defaultArgs(self,*args,**kw):
        kw = self.auth.addXauthHeaders(**kw)
        (kw,pageArgs) =  self.queryArgsFromKw("limit","offset",**kw)
        qStr = self.encodeQueryParams(pageArgs)
        return (kw,qStr)

    def getDomains(self,*args,**kw):
        (kw,qStr) = self._defaultArgs(*args,**kw)
        uri_tail = "/%i/domains%s"%(self.account,qStr)
        req = self.request(uri_tail,**kw)
        resp = urllib2.urlopen(req)
        return resp

    def getRecords(self,*argsIn,**kw):
        args = list(argsIn)
        domainId = args.pop(0)
        (kw,qStr) = self._defaultArgs(*args,**kw)
        uri_tail = "/%i/domains/%i/records%s"%(self.account,domainId,qStr)
        req = self.request(uri_tail,**kw)
        resp = urllib2.urlopen(req)
        return resp

    def listPtr(self,*argsIn,**kw):
        args = list(argsIn)
        serviceName = args.pop(0) #Example CloudLb
   
        (kw,qStr) = self._defaultArgs(*args,**kw)
        uri_tail = "/%i/"%(self.account,domainId,qStr)
        req = self.request(uri_tail,**kw)
        resp = urllib2.urlopen(req)
        return resp

    def addPtr(self,*argsIn,**kw):
        obj = {}
        args = list(argsIn)
        (kw,qStr) = self._defaultArgs(*args,**kw)
        sname = args.pop(0)
        url = args.pop(0)
        name = args.pop(0)
        ip = args.pop(0)
        ttl = args.pop(0)
        (kw,qStr) = self._defaultArgs(*args,**kw)
        obj["link"]={}
        obj["link"]["rel"]=sname
        obj["link"]["href"]=url
        obj["recordsList"] = []
        r = {}
        r["type"]="PTR"
        r["name"]=name
        r["data"] = ip
        r["ttl"] = ttl
        obj["rercordsList"].append(r)
        jsonStr = json.dumps(obj,indent=4)
        uri_tail = "/%s/rrnds%s"%(self.account,qStr)
        kw["data"] = jsonStr
        req = self.request(uri_tail,**kw)
        resp = urllib2.urlopen(req)
        return resp
        
        
        
