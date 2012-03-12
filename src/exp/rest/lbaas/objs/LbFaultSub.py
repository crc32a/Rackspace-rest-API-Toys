#!/usr/bin/env python

#
# Generated Tue Mar 13 17:52:13 2012 by generateDS.py version 2.7b.
#

import sys

import LbFault as supermod

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#

class lbaasFaultSub(supermod.lbaasFault):
    def __init__(self, code=None, message=None, details=None, extensiontype_=None):
        super(lbaasFaultSub, self).__init__(code, message, details, extensiontype_, )
supermod.lbaasFault.subclass = lbaasFaultSub
# end class lbaasFaultSub


class loadBalancerFaultSub(supermod.loadBalancerFault):
    def __init__(self, code=None, message=None, details=None):
        super(loadBalancerFaultSub, self).__init__(code, message, details, )
supermod.loadBalancerFault.subclass = loadBalancerFaultSub
# end class loadBalancerFaultSub


class generalFaultSub(supermod.generalFault):
    def __init__(self, code=None, message=None, details=None):
        super(generalFaultSub, self).__init__(code, message, details, )
supermod.generalFault.subclass = generalFaultSub
# end class generalFaultSub


class validationErrorsSub(supermod.validationErrors):
    def __init__(self, message=None):
        super(validationErrorsSub, self).__init__(message, )
supermod.validationErrors.subclass = validationErrorsSub
# end class validationErrorsSub


class badRequestSub(supermod.badRequest):
    def __init__(self, code=None, message=None, details=None, validationErrors=None):
        super(badRequestSub, self).__init__(code, message, details, validationErrors, )
supermod.badRequest.subclass = badRequestSub
# end class badRequestSub


class itemNotFoundSub(supermod.itemNotFound):
    def __init__(self, code=None, message=None, details=None):
        super(itemNotFoundSub, self).__init__(code, message, details, )
supermod.itemNotFound.subclass = itemNotFoundSub
# end class itemNotFoundSub


class overLimitSub(supermod.overLimit):
    def __init__(self, code=None, message=None, details=None):
        super(overLimitSub, self).__init__(code, message, details, )
supermod.overLimit.subclass = overLimitSub
# end class overLimitSub


class unauthorizedSub(supermod.unauthorized):
    def __init__(self, code=None, message=None, details=None):
        super(unauthorizedSub, self).__init__(code, message, details, )
supermod.unauthorized.subclass = unauthorizedSub
# end class unauthorizedSub


class outOfVirtualIpsSub(supermod.outOfVirtualIps):
    def __init__(self, code=None, message=None, details=None):
        super(outOfVirtualIpsSub, self).__init__(code, message, details, )
supermod.outOfVirtualIps.subclass = outOfVirtualIpsSub
# end class outOfVirtualIpsSub


class clusterStatusSub(supermod.clusterStatus):
    def __init__(self, code=None, message=None, details=None):
        super(clusterStatusSub, self).__init__(code, message, details, )
supermod.clusterStatus.subclass = clusterStatusSub
# end class clusterStatusSub


class immutableEntitySub(supermod.immutableEntity):
    def __init__(self, code=None, message=None, details=None):
        super(immutableEntitySub, self).__init__(code, message, details, )
supermod.immutableEntity.subclass = immutableEntitySub
# end class immutableEntitySub


class serviceUnavailableSub(supermod.serviceUnavailable):
    def __init__(self, code=None, message=None, details=None):
        super(serviceUnavailableSub, self).__init__(code, message, details, )
supermod.serviceUnavailable.subclass = serviceUnavailableSub
# end class serviceUnavailableSub


class unProcessableEntitySub(supermod.unProcessableEntity):
    def __init__(self, code=None, message=None, details=None):
        super(unProcessableEntitySub, self).__init__(code, message, details, )
supermod.unProcessableEntity.subclass = unProcessableEntitySub
# end class unProcessableEntitySub


class methodNotAllowedSub(supermod.methodNotAllowed):
    def __init__(self, code=None, message=None, details=None):
        super(methodNotAllowedSub, self).__init__(code, message, details, )
supermod.methodNotAllowed.subclass = methodNotAllowedSub
# end class methodNotAllowedSub



def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    if hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'lbaasFault'
        rootClass = supermod.lbaasFault
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='')
    doc = None
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'lbaasFault'
        rootClass = supermod.lbaasFault
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='')
    return rootObj


def parseLiteral(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'lbaasFault'
        rootClass = supermod.lbaasFault
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from ??? import *\n\n')
    sys.stdout.write('import ??? as model_\n\n')
    sys.stdout.write('rootObj = model_.lbaasFault(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="lbaasFault")
    sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    root = parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


