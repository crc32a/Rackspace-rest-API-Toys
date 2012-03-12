import dateutil.parser
import cPickle
import json
import sys
import os

class BaseUtil(object):
    @staticmethod
    def printf(format,*args): sys.stdout.write(format%args)

    @staticmethod
    def fprintf(fp,format,*args): fp.write(format%args)

    @staticmethod
    def isodt2dt(isoStr):
        return dateutil.parser.parse(isoStr)

    @staticmethod
    def dt2isodt(dt):
        return dt.isoformat()

    @staticmethod
    def fullPath(file_path):
        full_path = os.path.expanduser(file_path)
        full_path = os.path.abspath(full_path)
        return full_path

    @staticmethod
    def load_cpickle(file_name):
        file_path = BaseUtil.fullPath(file_name)
        fp = open(file_path,"r")
        obj = cPickle.load(fp)
        fp.close()
        return obj

    @staticmethod
    def save_cpickle(file_name,obj):
        file_path = BaseUtil.fullPath(file_name)
        fp = open(file_path,"w")
        cPickle.dump(obj,fp)
        fp.close()
        return None

    @staticmethod
    def load_json(json_file):
        fp = open(BaseUtil.fullPath(json_file),"r")
        json_data = fp.read()
        fp.close()
        out = json.loads(json_data)
        return out

    @staticmethod
    def save_json(json_file,obj):
        fp = open(BaseUtil.fullPath(json_file),"w")
        out = json.dumps(obj, indent=2)
        fp.write(out)
        fp.close()

