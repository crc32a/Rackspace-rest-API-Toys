from operator import itemgetter, attrgetter
import dateutil.parser
import httplib
import urllib2
import urllib
import base64
import json
import copy
import sys

def printf(format,*args): sys.stdout.write(format%args)

def fprintf(fp,format,*args): fp.write(format%args)

def setRequestMethod(methodStr):
    def wrapper(*args,**kw):
        return methodStr
    return wrapper

def isodt2dt(isoStr):
    return dateutil.parser.parse(isoStr)


def dt2isodt(dt):
    return dt.isoformat()

def keygetter(key):
    def wrapper(item):
        return item[key]
    return wrapper

def nilDictList(listIn):
    out = []
    keys = set()
    for le in listIn:
        for k in le.keys():
            if k not in keys:
                keys.add(k)
    for le in listIn:
        row = {}
        for k in keys:
            row[k] = le.get(k,None)
        out.append(row)
    return out

class BaseClient(object):
    def __init__(self,*args,**kw):
        self.debug = kw.pop("debug",False)
        self.headers = kw.pop("headers",{})
        self.uri = kw.pop("uri")
        if not self.headers.has_key("accept"):
            self.headers["accept"]="application/json"
        if not self.headers.has_key("content-type"):
            self.headers["content-type"] = "application/json"

    @staticmethod
    def basicAuthHeader(user,passwd):
        args = (user.encode("ascii","ignore"),passwd.encode("ascii","ignore"))
        b64 = base64.b64encode("%s:%s"%args)
        return {"Authorization":"BASIC %s"%b64}

    def encodeQueryParams(self,params):
        if len(params)<1:
            return ""
        else:
            return "?%s"%urllib.urlencode(params)

    def queryArgsFromKw(self,*args,**kw):
        params = []
        for key in args:
            val = kw.pop(key,None)
            if val == None:
                continue
            params.append( (key,val) )
        return (kw,params)

    def request(self,uri_tail,*args,**kw):
        data = kw.get("data",None)
        headers = copy.deepcopy(kw.get("headers",self.headers))
        headers.update(kw.get("extra_headers",{}))
        uri = self.uri + uri_tail
        if kw.get("debug",self.debug):
            fprintf(sys.stderr,"uri=%s\ndata=%s\nheaders=%s\n",uri,data,headers)
        req = urllib2.Request(uri,data=data,headers=headers)
        if kw.has_key("method"):
            req.get_method = setRequestMethod(kw["method"])
        return req

    def postReq(self,*args,**kw):
        kw["method"] = "POST"
        return self.request(*args,**kw)

    def getReq(self,*args,**kw):
        kw["method"] = "GET"
        return self.request(*args,**kw)

    def deleteReq(self,*args,**kw):
        kw["method"]="DELETE"
        return self.request(*args,**kw)

    def putReq(self,*args,**kw):
        kw["method"] = "PUT"
        return self.request(*args,**kw)

