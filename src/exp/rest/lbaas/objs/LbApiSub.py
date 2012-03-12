#!/usr/bin/env python

#
# Generated Tue Mar 13 17:51:01 2012 by generateDS.py version 2.7b.
#

import sys

import LbApi as supermod

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

class loadBalancersSub(supermod.loadBalancers):
    def __init__(self, loadBalancer=None, link=None):
        super(loadBalancersSub, self).__init__(loadBalancer, link, )
supermod.loadBalancers.subclass = loadBalancersSub
# end class loadBalancersSub


class loadBalancerSub(supermod.loadBalancer):
    def __init__(self, status=None, protocol=None, name=None, algorithm=None, isSticky=None, id=None, nodeCount=None, port=None, virtualIps=None, nodes=None, metadata=None, loadBalancerUsage=None, sessionPersistence=None, healthMonitor=None, connectionThrottle=None, accessList=None, cluster=None, created=None, updated=None, connectionLogging=None, sourceAddresses=None, sslTermination=None):
        super(loadBalancerSub, self).__init__(status, protocol, name, algorithm, isSticky, id, nodeCount, port, virtualIps, nodes, metadata, loadBalancerUsage, sessionPersistence, healthMonitor, connectionThrottle, accessList, cluster, created, updated, connectionLogging, sourceAddresses, sslTermination, )
supermod.loadBalancer.subclass = loadBalancerSub
# end class loadBalancerSub


class sourceAddressesSub(supermod.sourceAddresses):
    def __init__(self, ipv4Public=None, ipv4Servicenet=None, ipv6Public=None, ipv6Servicenet=None):
        super(sourceAddressesSub, self).__init__(ipv4Public, ipv4Servicenet, ipv6Public, ipv6Servicenet, )
supermod.sourceAddresses.subclass = sourceAddressesSub
# end class sourceAddressesSub


class statsSub(supermod.stats):
    def __init__(self, connectTimeOut=None, dataTimedOut=None, connectFailure=None, keepAliveTimedOut=None, maxConn=None, connectError=None):
        super(statsSub, self).__init__(connectTimeOut, dataTimedOut, connectFailure, keepAliveTimedOut, maxConn, connectError, )
supermod.stats.subclass = statsSub
# end class statsSub


class connectionLoggingSub(supermod.connectionLogging):
    def __init__(self, enabled=None):
        super(connectionLoggingSub, self).__init__(enabled, )
supermod.connectionLogging.subclass = connectionLoggingSub
# end class connectionLoggingSub


class createdSub(supermod.created):
    def __init__(self, time=None):
        super(createdSub, self).__init__(time, )
supermod.created.subclass = createdSub
# end class createdSub


class updatedSub(supermod.updated):
    def __init__(self, time=None):
        super(updatedSub, self).__init__(time, )
supermod.updated.subclass = updatedSub
# end class updatedSub


class healthMonitorSub(supermod.healthMonitor):
    def __init__(self, attemptsBeforeDeactivation=None, bodyRegex=None, statusRegex=None, delay=None, timeout=None, path=None, type_=None, id=None):
        super(healthMonitorSub, self).__init__(attemptsBeforeDeactivation, bodyRegex, statusRegex, delay, timeout, path, type_, id, )
supermod.healthMonitor.subclass = healthMonitorSub
# end class healthMonitorSub


class virtualIpsSub(supermod.virtualIps):
    def __init__(self, virtualIp=None):
        super(virtualIpsSub, self).__init__(virtualIp, )
supermod.virtualIps.subclass = virtualIpsSub
# end class virtualIpsSub


class nodesSub(supermod.nodes):
    def __init__(self, node=None):
        super(nodesSub, self).__init__(node, )
supermod.nodes.subclass = nodesSub
# end class nodesSub


class sessionPersistenceSub(supermod.sessionPersistence):
    def __init__(self, persistenceType=None):
        super(sessionPersistenceSub, self).__init__(persistenceType, )
supermod.sessionPersistence.subclass = sessionPersistenceSub
# end class sessionPersistenceSub


