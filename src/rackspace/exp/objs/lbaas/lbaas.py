# ./lbaas.py
# PyXB bindings for NM:48ffa5fab00dcd71d53b45fa8cb8435172724a67
# Generated 2012-08-14 20:55:59.185143 by PyXB version 1.1.3
# Namespace http://docs.openstack.org/loadbalancers/api/v1.0 [xmlns:papi]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:5bc55ab6-e67c-11e1-b54c-002564955ea1')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import atom

Namespace = pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a Python instance."""
    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=Namespace.fallbackNamespace(), location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, _fallback_namespace=default_namespace)


# Atomic SimpleTypeDefinition
class ipVersion (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ipVersion')
    _Documentation = ''
ipVersion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ipVersion, enum_prefix=None)
ipVersion.IPV4 = ipVersion._CF_enumeration.addEnumeration(unicode_value=u'IPV4', tag=u'IPV4')
ipVersion.IPV6 = ipVersion._CF_enumeration.addEnumeration(unicode_value=u'IPV6', tag=u'IPV6')
ipVersion._InitializeFacetMap(ipVersion._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ipVersion', ipVersion)

# Atomic SimpleTypeDefinition
class networkItemType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'networkItemType')
    _Documentation = None
networkItemType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=networkItemType, enum_prefix=None)
networkItemType.ALLOW = networkItemType._CF_enumeration.addEnumeration(unicode_value=u'ALLOW', tag=u'ALLOW')
networkItemType.DENY = networkItemType._CF_enumeration.addEnumeration(unicode_value=u'DENY', tag=u'DENY')
networkItemType._InitializeFacetMap(networkItemType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'networkItemType', networkItemType)

# Atomic SimpleTypeDefinition
class vipType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'vipType')
    _Documentation = None
vipType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=vipType, enum_prefix=None)
vipType.PUBLIC = vipType._CF_enumeration.addEnumeration(unicode_value=u'PUBLIC', tag=u'PUBLIC')
vipType.SERVICENET = vipType._CF_enumeration.addEnumeration(unicode_value=u'SERVICENET', tag=u'SERVICENET')
vipType._InitializeFacetMap(vipType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'vipType', vipType)

# Atomic SimpleTypeDefinition
class persistenceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'persistenceType')
    _Documentation = None
persistenceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=persistenceType, enum_prefix=None)
persistenceType.HTTP_COOKIE = persistenceType._CF_enumeration.addEnumeration(unicode_value=u'HTTP_COOKIE', tag=u'HTTP_COOKIE')
persistenceType.SOURCE_IP = persistenceType._CF_enumeration.addEnumeration(unicode_value=u'SOURCE_IP', tag=u'SOURCE_IP')
persistenceType._InitializeFacetMap(persistenceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'persistenceType', persistenceType)

# Atomic SimpleTypeDefinition
class healthMonitorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'healthMonitorType')
    _Documentation = None
healthMonitorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=healthMonitorType, enum_prefix=None)
healthMonitorType.CONNECT = healthMonitorType._CF_enumeration.addEnumeration(unicode_value=u'CONNECT', tag=u'CONNECT')
healthMonitorType.HTTP = healthMonitorType._CF_enumeration.addEnumeration(unicode_value=u'HTTP', tag=u'HTTP')
healthMonitorType.HTTPS = healthMonitorType._CF_enumeration.addEnumeration(unicode_value=u'HTTPS', tag=u'HTTPS')
healthMonitorType._InitializeFacetMap(healthMonitorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'healthMonitorType', healthMonitorType)

# Atomic SimpleTypeDefinition
class nodeStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nodeStatus')
    _Documentation = None
nodeStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nodeStatus, enum_prefix=None)
nodeStatus.ONLINE = nodeStatus._CF_enumeration.addEnumeration(unicode_value=u'ONLINE', tag=u'ONLINE')
nodeStatus.OFFLINE = nodeStatus._CF_enumeration.addEnumeration(unicode_value=u'OFFLINE', tag=u'OFFLINE')
nodeStatus._InitializeFacetMap(nodeStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'nodeStatus', nodeStatus)

# Atomic SimpleTypeDefinition
class nodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nodeType')
    _Documentation = None
nodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nodeType, enum_prefix=None)
nodeType.PRIMARY = nodeType._CF_enumeration.addEnumeration(unicode_value=u'PRIMARY', tag=u'PRIMARY')
nodeType.SECONDARY = nodeType._CF_enumeration.addEnumeration(unicode_value=u'SECONDARY', tag=u'SECONDARY')
nodeType._InitializeFacetMap(nodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'nodeType', nodeType)

# Atomic SimpleTypeDefinition
class nodeCondition (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nodeCondition')
    _Documentation = None
nodeCondition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nodeCondition, enum_prefix=None)
nodeCondition.ENABLED = nodeCondition._CF_enumeration.addEnumeration(unicode_value=u'ENABLED', tag=u'ENABLED')
nodeCondition.DISABLED = nodeCondition._CF_enumeration.addEnumeration(unicode_value=u'DISABLED', tag=u'DISABLED')
nodeCondition.DRAINING = nodeCondition._CF_enumeration.addEnumeration(unicode_value=u'DRAINING', tag=u'DRAINING')
nodeCondition._InitializeFacetMap(nodeCondition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'nodeCondition', nodeCondition)

# Complex type networkItem_ with content type EMPTY
class networkItem_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'networkItem')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapiv1_0_networkItem__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute address uses Python identifier address
    __address = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'address'), 'address', '__httpdocs_openstack_orgloadbalancersapiv1_0_networkItem__address', pyxb.binding.datatypes.string)
    
    address = property(__address.value, __address.set, None, None)

    
    # Attribute ipVersion uses Python identifier ipVersion
    __ipVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipVersion'), 'ipVersion', '__httpdocs_openstack_orgloadbalancersapiv1_0_networkItem__ipVersion', ipVersion)
    
    ipVersion = property(__ipVersion.value, __ipVersion.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpdocs_openstack_orgloadbalancersapiv1_0_networkItem__type', networkItemType)
    
    type = property(__type.value, __type.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __id.name() : __id,
        __address.name() : __address,
        __ipVersion.name() : __ipVersion,
        __type.name() : __type
    }
Namespace.addCategoryObject('typeBinding', u'networkItem', networkItem_)


# Complex type validationErrors_ with content type ELEMENT_ONLY
class validationErrors_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'validationErrors')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpdocs_openstack_orgloadbalancersapiv1_0_validationErrors__httpdocs_openstack_orgloadbalancersapiv1_0message', True)

    
    message = property(__message.value, __message.set, None, None)


    _ElementMap = {
        __message.name() : __message
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'validationErrors', validationErrors_)


# Complex type loadBalancerUsage_ with content type ELEMENT_ONLY
class loadBalancerUsage_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), 'link', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsage__httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancerUsageRecord uses Python identifier loadBalancerUsageRecord
    __loadBalancerUsageRecord = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsageRecord'), 'loadBalancerUsageRecord', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsage__httpdocs_openstack_orgloadbalancersapiv1_0loadBalancerUsageRecord', True)

    
    loadBalancerUsageRecord = property(__loadBalancerUsageRecord.value, __loadBalancerUsageRecord.set, None, None)

    
    # Attribute loadBalancerName uses Python identifier loadBalancerName
    __loadBalancerName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadBalancerName'), 'loadBalancerName', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsage__loadBalancerName', pyxb.binding.datatypes.string)
    
    loadBalancerName = property(__loadBalancerName.value, __loadBalancerName.set, None, None)

    
    # Attribute loadBalancerId uses Python identifier loadBalancerId
    __loadBalancerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadBalancerId'), 'loadBalancerId', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsage__loadBalancerId', pyxb.binding.datatypes.int)
    
    loadBalancerId = property(__loadBalancerId.value, __loadBalancerId.set, None, None)


    _ElementMap = {
        __link.name() : __link,
        __loadBalancerUsageRecord.name() : __loadBalancerUsageRecord
    }
    _AttributeMap = {
        __loadBalancerName.name() : __loadBalancerName,
        __loadBalancerId.name() : __loadBalancerId
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancerUsage', loadBalancerUsage_)


# Complex type sslTermination_ with content type ELEMENT_ONLY
class sslTermination_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sslTermination')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}intermediateCertificate uses Python identifier intermediateCertificate
    __intermediateCertificate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'intermediateCertificate'), 'intermediateCertificate', '__httpdocs_openstack_orgloadbalancersapiv1_0_sslTermination__httpdocs_openstack_orgloadbalancersapiv1_0intermediateCertificate', False)

    
    intermediateCertificate = property(__intermediateCertificate.value, __intermediateCertificate.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}certificate uses Python identifier certificate
    __certificate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'certificate'), 'certificate', '__httpdocs_openstack_orgloadbalancersapiv1_0_sslTermination__httpdocs_openstack_orgloadbalancersapiv1_0certificate', False)

    
    certificate = property(__certificate.value, __certificate.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}privatekey uses Python identifier privatekey
    __privatekey = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'privatekey'), 'privatekey', '__httpdocs_openstack_orgloadbalancersapiv1_0_sslTermination__httpdocs_openstack_orgloadbalancersapiv1_0privatekey', False)

    
    privatekey = property(__privatekey.value, __privatekey.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapiv1_0_sslTermination__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute enabled uses Python identifier enabled
    __enabled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'enabled'), 'enabled', '__httpdocs_openstack_orgloadbalancersapiv1_0_sslTermination__enabled', pyxb.binding.datatypes.boolean)
    
    enabled = property(__enabled.value, __enabled.set, None, None)

    
    # Attribute secureTrafficOnly uses Python identifier secureTrafficOnly
    __secureTrafficOnly = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'secureTrafficOnly'), 'secureTrafficOnly', '__httpdocs_openstack_orgloadbalancersapiv1_0_sslTermination__secureTrafficOnly', pyxb.binding.datatypes.boolean)
    
    secureTrafficOnly = property(__secureTrafficOnly.value, __secureTrafficOnly.set, None, None)

    
    # Attribute securePort uses Python identifier securePort
    __securePort = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'securePort'), 'securePort', '__httpdocs_openstack_orgloadbalancersapiv1_0_sslTermination__securePort', pyxb.binding.datatypes.int)
    
    securePort = property(__securePort.value, __securePort.set, None, None)


    _ElementMap = {
        __intermediateCertificate.name() : __intermediateCertificate,
        __certificate.name() : __certificate,
        __privatekey.name() : __privatekey
    }
    _AttributeMap = {
        __id.name() : __id,
        __enabled.name() : __enabled,
        __secureTrafficOnly.name() : __secureTrafficOnly,
        __securePort.name() : __securePort
    }
Namespace.addCategoryObject('typeBinding', u'sslTermination', sslTermination_)


# Complex type sourceAddresses_ with content type EMPTY
class sourceAddresses_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sourceAddresses')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ipv6Public uses Python identifier ipv6Public
    __ipv6Public = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipv6Public'), 'ipv6Public', '__httpdocs_openstack_orgloadbalancersapiv1_0_sourceAddresses__ipv6Public', pyxb.binding.datatypes.string)
    
    ipv6Public = property(__ipv6Public.value, __ipv6Public.set, None, None)

    
    # Attribute ipv6Servicenet uses Python identifier ipv6Servicenet
    __ipv6Servicenet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipv6Servicenet'), 'ipv6Servicenet', '__httpdocs_openstack_orgloadbalancersapiv1_0_sourceAddresses__ipv6Servicenet', pyxb.binding.datatypes.string)
    
    ipv6Servicenet = property(__ipv6Servicenet.value, __ipv6Servicenet.set, None, None)

    
    # Attribute ipv4Public uses Python identifier ipv4Public
    __ipv4Public = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipv4Public'), 'ipv4Public', '__httpdocs_openstack_orgloadbalancersapiv1_0_sourceAddresses__ipv4Public', pyxb.binding.datatypes.string)
    
    ipv4Public = property(__ipv4Public.value, __ipv4Public.set, None, None)

    
    # Attribute ipv4Servicenet uses Python identifier ipv4Servicenet
    __ipv4Servicenet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipv4Servicenet'), 'ipv4Servicenet', '__httpdocs_openstack_orgloadbalancersapiv1_0_sourceAddresses__ipv4Servicenet', pyxb.binding.datatypes.string)
    
    ipv4Servicenet = property(__ipv4Servicenet.value, __ipv4Servicenet.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __ipv6Public.name() : __ipv6Public,
        __ipv6Servicenet.name() : __ipv6Servicenet,
        __ipv4Public.name() : __ipv4Public,
        __ipv4Servicenet.name() : __ipv4Servicenet
    }
Namespace.addCategoryObject('typeBinding', u'sourceAddresses', sourceAddresses_)


# Complex type nodes_ with content type ELEMENT_ONLY
class nodes_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nodes')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}node uses Python identifier node
    __node = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'node'), 'node', '__httpdocs_openstack_orgloadbalancersapiv1_0_nodes__httpdocs_openstack_orgloadbalancersapiv1_0node', True)

    
    node = property(__node.value, __node.set, None, None)


    _ElementMap = {
        __node.name() : __node
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nodes', nodes_)


# Complex type lbaasFault_ with content type ELEMENT_ONLY
class lbaasFault_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lbaasFault')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}details uses Python identifier details
    __details = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'details'), 'details', '__httpdocs_openstack_orgloadbalancersapiv1_0_lbaasFault__httpdocs_openstack_orgloadbalancersapiv1_0details', False)

    
    details = property(__details.value, __details.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpdocs_openstack_orgloadbalancersapiv1_0_lbaasFault__httpdocs_openstack_orgloadbalancersapiv1_0message', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'code'), 'code', '__httpdocs_openstack_orgloadbalancersapiv1_0_lbaasFault__code', pyxb.binding.datatypes.int)
    
    code = property(__code.value, __code.set, None, None)


    _ElementMap = {
        __details.name() : __details,
        __message.name() : __message
    }
    _AttributeMap = {
        __code.name() : __code
    }
Namespace.addCategoryObject('typeBinding', u'lbaasFault', lbaasFault_)


# Complex type clusterStatus_ with content type ELEMENT_ONLY
class clusterStatus_ (lbaasFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'clusterStatus')
    # Base type is lbaasFault_
    
    # Element details ({http://docs.openstack.org/loadbalancers/api/v1.0}details) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Element message ({http://docs.openstack.org/loadbalancers/api/v1.0}message) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Attribute code inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault

    _ElementMap = lbaasFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = lbaasFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'clusterStatus', clusterStatus_)


# Complex type sessionPersistence_ with content type EMPTY
class sessionPersistence_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sessionPersistence')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute persistenceType uses Python identifier persistenceType
    __persistenceType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'persistenceType'), 'persistenceType', '__httpdocs_openstack_orgloadbalancersapiv1_0_sessionPersistence__persistenceType', persistenceType)
    
    persistenceType = property(__persistenceType.value, __persistenceType.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __persistenceType.name() : __persistenceType
    }
Namespace.addCategoryObject('typeBinding', u'sessionPersistence', sessionPersistence_)


# Complex type limit_ with content type EMPTY
class limit_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'limit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapiv1_0_limit__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpdocs_openstack_orgloadbalancersapiv1_0_limit__value', pyxb.binding.datatypes.int)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapiv1_0_limit__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __id.name() : __id,
        __value.name() : __value,
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'limit', limit_)


# Complex type unProcessableEntity_ with content type ELEMENT_ONLY
class unProcessableEntity_ (lbaasFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'unProcessableEntity')
    # Base type is lbaasFault_
    
    # Element details ({http://docs.openstack.org/loadbalancers/api/v1.0}details) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Element message ({http://docs.openstack.org/loadbalancers/api/v1.0}message) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Attribute code inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault

    _ElementMap = lbaasFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = lbaasFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'unProcessableEntity', unProcessableEntity_)


# Complex type accountUsageRecord_ with content type EMPTY
class accountUsageRecord_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountUsageRecord')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute numPublicVips uses Python identifier numPublicVips
    __numPublicVips = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numPublicVips'), 'numPublicVips', '__httpdocs_openstack_orgloadbalancersapiv1_0_accountUsageRecord__numPublicVips', pyxb.binding.datatypes.int)
    
    numPublicVips = property(__numPublicVips.value, __numPublicVips.set, None, None)

    
    # Attribute numLoadBalancers uses Python identifier numLoadBalancers
    __numLoadBalancers = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numLoadBalancers'), 'numLoadBalancers', '__httpdocs_openstack_orgloadbalancersapiv1_0_accountUsageRecord__numLoadBalancers', pyxb.binding.datatypes.int)
    
    numLoadBalancers = property(__numLoadBalancers.value, __numLoadBalancers.set, None, None)

    
    # Attribute startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'startTime'), 'startTime', '__httpdocs_openstack_orgloadbalancersapiv1_0_accountUsageRecord__startTime', pyxb.binding.datatypes.dateTime)
    
    startTime = property(__startTime.value, __startTime.set, None, None)

    
    # Attribute numServicenetVips uses Python identifier numServicenetVips
    __numServicenetVips = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numServicenetVips'), 'numServicenetVips', '__httpdocs_openstack_orgloadbalancersapiv1_0_accountUsageRecord__numServicenetVips', pyxb.binding.datatypes.int)
    
    numServicenetVips = property(__numServicenetVips.value, __numServicenetVips.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __numPublicVips.name() : __numPublicVips,
        __numLoadBalancers.name() : __numLoadBalancers,
        __startTime.name() : __startTime,
        __numServicenetVips.name() : __numServicenetVips
    }
Namespace.addCategoryObject('typeBinding', u'accountUsageRecord', accountUsageRecord_)


# Complex type metadata_ with content type ELEMENT_ONLY
class metadata_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'metadata')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}meta uses Python identifier meta
    __meta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'meta'), 'meta', '__httpdocs_openstack_orgloadbalancersapiv1_0_metadata__httpdocs_openstack_orgloadbalancersapiv1_0meta', True)

    
    meta = property(__meta.value, __meta.set, None, None)


    _ElementMap = {
        __meta.name() : __meta
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'metadata', metadata_)


# Complex type allowedDomain_ with content type EMPTY
class allowedDomain_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'allowedDomain')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapiv1_0_allowedDomain__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'allowedDomain', allowedDomain_)


# Complex type methodNotAllowed_ with content type ELEMENT_ONLY
class methodNotAllowed_ (lbaasFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'methodNotAllowed')
    # Base type is lbaasFault_
    
    # Element details ({http://docs.openstack.org/loadbalancers/api/v1.0}details) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Element message ({http://docs.openstack.org/loadbalancers/api/v1.0}message) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Attribute code inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault

    _ElementMap = lbaasFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = lbaasFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'methodNotAllowed', methodNotAllowed_)


# Complex type updated_ with content type EMPTY
class updated_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'updated')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute time uses Python identifier time
    __time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'time'), 'time', '__httpdocs_openstack_orgloadbalancersapiv1_0_updated__time', pyxb.binding.datatypes.dateTime)
    
    time = property(__time.value, __time.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __time.name() : __time
    }
Namespace.addCategoryObject('typeBinding', u'updated', updated_)


# Complex type loadBalancers_ with content type ELEMENT_ONLY
class loadBalancers_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancers')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), 'link', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancers__httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer uses Python identifier loadBalancer
    __loadBalancer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancer'), 'loadBalancer', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancers__httpdocs_openstack_orgloadbalancersapiv1_0loadBalancer', True)

    
    loadBalancer = property(__loadBalancer.value, __loadBalancer.set, None, None)


    _ElementMap = {
        __link.name() : __link,
        __loadBalancer.name() : __loadBalancer
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancers', loadBalancers_)


# Complex type virtualIp_ with content type EMPTY
class virtualIp_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualIp')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute address uses Python identifier address
    __address = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'address'), 'address', '__httpdocs_openstack_orgloadbalancersapiv1_0_virtualIp__address', pyxb.binding.datatypes.string)
    
    address = property(__address.value, __address.set, None, None)

    
    # Attribute ipVersion uses Python identifier ipVersion
    __ipVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipVersion'), 'ipVersion', '__httpdocs_openstack_orgloadbalancersapiv1_0_virtualIp__ipVersion', ipVersion)
    
    ipVersion = property(__ipVersion.value, __ipVersion.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapiv1_0_virtualIp__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpdocs_openstack_orgloadbalancersapiv1_0_virtualIp__type', vipType)
    
    type = property(__type.value, __type.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __address.name() : __address,
        __ipVersion.name() : __ipVersion,
        __id.name() : __id,
        __type.name() : __type
    }
Namespace.addCategoryObject('typeBinding', u'virtualIp', virtualIp_)


# Complex type healthMonitor_ with content type EMPTY
class healthMonitor_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'healthMonitor')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute path uses Python identifier path
    __path = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'path'), 'path', '__httpdocs_openstack_orgloadbalancersapiv1_0_healthMonitor__path', pyxb.binding.datatypes.string)
    
    path = property(__path.value, __path.set, None, None)

    
    # Attribute bodyRegex uses Python identifier bodyRegex
    __bodyRegex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'bodyRegex'), 'bodyRegex', '__httpdocs_openstack_orgloadbalancersapiv1_0_healthMonitor__bodyRegex', pyxb.binding.datatypes.string)
    
    bodyRegex = property(__bodyRegex.value, __bodyRegex.set, None, None)

    
    # Attribute statusRegex uses Python identifier statusRegex
    __statusRegex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'statusRegex'), 'statusRegex', '__httpdocs_openstack_orgloadbalancersapiv1_0_healthMonitor__statusRegex', pyxb.binding.datatypes.string)
    
    statusRegex = property(__statusRegex.value, __statusRegex.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpdocs_openstack_orgloadbalancersapiv1_0_healthMonitor__type', healthMonitorType)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute delay uses Python identifier delay
    __delay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'delay'), 'delay', '__httpdocs_openstack_orgloadbalancersapiv1_0_healthMonitor__delay', pyxb.binding.datatypes.int)
    
    delay = property(__delay.value, __delay.set, None, None)

    
    # Attribute timeout uses Python identifier timeout
    __timeout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'timeout'), 'timeout', '__httpdocs_openstack_orgloadbalancersapiv1_0_healthMonitor__timeout', pyxb.binding.datatypes.int)
    
    timeout = property(__timeout.value, __timeout.set, None, None)

    
    # Attribute hostHeader uses Python identifier hostHeader
    __hostHeader = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'hostHeader'), 'hostHeader', '__httpdocs_openstack_orgloadbalancersapiv1_0_healthMonitor__hostHeader', pyxb.binding.datatypes.string)
    
    hostHeader = property(__hostHeader.value, __hostHeader.set, None, None)

    
    # Attribute attemptsBeforeDeactivation uses Python identifier attemptsBeforeDeactivation
    __attemptsBeforeDeactivation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'attemptsBeforeDeactivation'), 'attemptsBeforeDeactivation', '__httpdocs_openstack_orgloadbalancersapiv1_0_healthMonitor__attemptsBeforeDeactivation', pyxb.binding.datatypes.int)
    
    attemptsBeforeDeactivation = property(__attemptsBeforeDeactivation.value, __attemptsBeforeDeactivation.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapiv1_0_healthMonitor__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __path.name() : __path,
        __bodyRegex.name() : __bodyRegex,
        __statusRegex.name() : __statusRegex,
        __type.name() : __type,
        __delay.name() : __delay,
        __timeout.name() : __timeout,
        __hostHeader.name() : __hostHeader,
        __attemptsBeforeDeactivation.name() : __attemptsBeforeDeactivation,
        __id.name() : __id
    }
Namespace.addCategoryObject('typeBinding', u'healthMonitor', healthMonitor_)


# Complex type itemNotFound_ with content type ELEMENT_ONLY
class itemNotFound_ (lbaasFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'itemNotFound')
    # Base type is lbaasFault_
    
    # Element details ({http://docs.openstack.org/loadbalancers/api/v1.0}details) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Element message ({http://docs.openstack.org/loadbalancers/api/v1.0}message) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Attribute code inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault

    _ElementMap = lbaasFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = lbaasFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'itemNotFound', itemNotFound_)


# Complex type badRequest_ with content type ELEMENT_ONLY
class badRequest_ (lbaasFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'badRequest')
    # Base type is lbaasFault_
    
    # Element details ({http://docs.openstack.org/loadbalancers/api/v1.0}details) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}validationErrors uses Python identifier validationErrors
    __validationErrors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'validationErrors'), 'validationErrors', '__httpdocs_openstack_orgloadbalancersapiv1_0_badRequest__httpdocs_openstack_orgloadbalancersapiv1_0validationErrors', False)

    
    validationErrors = property(__validationErrors.value, __validationErrors.set, None, None)

    
    # Element message ({http://docs.openstack.org/loadbalancers/api/v1.0}message) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Attribute code inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault

    _ElementMap = lbaasFault_._ElementMap.copy()
    _ElementMap.update({
        __validationErrors.name() : __validationErrors
    })
    _AttributeMap = lbaasFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'badRequest', badRequest_)


# Complex type absolute_ with content type ELEMENT_ONLY
class absolute_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'absolute')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}limit uses Python identifier limit
    __limit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'limit'), 'limit', '__httpdocs_openstack_orgloadbalancersapiv1_0_absolute__httpdocs_openstack_orgloadbalancersapiv1_0limit', True)

    
    limit = property(__limit.value, __limit.set, None, None)


    _ElementMap = {
        __limit.name() : __limit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'absolute', absolute_)


# Complex type connectionLogging_ with content type EMPTY
class connectionLogging_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'connectionLogging')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute enabled uses Python identifier enabled
    __enabled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'enabled'), 'enabled', '__httpdocs_openstack_orgloadbalancersapiv1_0_connectionLogging__enabled', pyxb.binding.datatypes.boolean)
    
    enabled = property(__enabled.value, __enabled.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __enabled.name() : __enabled
    }
Namespace.addCategoryObject('typeBinding', u'connectionLogging', connectionLogging_)


# Complex type contentCaching_ with content type EMPTY
class contentCaching_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'contentCaching')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute enabled uses Python identifier enabled
    __enabled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'enabled'), 'enabled', '__httpdocs_openstack_orgloadbalancersapiv1_0_contentCaching__enabled', pyxb.binding.datatypes.boolean)
    
    enabled = property(__enabled.value, __enabled.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __enabled.name() : __enabled
    }
Namespace.addCategoryObject('typeBinding', u'contentCaching', contentCaching_)


# Complex type overLimit_ with content type ELEMENT_ONLY
class overLimit_ (lbaasFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'overLimit')
    # Base type is lbaasFault_
    
    # Element details ({http://docs.openstack.org/loadbalancers/api/v1.0}details) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Element message ({http://docs.openstack.org/loadbalancers/api/v1.0}message) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Attribute code inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault

    _ElementMap = lbaasFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = lbaasFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'overLimit', overLimit_)


# Complex type loadBalancer_ with content type ELEMENT_ONLY
class loadBalancer_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}connectionLogging uses Python identifier connectionLogging
    __connectionLogging = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'connectionLogging'), 'connectionLogging', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0connectionLogging', False)

    
    connectionLogging = property(__connectionLogging.value, __connectionLogging.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}healthMonitor uses Python identifier healthMonitor
    __healthMonitor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'healthMonitor'), 'healthMonitor', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0healthMonitor', False)

    
    healthMonitor = property(__healthMonitor.value, __healthMonitor.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}updated uses Python identifier updated
    __updated = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'updated'), 'updated', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0updated', False)

    
    updated = property(__updated.value, __updated.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancerUsage uses Python identifier loadBalancerUsage
    __loadBalancerUsage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsage'), 'loadBalancerUsage', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0loadBalancerUsage', False)

    
    loadBalancerUsage = property(__loadBalancerUsage.value, __loadBalancerUsage.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}sslTermination uses Python identifier sslTermination
    __sslTermination = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sslTermination'), 'sslTermination', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0sslTermination', False)

    
    sslTermination = property(__sslTermination.value, __sslTermination.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}created uses Python identifier created
    __created = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'created'), 'created', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0created', False)

    
    created = property(__created.value, __created.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}sourceAddresses uses Python identifier sourceAddresses
    __sourceAddresses = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sourceAddresses'), 'sourceAddresses', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0sourceAddresses', False)

    
    sourceAddresses = property(__sourceAddresses.value, __sourceAddresses.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}virtualIps uses Python identifier virtualIps
    __virtualIps = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'virtualIps'), 'virtualIps', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0virtualIps', False)

    
    virtualIps = property(__virtualIps.value, __virtualIps.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}accessList uses Python identifier accessList
    __accessList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accessList'), 'accessList', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0accessList', False)

    
    accessList = property(__accessList.value, __accessList.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}cluster uses Python identifier cluster
    __cluster = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cluster'), 'cluster', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0cluster', False)

    
    cluster = property(__cluster.value, __cluster.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}sessionPersistence uses Python identifier sessionPersistence
    __sessionPersistence = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sessionPersistence'), 'sessionPersistence', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0sessionPersistence', False)

    
    sessionPersistence = property(__sessionPersistence.value, __sessionPersistence.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}connectionThrottle uses Python identifier connectionThrottle
    __connectionThrottle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'connectionThrottle'), 'connectionThrottle', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0connectionThrottle', False)

    
    connectionThrottle = property(__connectionThrottle.value, __connectionThrottle.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}contentCaching uses Python identifier contentCaching
    __contentCaching = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'contentCaching'), 'contentCaching', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0contentCaching', False)

    
    contentCaching = property(__contentCaching.value, __contentCaching.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'metadata'), 'metadata', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0metadata', False)

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}nodes uses Python identifier nodes
    __nodes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nodes'), 'nodes', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapiv1_0nodes', False)

    
    nodes = property(__nodes.value, __nodes.set, None, None)

    
    # Attribute isSticky uses Python identifier isSticky
    __isSticky = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'isSticky'), 'isSticky', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__isSticky', pyxb.binding.datatypes.boolean)
    
    isSticky = property(__isSticky.value, __isSticky.set, None, None)

    
    # Attribute protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'protocol'), 'protocol', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__protocol', pyxb.binding.datatypes.string)
    
    protocol = property(__protocol.value, __protocol.set, None, None)

    
    # Attribute nodeCount uses Python identifier nodeCount
    __nodeCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'nodeCount'), 'nodeCount', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__nodeCount', pyxb.binding.datatypes.int)
    
    nodeCount = property(__nodeCount.value, __nodeCount.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute port uses Python identifier port
    __port = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'port'), 'port', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__port', pyxb.binding.datatypes.int)
    
    port = property(__port.value, __port.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__status', pyxb.binding.datatypes.string)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute algorithm uses Python identifier algorithm
    __algorithm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'algorithm'), 'algorithm', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancer__algorithm', pyxb.binding.datatypes.string)
    
    algorithm = property(__algorithm.value, __algorithm.set, None, None)


    _ElementMap = {
        __connectionLogging.name() : __connectionLogging,
        __healthMonitor.name() : __healthMonitor,
        __updated.name() : __updated,
        __loadBalancerUsage.name() : __loadBalancerUsage,
        __sslTermination.name() : __sslTermination,
        __created.name() : __created,
        __sourceAddresses.name() : __sourceAddresses,
        __virtualIps.name() : __virtualIps,
        __accessList.name() : __accessList,
        __cluster.name() : __cluster,
        __sessionPersistence.name() : __sessionPersistence,
        __connectionThrottle.name() : __connectionThrottle,
        __contentCaching.name() : __contentCaching,
        __metadata.name() : __metadata,
        __nodes.name() : __nodes
    }
    _AttributeMap = {
        __isSticky.name() : __isSticky,
        __protocol.name() : __protocol,
        __nodeCount.name() : __nodeCount,
        __id.name() : __id,
        __port.name() : __port,
        __name.name() : __name,
        __status.name() : __status,
        __algorithm.name() : __algorithm
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancer', loadBalancer_)


# Complex type generalFault_ with content type ELEMENT_ONLY
class generalFault_ (lbaasFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'generalFault')
    # Base type is lbaasFault_
    
    # Element details ({http://docs.openstack.org/loadbalancers/api/v1.0}details) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Element message ({http://docs.openstack.org/loadbalancers/api/v1.0}message) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Attribute code inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault

    _ElementMap = lbaasFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = lbaasFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'generalFault', generalFault_)


# Complex type stats_ with content type EMPTY
class stats_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'stats')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute connectTimeOut uses Python identifier connectTimeOut
    __connectTimeOut = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'connectTimeOut'), 'connectTimeOut', '__httpdocs_openstack_orgloadbalancersapiv1_0_stats__connectTimeOut', pyxb.binding.datatypes.int)
    
    connectTimeOut = property(__connectTimeOut.value, __connectTimeOut.set, None, None)

    
    # Attribute keepAliveTimedOut uses Python identifier keepAliveTimedOut
    __keepAliveTimedOut = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'keepAliveTimedOut'), 'keepAliveTimedOut', '__httpdocs_openstack_orgloadbalancersapiv1_0_stats__keepAliveTimedOut', pyxb.binding.datatypes.int)
    
    keepAliveTimedOut = property(__keepAliveTimedOut.value, __keepAliveTimedOut.set, None, None)

    
    # Attribute connectError uses Python identifier connectError
    __connectError = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'connectError'), 'connectError', '__httpdocs_openstack_orgloadbalancersapiv1_0_stats__connectError', pyxb.binding.datatypes.int)
    
    connectError = property(__connectError.value, __connectError.set, None, None)

    
    # Attribute maxConn uses Python identifier maxConn
    __maxConn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'maxConn'), 'maxConn', '__httpdocs_openstack_orgloadbalancersapiv1_0_stats__maxConn', pyxb.binding.datatypes.int)
    
    maxConn = property(__maxConn.value, __maxConn.set, None, None)

    
    # Attribute connectFailure uses Python identifier connectFailure
    __connectFailure = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'connectFailure'), 'connectFailure', '__httpdocs_openstack_orgloadbalancersapiv1_0_stats__connectFailure', pyxb.binding.datatypes.int)
    
    connectFailure = property(__connectFailure.value, __connectFailure.set, None, None)

    
    # Attribute dataTimedOut uses Python identifier dataTimedOut
    __dataTimedOut = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dataTimedOut'), 'dataTimedOut', '__httpdocs_openstack_orgloadbalancersapiv1_0_stats__dataTimedOut', pyxb.binding.datatypes.int)
    
    dataTimedOut = property(__dataTimedOut.value, __dataTimedOut.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __connectTimeOut.name() : __connectTimeOut,
        __keepAliveTimedOut.name() : __keepAliveTimedOut,
        __connectError.name() : __connectError,
        __maxConn.name() : __maxConn,
        __connectFailure.name() : __connectFailure,
        __dataTimedOut.name() : __dataTimedOut
    }
Namespace.addCategoryObject('typeBinding', u'stats', stats_)


# Complex type algorithm with content type EMPTY
class algorithm (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'algorithm')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapiv1_0_algorithm_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'algorithm', algorithm)


# Complex type accessList_ with content type ELEMENT_ONLY
class accessList_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accessList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}networkItem uses Python identifier networkItem
    __networkItem = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'networkItem'), 'networkItem', '__httpdocs_openstack_orgloadbalancersapiv1_0_accessList__httpdocs_openstack_orgloadbalancersapiv1_0networkItem', True)

    
    networkItem = property(__networkItem.value, __networkItem.set, None, None)


    _ElementMap = {
        __networkItem.name() : __networkItem
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'accessList', accessList_)


# Complex type unauthorized_ with content type ELEMENT_ONLY
class unauthorized_ (lbaasFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'unauthorized')
    # Base type is lbaasFault_
    
    # Element details ({http://docs.openstack.org/loadbalancers/api/v1.0}details) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Element message ({http://docs.openstack.org/loadbalancers/api/v1.0}message) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Attribute code inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault

    _ElementMap = lbaasFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = lbaasFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'unauthorized', unauthorized_)


# Complex type created_ with content type EMPTY
class created_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'created')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute time uses Python identifier time
    __time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'time'), 'time', '__httpdocs_openstack_orgloadbalancersapiv1_0_created__time', pyxb.binding.datatypes.dateTime)
    
    time = property(__time.value, __time.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __time.name() : __time
    }
Namespace.addCategoryObject('typeBinding', u'created', created_)


# Complex type accountBilling_ with content type ELEMENT_ONLY
class accountBilling_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountBilling')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancerUsage uses Python identifier loadBalancerUsage
    __loadBalancerUsage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsage'), 'loadBalancerUsage', '__httpdocs_openstack_orgloadbalancersapiv1_0_accountBilling__httpdocs_openstack_orgloadbalancersapiv1_0loadBalancerUsage', True)

    
    loadBalancerUsage = property(__loadBalancerUsage.value, __loadBalancerUsage.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}accountUsage uses Python identifier accountUsage
    __accountUsage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountUsage'), 'accountUsage', '__httpdocs_openstack_orgloadbalancersapiv1_0_accountBilling__httpdocs_openstack_orgloadbalancersapiv1_0accountUsage', False)

    
    accountUsage = property(__accountUsage.value, __accountUsage.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapiv1_0_accountBilling__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)


    _ElementMap = {
        __loadBalancerUsage.name() : __loadBalancerUsage,
        __accountUsage.name() : __accountUsage
    }
    _AttributeMap = {
        __accountId.name() : __accountId
    }
Namespace.addCategoryObject('typeBinding', u'accountBilling', accountBilling_)


# Complex type cluster with content type EMPTY
class cluster (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cluster')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapiv1_0_cluster_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'cluster', cluster)


# Complex type loadBalancerUsageRecord with content type EMPTY
class loadBalancerUsageRecord (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsageRecord')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute averageNumConnections uses Python identifier averageNumConnections
    __averageNumConnections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'averageNumConnections'), 'averageNumConnections', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_averageNumConnections', pyxb.binding.datatypes.double)
    
    averageNumConnections = property(__averageNumConnections.value, __averageNumConnections.set, None, None)

    
    # Attribute outgoingTransfer uses Python identifier outgoingTransfer
    __outgoingTransfer = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'outgoingTransfer'), 'outgoingTransfer', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_outgoingTransfer', pyxb.binding.datatypes.long)
    
    outgoingTransfer = property(__outgoingTransfer.value, __outgoingTransfer.set, None, None)

    
    # Attribute eventType uses Python identifier eventType
    __eventType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'eventType'), 'eventType', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_eventType', pyxb.binding.datatypes.string)
    
    eventType = property(__eventType.value, __eventType.set, None, None)

    
    # Attribute numVips uses Python identifier numVips
    __numVips = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numVips'), 'numVips', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_numVips', pyxb.binding.datatypes.int)
    
    numVips = property(__numVips.value, __numVips.set, None, None)

    
    # Attribute startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'startTime'), 'startTime', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_startTime', pyxb.binding.datatypes.dateTime)
    
    startTime = property(__startTime.value, __startTime.set, None, None)

    
    # Attribute entryVersion uses Python identifier entryVersion
    __entryVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'entryVersion'), 'entryVersion', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_entryVersion', pyxb.binding.datatypes.int)
    
    entryVersion = property(__entryVersion.value, __entryVersion.set, None, None)

    
    # Attribute vipType uses Python identifier vipType
    __vipType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vipType'), 'vipType', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_vipType', vipType)
    
    vipType = property(__vipType.value, __vipType.set, None, None)

    
    # Attribute incomingTransfer uses Python identifier incomingTransfer
    __incomingTransfer = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'incomingTransfer'), 'incomingTransfer', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_incomingTransfer', pyxb.binding.datatypes.long)
    
    incomingTransfer = property(__incomingTransfer.value, __incomingTransfer.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute needsPushed uses Python identifier needsPushed
    __needsPushed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'needsPushed'), 'needsPushed', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_needsPushed', pyxb.binding.datatypes.int)
    
    needsPushed = property(__needsPushed.value, __needsPushed.set, None, None)

    
    # Attribute numPolls uses Python identifier numPolls
    __numPolls = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numPolls'), 'numPolls', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_numPolls', pyxb.binding.datatypes.int)
    
    numPolls = property(__numPolls.value, __numPolls.set, None, None)

    
    # Attribute sslMode uses Python identifier sslMode
    __sslMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'sslMode'), 'sslMode', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_sslMode', pyxb.binding.datatypes.string)
    
    sslMode = property(__sslMode.value, __sslMode.set, None, None)

    
    # Attribute outgoingTransferSsl uses Python identifier outgoingTransferSsl
    __outgoingTransferSsl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'outgoingTransferSsl'), 'outgoingTransferSsl', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_outgoingTransferSsl', pyxb.binding.datatypes.long)
    
    outgoingTransferSsl = property(__outgoingTransferSsl.value, __outgoingTransferSsl.set, None, None)

    
    # Attribute averageNumConnectionsSsl uses Python identifier averageNumConnectionsSsl
    __averageNumConnectionsSsl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'averageNumConnectionsSsl'), 'averageNumConnectionsSsl', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_averageNumConnectionsSsl', pyxb.binding.datatypes.double)
    
    averageNumConnectionsSsl = property(__averageNumConnectionsSsl.value, __averageNumConnectionsSsl.set, None, None)

    
    # Attribute endTime uses Python identifier endTime
    __endTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'endTime'), 'endTime', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_endTime', pyxb.binding.datatypes.dateTime)
    
    endTime = property(__endTime.value, __endTime.set, None, None)

    
    # Attribute incomingTransferSsl uses Python identifier incomingTransferSsl
    __incomingTransferSsl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'incomingTransferSsl'), 'incomingTransferSsl', '__httpdocs_openstack_orgloadbalancersapiv1_0_loadBalancerUsageRecord_incomingTransferSsl', pyxb.binding.datatypes.long)
    
    incomingTransferSsl = property(__incomingTransferSsl.value, __incomingTransferSsl.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __averageNumConnections.name() : __averageNumConnections,
        __outgoingTransfer.name() : __outgoingTransfer,
        __eventType.name() : __eventType,
        __numVips.name() : __numVips,
        __startTime.name() : __startTime,
        __entryVersion.name() : __entryVersion,
        __vipType.name() : __vipType,
        __incomingTransfer.name() : __incomingTransfer,
        __id.name() : __id,
        __needsPushed.name() : __needsPushed,
        __numPolls.name() : __numPolls,
        __sslMode.name() : __sslMode,
        __outgoingTransferSsl.name() : __outgoingTransferSsl,
        __averageNumConnectionsSsl.name() : __averageNumConnectionsSsl,
        __endTime.name() : __endTime,
        __incomingTransferSsl.name() : __incomingTransferSsl
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancerUsageRecord', loadBalancerUsageRecord)


# Complex type protocols_ with content type ELEMENT_ONLY
class protocols_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'protocols')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'protocol'), 'protocol', '__httpdocs_openstack_orgloadbalancersapiv1_0_protocols__httpdocs_openstack_orgloadbalancersapiv1_0protocol', True)

    
    protocol = property(__protocol.value, __protocol.set, None, None)


    _ElementMap = {
        __protocol.name() : __protocol
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'protocols', protocols_)


# Complex type protocol with content type EMPTY
class protocol (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'protocol')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapiv1_0_protocol_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute port uses Python identifier port
    __port = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'port'), 'port', '__httpdocs_openstack_orgloadbalancersapiv1_0_protocol_port', pyxb.binding.datatypes.int)
    
    port = property(__port.value, __port.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __name.name() : __name,
        __port.name() : __port
    }
Namespace.addCategoryObject('typeBinding', u'protocol', protocol)


# Complex type immutableEntity_ with content type ELEMENT_ONLY
class immutableEntity_ (lbaasFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'immutableEntity')
    # Base type is lbaasFault_
    
    # Element details ({http://docs.openstack.org/loadbalancers/api/v1.0}details) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Element message ({http://docs.openstack.org/loadbalancers/api/v1.0}message) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Attribute code inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault

    _ElementMap = lbaasFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = lbaasFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'immutableEntity', immutableEntity_)


# Complex type algorithms_ with content type ELEMENT_ONLY
class algorithms_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'algorithms')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}algorithm uses Python identifier algorithm
    __algorithm = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'algorithm'), 'algorithm', '__httpdocs_openstack_orgloadbalancersapiv1_0_algorithms__httpdocs_openstack_orgloadbalancersapiv1_0algorithm', True)

    
    algorithm = property(__algorithm.value, __algorithm.set, None, None)


    _ElementMap = {
        __algorithm.name() : __algorithm
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'algorithms', algorithms_)


# Complex type node_ with content type ELEMENT_ONLY
class node_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'node')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'metadata'), 'metadata', '__httpdocs_openstack_orgloadbalancersapiv1_0_node__httpdocs_openstack_orgloadbalancersapiv1_0metadata', False)

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Attribute weight uses Python identifier weight
    __weight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'weight'), 'weight', '__httpdocs_openstack_orgloadbalancersapiv1_0_node__weight', pyxb.binding.datatypes.int)
    
    weight = property(__weight.value, __weight.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpdocs_openstack_orgloadbalancersapiv1_0_node__type', nodeType)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute condition uses Python identifier condition
    __condition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'condition'), 'condition', '__httpdocs_openstack_orgloadbalancersapiv1_0_node__condition', nodeCondition)
    
    condition = property(__condition.value, __condition.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapiv1_0_node__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute port uses Python identifier port
    __port = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'port'), 'port', '__httpdocs_openstack_orgloadbalancersapiv1_0_node__port', pyxb.binding.datatypes.int)
    
    port = property(__port.value, __port.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpdocs_openstack_orgloadbalancersapiv1_0_node__status', nodeStatus)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute address uses Python identifier address
    __address = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'address'), 'address', '__httpdocs_openstack_orgloadbalancersapiv1_0_node__address', pyxb.binding.datatypes.string)
    
    address = property(__address.value, __address.set, None, None)


    _ElementMap = {
        __metadata.name() : __metadata
    }
    _AttributeMap = {
        __weight.name() : __weight,
        __type.name() : __type,
        __condition.name() : __condition,
        __id.name() : __id,
        __port.name() : __port,
        __status.name() : __status,
        __address.name() : __address
    }
Namespace.addCategoryObject('typeBinding', u'node', node_)


# Complex type allowedDomains_ with content type ELEMENT_ONLY
class allowedDomains_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'allowedDomains')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}allowedDomain uses Python identifier allowedDomain
    __allowedDomain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'allowedDomain'), 'allowedDomain', '__httpdocs_openstack_orgloadbalancersapiv1_0_allowedDomains__httpdocs_openstack_orgloadbalancersapiv1_0allowedDomain', True)

    
    allowedDomain = property(__allowedDomain.value, __allowedDomain.set, None, None)


    _ElementMap = {
        __allowedDomain.name() : __allowedDomain
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'allowedDomains', allowedDomains_)


# Complex type virtualIps_ with content type ELEMENT_ONLY
class virtualIps_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualIps')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}virtualIp uses Python identifier virtualIp
    __virtualIp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'virtualIp'), 'virtualIp', '__httpdocs_openstack_orgloadbalancersapiv1_0_virtualIps__httpdocs_openstack_orgloadbalancersapiv1_0virtualIp', True)

    
    virtualIp = property(__virtualIp.value, __virtualIp.set, None, None)


    _ElementMap = {
        __virtualIp.name() : __virtualIp
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'virtualIps', virtualIps_)


# Complex type limitTypes_ with content type ELEMENT_ONLY
class limitTypes_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'limitTypes')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}limitType uses Python identifier limitType
    __limitType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'limitType'), 'limitType', '__httpdocs_openstack_orgloadbalancersapiv1_0_limitTypes__httpdocs_openstack_orgloadbalancersapiv1_0limitType', True)

    
    limitType = property(__limitType.value, __limitType.set, None, None)


    _ElementMap = {
        __limitType.name() : __limitType
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'limitTypes', limitTypes_)


# Complex type serviceUnavailable_ with content type ELEMENT_ONLY
class serviceUnavailable_ (lbaasFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'serviceUnavailable')
    # Base type is lbaasFault_
    
    # Element details ({http://docs.openstack.org/loadbalancers/api/v1.0}details) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Element message ({http://docs.openstack.org/loadbalancers/api/v1.0}message) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Attribute code inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault

    _ElementMap = lbaasFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = lbaasFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'serviceUnavailable', serviceUnavailable_)


# Complex type limitType_ with content type EMPTY
class limitType_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'limitType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute defaultValue uses Python identifier defaultValue
    __defaultValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'defaultValue'), 'defaultValue', '__httpdocs_openstack_orgloadbalancersapiv1_0_limitType__defaultValue', pyxb.binding.datatypes.int)
    
    defaultValue = property(__defaultValue.value, __defaultValue.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpdocs_openstack_orgloadbalancersapiv1_0_limitType__description', pyxb.binding.datatypes.string)
    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapiv1_0_limitType__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __defaultValue.name() : __defaultValue,
        __description.name() : __description,
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'limitType', limitType_)


# Complex type connectionThrottle_ with content type EMPTY
class connectionThrottle_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'connectionThrottle')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute rateInterval uses Python identifier rateInterval
    __rateInterval = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rateInterval'), 'rateInterval', '__httpdocs_openstack_orgloadbalancersapiv1_0_connectionThrottle__rateInterval', pyxb.binding.datatypes.int)
    
    rateInterval = property(__rateInterval.value, __rateInterval.set, None, None)

    
    # Attribute maxConnectionRate uses Python identifier maxConnectionRate
    __maxConnectionRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'maxConnectionRate'), 'maxConnectionRate', '__httpdocs_openstack_orgloadbalancersapiv1_0_connectionThrottle__maxConnectionRate', pyxb.binding.datatypes.int)
    
    maxConnectionRate = property(__maxConnectionRate.value, __maxConnectionRate.set, None, None)

    
    # Attribute minConnections uses Python identifier minConnections
    __minConnections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'minConnections'), 'minConnections', '__httpdocs_openstack_orgloadbalancersapiv1_0_connectionThrottle__minConnections', pyxb.binding.datatypes.int)
    
    minConnections = property(__minConnections.value, __minConnections.set, None, None)

    
    # Attribute maxConnections uses Python identifier maxConnections
    __maxConnections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'maxConnections'), 'maxConnections', '__httpdocs_openstack_orgloadbalancersapiv1_0_connectionThrottle__maxConnections', pyxb.binding.datatypes.int)
    
    maxConnections = property(__maxConnections.value, __maxConnections.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __rateInterval.name() : __rateInterval,
        __maxConnectionRate.name() : __maxConnectionRate,
        __minConnections.name() : __minConnections,
        __maxConnections.name() : __maxConnections
    }
Namespace.addCategoryObject('typeBinding', u'connectionThrottle', connectionThrottle_)


# Complex type outOfVirtualIps_ with content type ELEMENT_ONLY
class outOfVirtualIps_ (lbaasFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'outOfVirtualIps')
    # Base type is lbaasFault_
    
    # Element details ({http://docs.openstack.org/loadbalancers/api/v1.0}details) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Element message ({http://docs.openstack.org/loadbalancers/api/v1.0}message) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Attribute code inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault

    _ElementMap = lbaasFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = lbaasFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'outOfVirtualIps', outOfVirtualIps_)


# Complex type meta_ with content type SIMPLE
class meta_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'meta')
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapiv1_0_meta__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'key'), 'key', '__httpdocs_openstack_orgloadbalancersapiv1_0_meta__key', pyxb.binding.datatypes.string)
    
    key = property(__key.value, __key.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __id.name() : __id,
        __key.name() : __key
    }
Namespace.addCategoryObject('typeBinding', u'meta', meta_)


# Complex type accountUsage_ with content type ELEMENT_ONLY
class accountUsage_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountUsage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), 'link', '__httpdocs_openstack_orgloadbalancersapiv1_0_accountUsage__httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}accountUsageRecord uses Python identifier accountUsageRecord
    __accountUsageRecord = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountUsageRecord'), 'accountUsageRecord', '__httpdocs_openstack_orgloadbalancersapiv1_0_accountUsage__httpdocs_openstack_orgloadbalancersapiv1_0accountUsageRecord', True)

    
    accountUsageRecord = property(__accountUsageRecord.value, __accountUsageRecord.set, None, None)


    _ElementMap = {
        __link.name() : __link,
        __accountUsageRecord.name() : __accountUsageRecord
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'accountUsage', accountUsage_)


# Complex type loadBalancerFault_ with content type ELEMENT_ONLY
class loadBalancerFault_ (lbaasFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancerFault')
    # Base type is lbaasFault_
    
    # Element details ({http://docs.openstack.org/loadbalancers/api/v1.0}details) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Element message ({http://docs.openstack.org/loadbalancers/api/v1.0}message) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault
    
    # Attribute code inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}lbaasFault

    _ElementMap = lbaasFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = lbaasFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'loadBalancerFault', loadBalancerFault_)


# Complex type limits_ with content type ELEMENT_ONLY
class limits_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'limits')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}absolute uses Python identifier absolute
    __absolute = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'absolute'), 'absolute', '__httpdocs_openstack_orgloadbalancersapiv1_0_limits__httpdocs_openstack_orgloadbalancersapiv1_0absolute', False)

    
    absolute = property(__absolute.value, __absolute.set, None, None)


    _ElementMap = {
        __absolute.name() : __absolute
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'limits', limits_)


# Complex type operationresponse with content type EMPTY
class operationresponse (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'operationresponse')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpdocs_openstack_orgloadbalancersapiv1_0_operationresponse_status', pyxb.binding.datatypes.int)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpdocs_openstack_orgloadbalancersapiv1_0_operationresponse_message', pyxb.binding.datatypes.string)
    
    message = property(__message.value, __message.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __status.name() : __status,
        __message.name() : __message
    }
Namespace.addCategoryObject('typeBinding', u'operationresponse', operationresponse)


# Complex type errorpage_ with content type ELEMENT_ONLY
class errorpage_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'errorpage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}content uses Python identifier content_
    __content = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'content'), 'content_', '__httpdocs_openstack_orgloadbalancersapiv1_0_errorpage__httpdocs_openstack_orgloadbalancersapiv1_0content', False)

    
    content_ = property(__content.value, __content.set, None, None)


    _ElementMap = {
        __content.name() : __content
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'errorpage', errorpage_)


networkItem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'networkItem'), networkItem_)
Namespace.addCategoryObject('elementBinding', networkItem.name().localName(), networkItem)

sourceAddresses = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sourceAddresses'), sourceAddresses_)
Namespace.addCategoryObject('elementBinding', sourceAddresses.name().localName(), sourceAddresses)

clusterStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'clusterStatus'), clusterStatus_)
Namespace.addCategoryObject('elementBinding', clusterStatus.name().localName(), clusterStatus)

unProcessableEntity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unProcessableEntity'), unProcessableEntity_)
Namespace.addCategoryObject('elementBinding', unProcessableEntity.name().localName(), unProcessableEntity)

allowedDomain = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'allowedDomain'), allowedDomain_)
Namespace.addCategoryObject('elementBinding', allowedDomain.name().localName(), allowedDomain)

methodNotAllowed = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'methodNotAllowed'), methodNotAllowed_)
Namespace.addCategoryObject('elementBinding', methodNotAllowed.name().localName(), methodNotAllowed)

loadBalancers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancers'), loadBalancers_)
Namespace.addCategoryObject('elementBinding', loadBalancers.name().localName(), loadBalancers)

itemNotFound = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'itemNotFound'), itemNotFound_)
Namespace.addCategoryObject('elementBinding', itemNotFound.name().localName(), itemNotFound)

sessionPersistence = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sessionPersistence'), sessionPersistence_)
Namespace.addCategoryObject('elementBinding', sessionPersistence.name().localName(), sessionPersistence)

badRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'badRequest'), badRequest_)
Namespace.addCategoryObject('elementBinding', badRequest.name().localName(), badRequest)

absolute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'absolute'), absolute_)
Namespace.addCategoryObject('elementBinding', absolute.name().localName(), absolute)

connectionLogging = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'connectionLogging'), connectionLogging_)
Namespace.addCategoryObject('elementBinding', connectionLogging.name().localName(), connectionLogging)

overLimit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'overLimit'), overLimit_)
Namespace.addCategoryObject('elementBinding', overLimit.name().localName(), overLimit)

generalFault = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'generalFault'), generalFault_)
Namespace.addCategoryObject('elementBinding', generalFault.name().localName(), generalFault)

stats = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stats'), stats_)
Namespace.addCategoryObject('elementBinding', stats.name().localName(), stats)

loadBalancer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancer'), loadBalancer_)
Namespace.addCategoryObject('elementBinding', loadBalancer.name().localName(), loadBalancer)

virtualIp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIp'), virtualIp_)
Namespace.addCategoryObject('elementBinding', virtualIp.name().localName(), virtualIp)

unauthorized = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unauthorized'), unauthorized_)
Namespace.addCategoryObject('elementBinding', unauthorized.name().localName(), unauthorized)

accessList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accessList'), accessList_)
Namespace.addCategoryObject('elementBinding', accessList.name().localName(), accessList)

created = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'created'), created_)
Namespace.addCategoryObject('elementBinding', created.name().localName(), created)

validationErrors = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'validationErrors'), validationErrors_)
Namespace.addCategoryObject('elementBinding', validationErrors.name().localName(), validationErrors)

accountBilling = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountBilling'), accountBilling_)
Namespace.addCategoryObject('elementBinding', accountBilling.name().localName(), accountBilling)

protocols = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'protocols'), protocols_)
Namespace.addCategoryObject('elementBinding', protocols.name().localName(), protocols)

limit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'limit'), limit_)
Namespace.addCategoryObject('elementBinding', limit.name().localName(), limit)

healthMonitor = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'healthMonitor'), healthMonitor_)
Namespace.addCategoryObject('elementBinding', healthMonitor.name().localName(), healthMonitor)

immutableEntity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'immutableEntity'), immutableEntity_)
Namespace.addCategoryObject('elementBinding', immutableEntity.name().localName(), immutableEntity)

algorithms = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'algorithms'), algorithms_)
Namespace.addCategoryObject('elementBinding', algorithms.name().localName(), algorithms)

node = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'node'), node_)
Namespace.addCategoryObject('elementBinding', node.name().localName(), node)

updated = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updated'), updated_)
Namespace.addCategoryObject('elementBinding', updated.name().localName(), updated)

allowedDomains = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'allowedDomains'), allowedDomains_)
Namespace.addCategoryObject('elementBinding', allowedDomains.name().localName(), allowedDomains)

limitTypes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'limitTypes'), limitTypes_)
Namespace.addCategoryObject('elementBinding', limitTypes.name().localName(), limitTypes)

contentCaching = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contentCaching'), contentCaching_)
Namespace.addCategoryObject('elementBinding', contentCaching.name().localName(), contentCaching)

serviceUnavailable = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'serviceUnavailable'), serviceUnavailable_)
Namespace.addCategoryObject('elementBinding', serviceUnavailable.name().localName(), serviceUnavailable)

metadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'metadata'), metadata_)
Namespace.addCategoryObject('elementBinding', metadata.name().localName(), metadata)

outOfVirtualIps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'outOfVirtualIps'), outOfVirtualIps_)
Namespace.addCategoryObject('elementBinding', outOfVirtualIps.name().localName(), outOfVirtualIps)

virtualIps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIps'), virtualIps_)
Namespace.addCategoryObject('elementBinding', virtualIps.name().localName(), virtualIps)

meta = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'meta'), meta_)
Namespace.addCategoryObject('elementBinding', meta.name().localName(), meta)

nodes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nodes'), nodes_)
Namespace.addCategoryObject('elementBinding', nodes.name().localName(), nodes)

connectionThrottle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'connectionThrottle'), connectionThrottle_)
Namespace.addCategoryObject('elementBinding', connectionThrottle.name().localName(), connectionThrottle)

loadBalancerFault = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerFault'), loadBalancerFault_)
Namespace.addCategoryObject('elementBinding', loadBalancerFault.name().localName(), loadBalancerFault)

limits = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'limits'), limits_)
Namespace.addCategoryObject('elementBinding', limits.name().localName(), limits)

accountUsageRecord = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUsageRecord'), accountUsageRecord_)
Namespace.addCategoryObject('elementBinding', accountUsageRecord.name().localName(), accountUsageRecord)

lbaasFault = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lbaasFault'), lbaasFault_)
Namespace.addCategoryObject('elementBinding', lbaasFault.name().localName(), lbaasFault)

loadBalancerUsage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsage'), loadBalancerUsage_)
Namespace.addCategoryObject('elementBinding', loadBalancerUsage.name().localName(), loadBalancerUsage)

limitType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'limitType'), limitType_)
Namespace.addCategoryObject('elementBinding', limitType.name().localName(), limitType)

operationsuccess = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'operationsuccess'), operationresponse)
Namespace.addCategoryObject('elementBinding', operationsuccess.name().localName(), operationsuccess)

accountUsage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUsage'), accountUsage_)
Namespace.addCategoryObject('elementBinding', accountUsage.name().localName(), accountUsage)

errorpage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'errorpage'), errorpage_)
Namespace.addCategoryObject('elementBinding', errorpage.name().localName(), errorpage)

sslTermination = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sslTermination'), sslTermination_)
Namespace.addCategoryObject('elementBinding', sslTermination.name().localName(), sslTermination)



validationErrors_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), pyxb.binding.datatypes.string, scope=validationErrors_))
validationErrors_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(validationErrors_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=1L, max_occurs=None)
    )
validationErrors_._ContentModel = pyxb.binding.content.ParticleModel(validationErrors_._GroupModel, min_occurs=1, max_occurs=1)



loadBalancerUsage_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), atom.linkType, scope=loadBalancerUsage_))

loadBalancerUsage_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsageRecord'), loadBalancerUsageRecord, scope=loadBalancerUsage_))
loadBalancerUsage_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancerUsage_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsageRecord')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(loadBalancerUsage_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link')), min_occurs=0L, max_occurs=None)
    )
loadBalancerUsage_._ContentModel = pyxb.binding.content.ParticleModel(loadBalancerUsage_._GroupModel, min_occurs=1, max_occurs=1)



sslTermination_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'intermediateCertificate'), pyxb.binding.datatypes.string, scope=sslTermination_))

sslTermination_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'certificate'), pyxb.binding.datatypes.string, scope=sslTermination_))

sslTermination_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'privatekey'), pyxb.binding.datatypes.string, scope=sslTermination_))
sslTermination_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(sslTermination_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'privatekey')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(sslTermination_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'certificate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(sslTermination_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'intermediateCertificate')), min_occurs=0L, max_occurs=1)
    )
sslTermination_._ContentModel = pyxb.binding.content.ParticleModel(sslTermination_._GroupModel, min_occurs=1, max_occurs=1)



nodes_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'node'), node_, scope=nodes_))
nodes_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nodes_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'node')), min_occurs=1L, max_occurs=None)
    )
nodes_._ContentModel = pyxb.binding.content.ParticleModel(nodes_._GroupModel, min_occurs=1, max_occurs=1)



lbaasFault_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'details'), pyxb.binding.datatypes.string, scope=lbaasFault_))

lbaasFault_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), pyxb.binding.datatypes.string, scope=lbaasFault_))
lbaasFault_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(lbaasFault_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(lbaasFault_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
lbaasFault_._ContentModel = pyxb.binding.content.ParticleModel(lbaasFault_._GroupModel, min_occurs=1, max_occurs=1)


clusterStatus_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(clusterStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(clusterStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
clusterStatus_._ContentModel = pyxb.binding.content.ParticleModel(clusterStatus_._GroupModel, min_occurs=1, max_occurs=1)


unProcessableEntity_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(unProcessableEntity_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(unProcessableEntity_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
unProcessableEntity_._ContentModel = pyxb.binding.content.ParticleModel(unProcessableEntity_._GroupModel, min_occurs=1, max_occurs=1)



metadata_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'meta'), meta_, scope=metadata_))
metadata_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(metadata_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'meta')), min_occurs=1L, max_occurs=None)
    )
metadata_._ContentModel = pyxb.binding.content.ParticleModel(metadata_._GroupModel, min_occurs=1, max_occurs=1)


methodNotAllowed_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(methodNotAllowed_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(methodNotAllowed_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
methodNotAllowed_._ContentModel = pyxb.binding.content.ParticleModel(methodNotAllowed_._GroupModel, min_occurs=1, max_occurs=1)



loadBalancers_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), atom.linkType, scope=loadBalancers_))

loadBalancers_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancer'), loadBalancer_, scope=loadBalancers_))
loadBalancers_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancers_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancer')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(loadBalancers_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link')), min_occurs=0L, max_occurs=None)
    )
loadBalancers_._ContentModel = pyxb.binding.content.ParticleModel(loadBalancers_._GroupModel, min_occurs=1, max_occurs=1)


itemNotFound_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(itemNotFound_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(itemNotFound_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
itemNotFound_._ContentModel = pyxb.binding.content.ParticleModel(itemNotFound_._GroupModel, min_occurs=1, max_occurs=1)



badRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'validationErrors'), validationErrors_, scope=badRequest_))
badRequest_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(badRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(badRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
badRequest_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(badRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'validationErrors')), min_occurs=0L, max_occurs=1L)
    )
badRequest_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(badRequest_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(badRequest_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
badRequest_._ContentModel = pyxb.binding.content.ParticleModel(badRequest_._GroupModel, min_occurs=1, max_occurs=1)



absolute_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'limit'), limit_, scope=absolute_))
absolute_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(absolute_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'limit')), min_occurs=0L, max_occurs=None)
    )
absolute_._ContentModel = pyxb.binding.content.ParticleModel(absolute_._GroupModel, min_occurs=1, max_occurs=1)


overLimit_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(overLimit_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(overLimit_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
overLimit_._ContentModel = pyxb.binding.content.ParticleModel(overLimit_._GroupModel, min_occurs=1, max_occurs=1)



loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'connectionLogging'), connectionLogging_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'healthMonitor'), healthMonitor_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updated'), updated_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsage'), loadBalancerUsage_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sslTermination'), sslTermination_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'created'), created_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sourceAddresses'), sourceAddresses_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIps'), virtualIps_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accessList'), accessList_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cluster'), cluster, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sessionPersistence'), sessionPersistence_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'connectionThrottle'), connectionThrottle_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contentCaching'), contentCaching_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'metadata'), metadata_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nodes'), nodes_, scope=loadBalancer_))
loadBalancer_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'virtualIps')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nodes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'metadata')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsage')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sessionPersistence')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'healthMonitor')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'connectionThrottle')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accessList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cluster')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'created')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updated')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'connectionLogging')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contentCaching')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sourceAddresses')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sslTermination')), min_occurs=0L, max_occurs=1)
    )
loadBalancer_._ContentModel = pyxb.binding.content.ParticleModel(loadBalancer_._GroupModel, min_occurs=1, max_occurs=1)


generalFault_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(generalFault_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(generalFault_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
generalFault_._ContentModel = pyxb.binding.content.ParticleModel(generalFault_._GroupModel, min_occurs=1, max_occurs=1)



accessList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'networkItem'), networkItem_, scope=accessList_))
accessList_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accessList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'networkItem')), min_occurs=0L, max_occurs=None)
    )
accessList_._ContentModel = pyxb.binding.content.ParticleModel(accessList_._GroupModel, min_occurs=1, max_occurs=1)


unauthorized_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(unauthorized_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(unauthorized_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
unauthorized_._ContentModel = pyxb.binding.content.ParticleModel(unauthorized_._GroupModel, min_occurs=1, max_occurs=1)



accountBilling_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsage'), loadBalancerUsage_, scope=accountBilling_))

accountBilling_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUsage'), accountUsage_, scope=accountBilling_))
accountBilling_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accountBilling_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountUsage')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(accountBilling_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsage')), min_occurs=0L, max_occurs=None)
    )
accountBilling_._ContentModel = pyxb.binding.content.ParticleModel(accountBilling_._GroupModel, min_occurs=1, max_occurs=1)



protocols_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'protocol'), protocol, scope=protocols_))
protocols_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(protocols_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'protocol')), min_occurs=0L, max_occurs=None)
    )
protocols_._ContentModel = pyxb.binding.content.ParticleModel(protocols_._GroupModel, min_occurs=1, max_occurs=1)


immutableEntity_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(immutableEntity_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(immutableEntity_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
immutableEntity_._ContentModel = pyxb.binding.content.ParticleModel(immutableEntity_._GroupModel, min_occurs=1, max_occurs=1)



algorithms_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'algorithm'), algorithm, scope=algorithms_))
algorithms_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(algorithms_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'algorithm')), min_occurs=0L, max_occurs=None)
    )
algorithms_._ContentModel = pyxb.binding.content.ParticleModel(algorithms_._GroupModel, min_occurs=1, max_occurs=1)



node_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'metadata'), metadata_, scope=node_))
node_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(node_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'metadata')), min_occurs=0L, max_occurs=1)
    )
node_._ContentModel = pyxb.binding.content.ParticleModel(node_._GroupModel, min_occurs=1, max_occurs=1)



allowedDomains_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'allowedDomain'), allowedDomain_, scope=allowedDomains_))
allowedDomains_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(allowedDomains_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'allowedDomain')), min_occurs=0L, max_occurs=None)
    )
allowedDomains_._ContentModel = pyxb.binding.content.ParticleModel(allowedDomains_._GroupModel, min_occurs=1, max_occurs=1)



virtualIps_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIp'), virtualIp_, scope=virtualIps_))
virtualIps_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(virtualIps_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'virtualIp')), min_occurs=1L, max_occurs=None)
    )
virtualIps_._ContentModel = pyxb.binding.content.ParticleModel(virtualIps_._GroupModel, min_occurs=1, max_occurs=1)



limitTypes_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'limitType'), limitType_, scope=limitTypes_))
limitTypes_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(limitTypes_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'limitType')), min_occurs=0L, max_occurs=None)
    )
limitTypes_._ContentModel = pyxb.binding.content.ParticleModel(limitTypes_._GroupModel, min_occurs=1, max_occurs=1)


serviceUnavailable_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(serviceUnavailable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(serviceUnavailable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
serviceUnavailable_._ContentModel = pyxb.binding.content.ParticleModel(serviceUnavailable_._GroupModel, min_occurs=1, max_occurs=1)


outOfVirtualIps_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(outOfVirtualIps_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(outOfVirtualIps_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
outOfVirtualIps_._ContentModel = pyxb.binding.content.ParticleModel(outOfVirtualIps_._GroupModel, min_occurs=1, max_occurs=1)



accountUsage_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), atom.linkType, scope=accountUsage_))

accountUsage_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUsageRecord'), accountUsageRecord_, scope=accountUsage_))
accountUsage_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accountUsage_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountUsageRecord')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(accountUsage_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link')), min_occurs=0L, max_occurs=None)
    )
accountUsage_._ContentModel = pyxb.binding.content.ParticleModel(accountUsage_._GroupModel, min_occurs=1, max_occurs=1)


loadBalancerFault_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancerFault_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(loadBalancerFault_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=0L, max_occurs=1L)
    )
loadBalancerFault_._ContentModel = pyxb.binding.content.ParticleModel(loadBalancerFault_._GroupModel, min_occurs=1, max_occurs=1)



limits_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'absolute'), absolute_, scope=limits_))
limits_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(limits_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'absolute')), min_occurs=1, max_occurs=1)
    )
limits_._ContentModel = pyxb.binding.content.ParticleModel(limits_._GroupModel, min_occurs=1, max_occurs=1)



errorpage_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'content'), pyxb.binding.datatypes.string, scope=errorpage_))
errorpage_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(errorpage_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'content')), min_occurs=1, max_occurs=1)
    )
errorpage_._ContentModel = pyxb.binding.content.ParticleModel(errorpage_._GroupModel, min_occurs=1, max_occurs=1)