class nodeSub(supermod.node):
    def __init__(self, status=None, weight=None, id=None, address=None, type_=None, port=None, condition=None):
        super(nodeSub, self).__init__(status, weight, id, address, type_, port, condition, )
supermod.node.subclass = nodeSub
# end class nodeSub


class virtualIpSub(supermod.virtualIp):
    def __init__(self, ipVersion=None, type_=None, id=None, address=None):
        super(virtualIpSub, self).__init__(ipVersion, type_, id, address, )
supermod.virtualIp.subclass = virtualIpSub
# end class virtualIpSub


class connectionThrottleSub(supermod.connectionThrottle):
    def __init__(self, maxConnectionRate=None, minConnections=None, rateInterval=None, maxConnections=None):
        super(connectionThrottleSub, self).__init__(maxConnectionRate, minConnections, rateInterval, maxConnections, )
supermod.connectionThrottle.subclass = connectionThrottleSub
# end class connectionThrottleSub


class algorithmSub(supermod.algorithm):
    def __init__(self, name=None):
        super(algorithmSub, self).__init__(name, )
supermod.algorithm.subclass = algorithmSub
# end class algorithmSub


class algorithmsSub(supermod.algorithms):
    def __init__(self, algorithm=None):
        super(algorithmsSub, self).__init__(algorithm, )
supermod.algorithms.subclass = algorithmsSub
# end class algorithmsSub


class accessListSub(supermod.accessList):
    def __init__(self, networkItem=None):
        super(accessListSub, self).__init__(networkItem, )
supermod.accessList.subclass = accessListSub
# end class accessListSub


class networkItemSub(supermod.networkItem):
    def __init__(self, ipVersion=None, type_=None, id=None, address=None):
        super(networkItemSub, self).__init__(ipVersion, type_, id, address, )
supermod.networkItem.subclass = networkItemSub
# end class networkItemSub


class loadBalancerUsageRecordSub(supermod.loadBalancerUsageRecord):
    def __init__(self, startTime=None, eventType=None, outgoingTransfer=None, incomingTransfer=None, numPolls=None, numVips=None, endTime=None, id=None, vipType=None, averageNumConnections=None):
        super(loadBalancerUsageRecordSub, self).__init__(startTime, eventType, outgoingTransfer, incomingTransfer, numPolls, numVips, endTime, id, vipType, averageNumConnections, )
supermod.loadBalancerUsageRecord.subclass = loadBalancerUsageRecordSub
# end class loadBalancerUsageRecordSub


class accountBillingSub(supermod.accountBilling):
    def __init__(self, accountId=None, accountUsage=None, loadBalancerUsage=None):
        super(accountBillingSub, self).__init__(accountId, accountUsage, loadBalancerUsage, )
supermod.accountBilling.subclass = accountBillingSub
# end class accountBillingSub


class accountUsageSub(supermod.accountUsage):
    def __init__(self, accountUsageRecord=None, link=None):
        super(accountUsageSub, self).__init__(accountUsageRecord, link, )
supermod.accountUsage.subclass = accountUsageSub
# end class accountUsageSub


class accountUsageRecordSub(supermod.accountUsageRecord):
    def __init__(self, numPublicVips=None, numServicenetVips=None, numLoadBalancers=None, startTime=None):
        super(accountUsageRecordSub, self).__init__(numPublicVips, numServicenetVips, numLoadBalancers, startTime, )
supermod.accountUsageRecord.subclass = accountUsageRecordSub
# end class accountUsageRecordSub


class loadBalancerUsageSub(supermod.loadBalancerUsage):
    def __init__(self, loadBalancerName=None, loadBalancerId=None, loadBalancerUsageRecord=None, link=None):
        super(loadBalancerUsageSub, self).__init__(loadBalancerName, loadBalancerId, loadBalancerUsageRecord, link, )
supermod.loadBalancerUsage.subclass = loadBalancerUsageSub
# end class loadBalancerUsageSub


class clusterSub(supermod.cluster):
    def __init__(self, name=None):
        super(clusterSub, self).__init__(name, )
supermod.cluster.subclass = clusterSub
# end class clusterSub


class protocolsSub(supermod.protocols):
    def __init__(self, protocol=None):
        super(protocolsSub, self).__init__(protocol, )
supermod.protocols.subclass = protocolsSub
# end class protocolsSub


class operationresponseSub(supermod.operationresponse):
    def __init__(self, status=None, message=None):
        super(operationresponseSub, self).__init__(status, message, )
supermod.operationresponse.subclass = operationresponseSub
# end class operationresponseSub


class protocolSub(supermod.protocol):
    def __init__(self, name=None, port=None):
        super(protocolSub, self).__init__(name, port, )
supermod.protocol.subclass = protocolSub
# end class protocolSub


class limitTypesSub(supermod.limitTypes):
    def __init__(self, limitType=None):
        super(limitTypesSub, self).__init__(limitType, )
supermod.limitTypes.subclass = limitTypesSub
# end class limitTypesSub


class limitTypeSub(supermod.limitType):
    def __init__(self, defaultValue=None, name=None, description=None):
        super(limitTypeSub, self).__init__(defaultValue, name, description, )
supermod.limitType.subclass = limitTypeSub
# end class limitTypeSub


class limitsSub(supermod.limits):
    def __init__(self, absolute=None):
        super(limitsSub, self).__init__(absolute, )
supermod.limits.subclass = limitsSub
# end class limitsSub


class absoluteSub(supermod.absolute):
    def __init__(self, limit=None):
        super(absoluteSub, self).__init__(limit, )
supermod.absolute.subclass = absoluteSub
# end class absoluteSub


class limitSub(supermod.limit):
    def __init__(self, id=None, value=None, name=None):
        super(limitSub, self).__init__(id, value, name, )
supermod.limit.subclass = limitSub
# end class limitSub


class errorpageSub(supermod.errorpage):
    def __init__(self, content=None):
        super(errorpageSub, self).__init__(content, )
supermod.errorpage.subclass = errorpageSub
# end class errorpageSub


class sslTerminationSub(supermod.sslTermination):
    def __init__(self, securePort=None, enabled=None, id=None, secureTrafficOnly=None, privatekey=None, certificate=None, intermediateCertificate=None):
        super(sslTerminationSub, self).__init__(securePort, enabled, id, secureTrafficOnly, privatekey, certificate, intermediateCertificate, )
supermod.sslTermination.subclass = sslTerminationSub
# end class sslTerminationSub


class allowedDomainsSub(supermod.allowedDomains):
    def __init__(self, allowedDomain=None):
        super(allowedDomainsSub, self).__init__(allowedDomain, )
supermod.allowedDomains.subclass = allowedDomainsSub
# end class allowedDomainsSub


class allowedDomainSub(supermod.allowedDomain):
    def __init__(self, name=None):
        super(allowedDomainSub, self).__init__(name, )
supermod.allowedDomain.subclass = allowedDomainSub
# end class allowedDomainSub


class metadataSub(supermod.metadata):
    def __init__(self, meta=None):
        super(metadataSub, self).__init__(meta, )
supermod.metadata.subclass = metadataSub
# end class metadataSub


class metaSub(supermod.meta):
    def __init__(self, id=None, key=None, valueOf_=None):
        super(metaSub, self).__init__(id, key, valueOf_, )
supermod.meta.subclass = metaSub
# end class metaSub


class textTypeSub(supermod.textType):
    def __init__(self, lang=None, base=None, type_=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(textTypeSub, self).__init__(lang, base, type_, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.textType.subclass = textTypeSub
# end class textTypeSub


class personTypeSub(supermod.personType):
    def __init__(self, lang=None, base=None, name=None, uri=None, email=None, anytypeobjs_=None):
        super(personTypeSub, self).__init__(lang, base, name, uri, email, anytypeobjs_, )
supermod.personType.subclass = personTypeSub
# end class personTypeSub


class feedTypeSub(supermod.feedType):
    def __init__(self, lang=None, base=None, author=None, category=None, contributor=None, generator=None, icon=None, id=None, link=None, logo=None, rights=None, subtitle=None, title=None, updated=None, entry=None, anytypeobjs_=None):
        super(feedTypeSub, self).__init__(lang, base, author, category, contributor, generator, icon, id, link, logo, rights, subtitle, title, updated, entry, anytypeobjs_, )
supermod.feedType.subclass = feedTypeSub
# end class feedTypeSub


class entryTypeSub(supermod.entryType):
    def __init__(self, lang=None, base=None, author=None, category=None, content=None, contributor=None, id=None, link=None, published=None, rights=None, source=None, summary=None, title=None, updated=None, anytypeobjs_=None):
        super(entryTypeSub, self).__init__(lang, base, author, category, content, contributor, id, link, published, rights, source, summary, title, updated, anytypeobjs_, )
supermod.entryType.subclass = entryTypeSub
# end class entryTypeSub


class contentTypeSub(supermod.contentType):
    def __init__(self, lang=None, src=None, base=None, type_=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(contentTypeSub, self).__init__(lang, src, base, type_, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.contentType.subclass = contentTypeSub
# end class contentTypeSub


class categoryTypeSub(supermod.categoryType):
    def __init__(self, lang=None, term=None, scheme=None, base=None, label=None):
        super(categoryTypeSub, self).__init__(lang, term, scheme, base, label, )
supermod.categoryType.subclass = categoryTypeSub
# end class categoryTypeSub


class generatorTypeSub(supermod.generatorType):
    def __init__(self, lang=None, version=None, uri=None, base=None, valueOf_=None):
        super(generatorTypeSub, self).__init__(lang, version, uri, base, valueOf_, )
supermod.generatorType.subclass = generatorTypeSub
# end class generatorTypeSub


class iconTypeSub(supermod.iconType):
    def __init__(self, lang=None, base=None, valueOf_=None):
        super(iconTypeSub, self).__init__(lang, base, valueOf_, )
supermod.iconType.subclass = iconTypeSub
# end class iconTypeSub


class idTypeSub(supermod.idType):
    def __init__(self, lang=None, base=None, valueOf_=None):
        super(idTypeSub, self).__init__(lang, base, valueOf_, )
supermod.idType.subclass = idTypeSub
# end class idTypeSub


class linkTypeSub(supermod.linkType):
    def __init__(self, lang=None, title=None, hreflang=None, length=None, href=None, rel=None, base=None, type_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(linkTypeSub, self).__init__(lang, title, hreflang, length, href, rel, base, type_, valueOf_, mixedclass_, content_, )
supermod.linkType.subclass = linkTypeSub
# end class linkTypeSub


class logoTypeSub(supermod.logoType):
    def __init__(self, lang=None, base=None, valueOf_=None):
        super(logoTypeSub, self).__init__(lang, base, valueOf_, )
supermod.logoType.subclass = logoTypeSub
# end class logoTypeSub


class sourceTypeSub(supermod.sourceType):
    def __init__(self, lang=None, base=None, author=None, category=None, contributor=None, generator=None, icon=None, id=None, link=None, logo=None, rights=None, subtitle=None, title=None, updated=None, anytypeobjs_=None):
        super(sourceTypeSub, self).__init__(lang, base, author, category, contributor, generator, icon, id, link, logo, rights, subtitle, title, updated, anytypeobjs_, )
supermod.sourceType.subclass = sourceTypeSub
# end class sourceTypeSub


class uriTypeSub(supermod.uriType):
    def __init__(self, lang=None, base=None, valueOf_=None):
        super(uriTypeSub, self).__init__(lang, base, valueOf_, )
supermod.uriType.subclass = uriTypeSub
# end class uriTypeSub


class dateTimeTypeSub(supermod.dateTimeType):
    def __init__(self, lang=None, base=None, valueOf_=None):
        super(dateTimeTypeSub, self).__init__(lang, base, valueOf_, )
supermod.dateTimeType.subclass = dateTimeTypeSub
# end class dateTimeTypeSub



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
        rootTag = 'loadBalancers'
        rootClass = supermod.loadBalancers
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
        rootTag = 'loadBalancers'
        rootClass = supermod.loadBalancers
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
        rootTag = 'loadBalancers'
        rootClass = supermod.loadBalancers
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from ??? import *\n\n')
    sys.stdout.write('import ??? as model_\n\n')
    sys.stdout.write('rootObj = model_.loadBalancers(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="loadBalancers")
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


