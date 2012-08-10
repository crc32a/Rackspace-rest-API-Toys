# ./lbaasManagement.py
# PyXB bindings for NM:572bd5c41e492a58b221dbaaf57b283c047a5b82
# Generated 2012-08-14 20:55:59.185453 by PyXB version 1.1.3
# Namespace http://docs.openstack.org/loadbalancers/api/management/v1.0

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
import lbaas
import atom

Namespace = pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/management/v1.0', create_if_missing=True)
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
class blacklistType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'blacklistType')
    _Documentation = None
blacklistType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=blacklistType, enum_prefix=None)
blacklistType.NODE = blacklistType._CF_enumeration.addEnumeration(unicode_value=u'NODE', tag=u'NODE')
blacklistType.ACCESSLIST = blacklistType._CF_enumeration.addEnumeration(unicode_value=u'ACCESSLIST', tag=u'ACCESSLIST')
blacklistType._InitializeFacetMap(blacklistType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'blacklistType', blacklistType)

# Atomic SimpleTypeDefinition
class alertStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'alertStatus')
    _Documentation = None
alertStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=alertStatus, enum_prefix=None)
alertStatus.ACKNOWLEDGED = alertStatus._CF_enumeration.addEnumeration(unicode_value=u'ACKNOWLEDGED', tag=u'ACKNOWLEDGED')
alertStatus.UNACKNOWLEDGED = alertStatus._CF_enumeration.addEnumeration(unicode_value=u'UNACKNOWLEDGED', tag=u'UNACKNOWLEDGED')
alertStatus._InitializeFacetMap(alertStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'alertStatus', alertStatus)

# Atomic SimpleTypeDefinition
class dataCenter (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dataCenter')
    _Documentation = None
dataCenter._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dataCenter, enum_prefix=None)
dataCenter.DFW = dataCenter._CF_enumeration.addEnumeration(unicode_value=u'DFW', tag=u'DFW')
dataCenter.ORD = dataCenter._CF_enumeration.addEnumeration(unicode_value=u'ORD', tag=u'ORD')
dataCenter.LON = dataCenter._CF_enumeration.addEnumeration(unicode_value=u'LON', tag=u'LON')
dataCenter._InitializeFacetMap(dataCenter._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'dataCenter', dataCenter)

# Atomic SimpleTypeDefinition
class clusterStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'clusterStatus')
    _Documentation = None
clusterStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=clusterStatus, enum_prefix=None)
clusterStatus.ACTIVE = clusterStatus._CF_enumeration.addEnumeration(unicode_value=u'ACTIVE', tag=u'ACTIVE')
clusterStatus.INACTIVE = clusterStatus._CF_enumeration.addEnumeration(unicode_value=u'INACTIVE', tag=u'INACTIVE')
clusterStatus._InitializeFacetMap(clusterStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'clusterStatus', clusterStatus)

# Atomic SimpleTypeDefinition
class hostStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hostStatus')
    _Documentation = None
hostStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=hostStatus, enum_prefix=None)
hostStatus.ACTIVE_TARGET = hostStatus._CF_enumeration.addEnumeration(unicode_value=u'ACTIVE_TARGET', tag=u'ACTIVE_TARGET')
hostStatus.OFFLINE = hostStatus._CF_enumeration.addEnumeration(unicode_value=u'OFFLINE', tag=u'OFFLINE')
hostStatus.BURN_IN = hostStatus._CF_enumeration.addEnumeration(unicode_value=u'BURN_IN', tag=u'BURN_IN')
hostStatus.ACTIVE = hostStatus._CF_enumeration.addEnumeration(unicode_value=u'ACTIVE', tag=u'ACTIVE')
hostStatus.FAILOVER = hostStatus._CF_enumeration.addEnumeration(unicode_value=u'FAILOVER', tag=u'FAILOVER')
hostStatus.SOAP_API_ENDPOINT = hostStatus._CF_enumeration.addEnumeration(unicode_value=u'SOAP_API_ENDPOINT', tag=u'SOAP_API_ENDPOINT')
hostStatus._InitializeFacetMap(hostStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'hostStatus', hostStatus)

# Atomic SimpleTypeDefinition
class hostType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hostType')
    _Documentation = None
hostType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=hostType, enum_prefix=None)
hostType.ACTIVE = hostType._CF_enumeration.addEnumeration(unicode_value=u'ACTIVE', tag=u'ACTIVE')
hostType.FAILOVER = hostType._CF_enumeration.addEnumeration(unicode_value=u'FAILOVER', tag=u'FAILOVER')
hostType._InitializeFacetMap(hostType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'hostType', hostType)

# Atomic SimpleTypeDefinition
class zone (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'zone')
    _Documentation = None
zone._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=zone, enum_prefix=None)
zone.A = zone._CF_enumeration.addEnumeration(unicode_value=u'A', tag=u'A')
zone.B = zone._CF_enumeration.addEnumeration(unicode_value=u'B', tag=u'B')
zone._InitializeFacetMap(zone._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'zone', zone)

# Complex type ticket_ with content type EMPTY
class ticket_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ticket')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute comment uses Python identifier comment
    __comment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'comment'), 'comment', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_ticket__comment', pyxb.binding.datatypes.string)
    
    comment = property(__comment.value, __comment.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_ticket__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute ticketId uses Python identifier ticketId
    __ticketId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ticketId'), 'ticketId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_ticket__ticketId', pyxb.binding.datatypes.string)
    
    ticketId = property(__ticketId.value, __ticketId.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __comment.name() : __comment,
        __id.name() : __id,
        __ticketId.name() : __ticketId
    }
Namespace.addCategoryObject('typeBinding', u'ticket', ticket_)


# Complex type port_ with content type ELEMENT_ONLY
class port_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'port')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}loadBalancers uses Python identifier loadBalancers
    __loadBalancers = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancers'), 'loadBalancers', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_port__httpdocs_openstack_orgloadbalancersapimanagementv1_0loadBalancers', False)

    
    loadBalancers = property(__loadBalancers.value, __loadBalancers.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_port__value', pyxb.binding.datatypes.int)
    
    value_ = property(__value.value, __value.set, None, None)


    _ElementMap = {
        __loadBalancers.name() : __loadBalancers
    }
    _AttributeMap = {
        __value.name() : __value
    }
Namespace.addCategoryObject('typeBinding', u'port', port_)


# Complex type jobs_ with content type ELEMENT_ONLY
class jobs_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'jobs')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}job uses Python identifier job
    __job = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'job'), 'job', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_jobs__httpdocs_openstack_orgloadbalancersapimanagementv1_0job', True)

    
    job = property(__job.value, __job.set, None, None)


    _ElementMap = {
        __job.name() : __job
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'jobs', jobs_)


# Complex type accountLoadBalancerServiceEvents_ with content type ELEMENT_ONLY
class accountLoadBalancerServiceEvents_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountLoadBalancerServiceEvents')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}loadBalancerServiceEvents uses Python identifier loadBalancerServiceEvents
    __loadBalancerServiceEvents = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerServiceEvents'), 'loadBalancerServiceEvents', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountLoadBalancerServiceEvents__httpdocs_openstack_orgloadbalancersapimanagementv1_0loadBalancerServiceEvents', True)

    
    loadBalancerServiceEvents = property(__loadBalancerServiceEvents.value, __loadBalancerServiceEvents.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountLoadBalancerServiceEvents__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)


    _ElementMap = {
        __loadBalancerServiceEvents.name() : __loadBalancerServiceEvents
    }
    _AttributeMap = {
        __accountId.name() : __accountId
    }
Namespace.addCategoryObject('typeBinding', u'accountLoadBalancerServiceEvents', accountLoadBalancerServiceEvents_)


# Complex type netInterface_ with content type ELEMENT_ONLY
class netInterface_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'netInterface')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}cidr uses Python identifier cidr
    __cidr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cidr'), 'cidr', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_netInterface__httpdocs_openstack_orgloadbalancersapimanagementv1_0cidr', True)

    
    cidr = property(__cidr.value, __cidr.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_netInterface__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __cidr.name() : __cidr
    }
    _AttributeMap = {
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'netInterface', netInterface_)


# Complex type virtualIpAvailabilityReport_ with content type EMPTY
class virtualIpAvailabilityReport_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualIpAvailabilityReport')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute serviceNetIpAddressesInHolding uses Python identifier serviceNetIpAddressesInHolding
    __serviceNetIpAddressesInHolding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'serviceNetIpAddressesInHolding'), 'serviceNetIpAddressesInHolding', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__serviceNetIpAddressesInHolding', pyxb.binding.datatypes.long)
    
    serviceNetIpAddressesInHolding = property(__serviceNetIpAddressesInHolding.value, __serviceNetIpAddressesInHolding.set, None, None)

    
    # Attribute freeAndClearServiceNetIpAddresses uses Python identifier freeAndClearServiceNetIpAddresses
    __freeAndClearServiceNetIpAddresses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'freeAndClearServiceNetIpAddresses'), 'freeAndClearServiceNetIpAddresses', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__freeAndClearServiceNetIpAddresses', pyxb.binding.datatypes.long)
    
    freeAndClearServiceNetIpAddresses = property(__freeAndClearServiceNetIpAddresses.value, __freeAndClearServiceNetIpAddresses.set, None, None)

    
    # Attribute clusterId uses Python identifier clusterId
    __clusterId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'clusterId'), 'clusterId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__clusterId', pyxb.binding.datatypes.int)
    
    clusterId = property(__clusterId.value, __clusterId.set, None, None)

    
    # Attribute totalServiceNetAddresses uses Python identifier totalServiceNetAddresses
    __totalServiceNetAddresses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'totalServiceNetAddresses'), 'totalServiceNetAddresses', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__totalServiceNetAddresses', pyxb.binding.datatypes.long)
    
    totalServiceNetAddresses = property(__totalServiceNetAddresses.value, __totalServiceNetAddresses.set, None, None)

    
    # Attribute publicIpAddressesAllocatedToday uses Python identifier publicIpAddressesAllocatedToday
    __publicIpAddressesAllocatedToday = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'publicIpAddressesAllocatedToday'), 'publicIpAddressesAllocatedToday', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__publicIpAddressesAllocatedToday', pyxb.binding.datatypes.long)
    
    publicIpAddressesAllocatedToday = property(__publicIpAddressesAllocatedToday.value, __publicIpAddressesAllocatedToday.set, None, None)

    
    # Attribute freeAndClearPublicIpAddresses uses Python identifier freeAndClearPublicIpAddresses
    __freeAndClearPublicIpAddresses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'freeAndClearPublicIpAddresses'), 'freeAndClearPublicIpAddresses', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__freeAndClearPublicIpAddresses', pyxb.binding.datatypes.long)
    
    freeAndClearPublicIpAddresses = property(__freeAndClearPublicIpAddresses.value, __freeAndClearPublicIpAddresses.set, None, None)

    
    # Attribute allocatedServiceNetIpAddressesInLastSevenDays uses Python identifier allocatedServiceNetIpAddressesInLastSevenDays
    __allocatedServiceNetIpAddressesInLastSevenDays = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'allocatedServiceNetIpAddressesInLastSevenDays'), 'allocatedServiceNetIpAddressesInLastSevenDays', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__allocatedServiceNetIpAddressesInLastSevenDays', pyxb.binding.datatypes.long)
    
    allocatedServiceNetIpAddressesInLastSevenDays = property(__allocatedServiceNetIpAddressesInLastSevenDays.value, __allocatedServiceNetIpAddressesInLastSevenDays.set, None, None)

    
    # Attribute totalPublicIpAddresses uses Python identifier totalPublicIpAddresses
    __totalPublicIpAddresses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'totalPublicIpAddresses'), 'totalPublicIpAddresses', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__totalPublicIpAddresses', pyxb.binding.datatypes.long)
    
    totalPublicIpAddresses = property(__totalPublicIpAddresses.value, __totalPublicIpAddresses.set, None, None)

    
    # Attribute serviceNetIpAddressesAllocatedToday uses Python identifier serviceNetIpAddressesAllocatedToday
    __serviceNetIpAddressesAllocatedToday = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'serviceNetIpAddressesAllocatedToday'), 'serviceNetIpAddressesAllocatedToday', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__serviceNetIpAddressesAllocatedToday', pyxb.binding.datatypes.long)
    
    serviceNetIpAddressesAllocatedToday = property(__serviceNetIpAddressesAllocatedToday.value, __serviceNetIpAddressesAllocatedToday.set, None, None)

    
    # Attribute clusterName uses Python identifier clusterName
    __clusterName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'clusterName'), 'clusterName', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__clusterName', pyxb.binding.datatypes.string)
    
    clusterName = property(__clusterName.value, __clusterName.set, None, None)

    
    # Attribute allocatedPublicIpAddressesInLastSevenDays uses Python identifier allocatedPublicIpAddressesInLastSevenDays
    __allocatedPublicIpAddressesInLastSevenDays = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'allocatedPublicIpAddressesInLastSevenDays'), 'allocatedPublicIpAddressesInLastSevenDays', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__allocatedPublicIpAddressesInLastSevenDays', pyxb.binding.datatypes.long)
    
    allocatedPublicIpAddressesInLastSevenDays = property(__allocatedPublicIpAddressesInLastSevenDays.value, __allocatedPublicIpAddressesInLastSevenDays.set, None, None)

    
    # Attribute remainingDaysOfServiceNetIpAddresses uses Python identifier remainingDaysOfServiceNetIpAddresses
    __remainingDaysOfServiceNetIpAddresses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'remainingDaysOfServiceNetIpAddresses'), 'remainingDaysOfServiceNetIpAddresses', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__remainingDaysOfServiceNetIpAddresses', pyxb.binding.datatypes.double)
    
    remainingDaysOfServiceNetIpAddresses = property(__remainingDaysOfServiceNetIpAddresses.value, __remainingDaysOfServiceNetIpAddresses.set, None, None)

    
    # Attribute publicIpAddressesInHolding uses Python identifier publicIpAddressesInHolding
    __publicIpAddressesInHolding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'publicIpAddressesInHolding'), 'publicIpAddressesInHolding', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__publicIpAddressesInHolding', pyxb.binding.datatypes.long)
    
    publicIpAddressesInHolding = property(__publicIpAddressesInHolding.value, __publicIpAddressesInHolding.set, None, None)

    
    # Attribute remainingDaysOfPublicIpAddresses uses Python identifier remainingDaysOfPublicIpAddresses
    __remainingDaysOfPublicIpAddresses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'remainingDaysOfPublicIpAddresses'), 'remainingDaysOfPublicIpAddresses', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReport__remainingDaysOfPublicIpAddresses', pyxb.binding.datatypes.double)
    
    remainingDaysOfPublicIpAddresses = property(__remainingDaysOfPublicIpAddresses.value, __remainingDaysOfPublicIpAddresses.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __serviceNetIpAddressesInHolding.name() : __serviceNetIpAddressesInHolding,
        __freeAndClearServiceNetIpAddresses.name() : __freeAndClearServiceNetIpAddresses,
        __clusterId.name() : __clusterId,
        __totalServiceNetAddresses.name() : __totalServiceNetAddresses,
        __publicIpAddressesAllocatedToday.name() : __publicIpAddressesAllocatedToday,
        __freeAndClearPublicIpAddresses.name() : __freeAndClearPublicIpAddresses,
        __allocatedServiceNetIpAddressesInLastSevenDays.name() : __allocatedServiceNetIpAddressesInLastSevenDays,
        __totalPublicIpAddresses.name() : __totalPublicIpAddresses,
        __serviceNetIpAddressesAllocatedToday.name() : __serviceNetIpAddressesAllocatedToday,
        __clusterName.name() : __clusterName,
        __allocatedPublicIpAddressesInLastSevenDays.name() : __allocatedPublicIpAddressesInLastSevenDays,
        __remainingDaysOfServiceNetIpAddresses.name() : __remainingDaysOfServiceNetIpAddresses,
        __publicIpAddressesInHolding.name() : __publicIpAddressesInHolding,
        __remainingDaysOfPublicIpAddresses.name() : __remainingDaysOfPublicIpAddresses
    }
Namespace.addCategoryObject('typeBinding', u'virtualIpAvailabilityReport', virtualIpAvailabilityReport_)


# Complex type loadBalancers_ with content type ELEMENT_ONLY
class loadBalancers_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancers')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}loadBalancer uses Python identifier loadBalancer
    __loadBalancer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancer'), 'loadBalancer', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancers__httpdocs_openstack_orgloadbalancersapimanagementv1_0loadBalancer', True)

    
    loadBalancer = property(__loadBalancer.value, __loadBalancer.set, None, None)


    _ElementMap = {
        __loadBalancer.name() : __loadBalancer
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancers', loadBalancers_)


# Complex type hostssubnet_ with content type ELEMENT_ONLY
class hostssubnet_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hostssubnet')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}hostsubnet uses Python identifier hostsubnet
    __hostsubnet = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hostsubnet'), 'hostsubnet', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostssubnet__httpdocs_openstack_orgloadbalancersapimanagementv1_0hostsubnet', True)

    
    hostsubnet = property(__hostsubnet.value, __hostsubnet.set, None, None)


    _ElementMap = {
        __hostsubnet.name() : __hostsubnet
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'hostssubnet', hostssubnet_)


# Complex type blacklistItem_ with content type EMPTY
class blacklistItem_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'blacklistItem')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_blacklistItem__type', blacklistType)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ipVersion uses Python identifier ipVersion
    __ipVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipVersion'), 'ipVersion', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_blacklistItem__ipVersion', lbaas.ipVersion)
    
    ipVersion = property(__ipVersion.value, __ipVersion.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_blacklistItem__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute cidrBlock uses Python identifier cidrBlock
    __cidrBlock = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'cidrBlock'), 'cidrBlock', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_blacklistItem__cidrBlock', pyxb.binding.datatypes.string)
    
    cidrBlock = property(__cidrBlock.value, __cidrBlock.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __type.name() : __type,
        __ipVersion.name() : __ipVersion,
        __id.name() : __id,
        __cidrBlock.name() : __cidrBlock
    }
Namespace.addCategoryObject('typeBinding', u'blacklistItem', blacklistItem_)


# Complex type job_ with content type EMPTY
class job_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'job')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute state uses Python identifier state
    __state = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'state'), 'state', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_job__state', pyxb.binding.datatypes.string)
    
    state = property(__state.value, __state.set, None, None)

    
    # Attribute startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'startTime'), 'startTime', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_job__startTime', pyxb.binding.datatypes.dateTime)
    
    startTime = property(__startTime.value, __startTime.set, None, None)

    
    # Attribute jobName uses Python identifier jobName
    __jobName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'jobName'), 'jobName', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_job__jobName', pyxb.binding.datatypes.string)
    
    jobName = property(__jobName.value, __jobName.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_job__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute inputPath uses Python identifier inputPath
    __inputPath = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'inputPath'), 'inputPath', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_job__inputPath', pyxb.binding.datatypes.string)
    
    inputPath = property(__inputPath.value, __inputPath.set, None, None)

    
    # Attribute endTime uses Python identifier endTime
    __endTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'endTime'), 'endTime', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_job__endTime', pyxb.binding.datatypes.dateTime)
    
    endTime = property(__endTime.value, __endTime.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __state.name() : __state,
        __startTime.name() : __startTime,
        __jobName.name() : __jobName,
        __id.name() : __id,
        __inputPath.name() : __inputPath,
        __endTime.name() : __endTime
    }
Namespace.addCategoryObject('typeBinding', u'job', job_)


# Complex type ldapGroup_ with content type EMPTY
class ldapGroup_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ldapGroup')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute group uses Python identifier group
    __group = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'group'), 'group', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_ldapGroup__group', pyxb.binding.datatypes.string)
    
    group = property(__group.value, __group.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __group.name() : __group
    }
Namespace.addCategoryObject('typeBinding', u'ldapGroup', ldapGroup_)


# Complex type alerts_ with content type ELEMENT_ONLY
class alerts_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'alerts')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}alert uses Python identifier alert
    __alert = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'alert'), 'alert', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_alerts__httpdocs_openstack_orgloadbalancersapimanagementv1_0alert', True)

    
    alert = property(__alert.value, __alert.set, None, None)


    _ElementMap = {
        __alert.name() : __alert
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'alerts', alerts_)


# Complex type loadBalancerUsageRecord with content type EMPTY
class loadBalancerUsageRecord (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsageRecord')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute averageNumConnectionsSsl uses Python identifier averageNumConnectionsSsl
    __averageNumConnectionsSsl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'averageNumConnectionsSsl'), 'averageNumConnectionsSsl', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_averageNumConnectionsSsl', pyxb.binding.datatypes.double)
    
    averageNumConnectionsSsl = property(__averageNumConnectionsSsl.value, __averageNumConnectionsSsl.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)

    
    # Attribute averageNumConnections uses Python identifier averageNumConnections
    __averageNumConnections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'averageNumConnections'), 'averageNumConnections', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_averageNumConnections', pyxb.binding.datatypes.double)
    
    averageNumConnections = property(__averageNumConnections.value, __averageNumConnections.set, None, None)

    
    # Attribute numVips uses Python identifier numVips
    __numVips = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numVips'), 'numVips', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_numVips', pyxb.binding.datatypes.int)
    
    numVips = property(__numVips.value, __numVips.set, None, None)

    
    # Attribute startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'startTime'), 'startTime', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_startTime', pyxb.binding.datatypes.dateTime)
    
    startTime = property(__startTime.value, __startTime.set, None, None)

    
    # Attribute eventType uses Python identifier eventType
    __eventType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'eventType'), 'eventType', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_eventType', pyxb.binding.datatypes.string)
    
    eventType = property(__eventType.value, __eventType.set, None, None)

    
    # Attribute incomingTransferSsl uses Python identifier incomingTransferSsl
    __incomingTransferSsl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'incomingTransferSsl'), 'incomingTransferSsl', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_incomingTransferSsl', pyxb.binding.datatypes.long)
    
    incomingTransferSsl = property(__incomingTransferSsl.value, __incomingTransferSsl.set, None, None)

    
    # Attribute incomingTransfer uses Python identifier incomingTransfer
    __incomingTransfer = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'incomingTransfer'), 'incomingTransfer', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_incomingTransfer', pyxb.binding.datatypes.long)
    
    incomingTransfer = property(__incomingTransfer.value, __incomingTransfer.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute loadBalancerId uses Python identifier loadBalancerId
    __loadBalancerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadBalancerId'), 'loadBalancerId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_loadBalancerId', pyxb.binding.datatypes.int)
    
    loadBalancerId = property(__loadBalancerId.value, __loadBalancerId.set, None, None)

    
    # Attribute outgoingTransferSsl uses Python identifier outgoingTransferSsl
    __outgoingTransferSsl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'outgoingTransferSsl'), 'outgoingTransferSsl', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_outgoingTransferSsl', pyxb.binding.datatypes.long)
    
    outgoingTransferSsl = property(__outgoingTransferSsl.value, __outgoingTransferSsl.set, None, None)

    
    # Attribute sslMode uses Python identifier sslMode
    __sslMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'sslMode'), 'sslMode', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_sslMode', pyxb.binding.datatypes.string)
    
    sslMode = property(__sslMode.value, __sslMode.set, None, None)

    
    # Attribute endTime uses Python identifier endTime
    __endTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'endTime'), 'endTime', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_endTime', pyxb.binding.datatypes.dateTime)
    
    endTime = property(__endTime.value, __endTime.set, None, None)

    
    # Attribute outgoingTransfer uses Python identifier outgoingTransfer
    __outgoingTransfer = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'outgoingTransfer'), 'outgoingTransfer', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_outgoingTransfer', pyxb.binding.datatypes.long)
    
    outgoingTransfer = property(__outgoingTransfer.value, __outgoingTransfer.set, None, None)

    
    # Attribute vipType uses Python identifier vipType
    __vipType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vipType'), 'vipType', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_vipType', lbaas.vipType)
    
    vipType = property(__vipType.value, __vipType.set, None, None)

    
    # Attribute numPolls uses Python identifier numPolls
    __numPolls = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numPolls'), 'numPolls', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerUsageRecord_numPolls', pyxb.binding.datatypes.int)
    
    numPolls = property(__numPolls.value, __numPolls.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __averageNumConnectionsSsl.name() : __averageNumConnectionsSsl,
        __accountId.name() : __accountId,
        __averageNumConnections.name() : __averageNumConnections,
        __numVips.name() : __numVips,
        __startTime.name() : __startTime,
        __eventType.name() : __eventType,
        __incomingTransferSsl.name() : __incomingTransferSsl,
        __incomingTransfer.name() : __incomingTransfer,
        __id.name() : __id,
        __loadBalancerId.name() : __loadBalancerId,
        __outgoingTransferSsl.name() : __outgoingTransferSsl,
        __sslMode.name() : __sslMode,
        __endTime.name() : __endTime,
        __outgoingTransfer.name() : __outgoingTransfer,
        __vipType.name() : __vipType,
        __numPolls.name() : __numPolls
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancerUsageRecord', loadBalancerUsageRecord)


# Complex type hostsubnet_ with content type ELEMENT_ONLY
class hostsubnet_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hostsubnet')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}netInterface uses Python identifier netInterface
    __netInterface = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'netInterface'), 'netInterface', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostsubnet__httpdocs_openstack_orgloadbalancersapimanagementv1_0netInterface', True)

    
    netInterface = property(__netInterface.value, __netInterface.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostsubnet__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __netInterface.name() : __netInterface
    }
    _AttributeMap = {
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'hostsubnet', hostsubnet_)


# Complex type event_ with content type EMPTY
class event_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'event')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute author uses Python identifier author
    __author = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'author'), 'author', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_event__author', pyxb.binding.datatypes.string)
    
    author = property(__author.value, __author.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_event__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)

    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'category'), 'category', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_event__category', pyxb.binding.datatypes.string)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute loadbalancerId uses Python identifier loadbalancerId
    __loadbalancerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadbalancerId'), 'loadbalancerId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_event__loadbalancerId', pyxb.binding.datatypes.int)
    
    loadbalancerId = property(__loadbalancerId.value, __loadbalancerId.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_event__title', pyxb.binding.datatypes.string)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_event__severity', pyxb.binding.datatypes.string)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_event__description', pyxb.binding.datatypes.string)
    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute relativeUri uses Python identifier relativeUri
    __relativeUri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'relativeUri'), 'relativeUri', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_event__relativeUri', pyxb.binding.datatypes.string)
    
    relativeUri = property(__relativeUri.value, __relativeUri.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_event__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_event__type', pyxb.binding.datatypes.string)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'created'), 'created', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_event__created', pyxb.binding.datatypes.string)
    
    created = property(__created.value, __created.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __author.name() : __author,
        __accountId.name() : __accountId,
        __category.name() : __category,
        __loadbalancerId.name() : __loadbalancerId,
        __title.name() : __title,
        __severity.name() : __severity,
        __description.name() : __description,
        __relativeUri.name() : __relativeUri,
        __id.name() : __id,
        __type.name() : __type,
        __created.name() : __created
    }
Namespace.addCategoryObject('typeBinding', u'event', event_)


# Complex type loadBalancerServiceEvent_ with content type EMPTY
class loadBalancerServiceEvent_ (event_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancerServiceEvent')
    # Base type is event_
    
    # Attribute author inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute accountId inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute category inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute loadbalancerId inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute title inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute severity inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute description inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute relativeUri inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute id inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute type inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute created inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event

    _ElementMap = event_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = event_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'loadBalancerServiceEvent', loadBalancerServiceEvent_)


# Complex type virtualIp_ with content type ELEMENT_ONLY
class virtualIp_ (lbaas.virtualIp_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualIp')
    # Base type is lbaas.virtualIp_
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}ticket uses Python identifier ticket
    __ticket = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ticket'), 'ticket', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIp__httpdocs_openstack_orgloadbalancersapimanagementv1_0ticket', False)

    
    ticket = property(__ticket.value, __ticket.set, None, None)

    
    # Attribute type inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}virtualIp
    
    # Attribute loadBalancerId uses Python identifier loadBalancerId
    __loadBalancerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadBalancerId'), 'loadBalancerId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIp__loadBalancerId', pyxb.binding.datatypes.int)
    
    loadBalancerId = property(__loadBalancerId.value, __loadBalancerId.set, None, None)

    
    # Attribute id inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}virtualIp
    
    # Attribute clusterId uses Python identifier clusterId
    __clusterId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'clusterId'), 'clusterId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIp__clusterId', pyxb.binding.datatypes.int)
    
    clusterId = property(__clusterId.value, __clusterId.set, None, None)

    
    # Attribute address inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}virtualIp
    
    # Attribute ipVersion inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}virtualIp

    _ElementMap = lbaas.virtualIp_._ElementMap.copy()
    _ElementMap.update({
        __ticket.name() : __ticket
    })
    _AttributeMap = lbaas.virtualIp_._AttributeMap.copy()
    _AttributeMap.update({
        __loadBalancerId.name() : __loadBalancerId,
        __clusterId.name() : __clusterId
    })
Namespace.addCategoryObject('typeBinding', u'virtualIp', virtualIp_)


# Complex type clusterDetails_ with content type ELEMENT_ONLY
class clusterDetails_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'clusterDetails')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}virtualIpBlocks uses Python identifier virtualIpBlocks
    __virtualIpBlocks = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'virtualIpBlocks'), 'virtualIpBlocks', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_clusterDetails__httpdocs_openstack_orgloadbalancersapimanagementv1_0virtualIpBlocks', False)

    
    virtualIpBlocks = property(__virtualIpBlocks.value, __virtualIpBlocks.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}cluster uses Python identifier cluster
    __cluster = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cluster'), 'cluster', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_clusterDetails__httpdocs_openstack_orgloadbalancersapimanagementv1_0cluster', False)

    
    cluster = property(__cluster.value, __cluster.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}hostMachineDetails uses Python identifier hostMachineDetails
    __hostMachineDetails = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hostMachineDetails'), 'hostMachineDetails', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_clusterDetails__httpdocs_openstack_orgloadbalancersapimanagementv1_0hostMachineDetails', False)

    
    hostMachineDetails = property(__hostMachineDetails.value, __hostMachineDetails.set, None, None)

    
    # Attribute numberOfActiveLoadBalancer uses Python identifier numberOfActiveLoadBalancer
    __numberOfActiveLoadBalancer = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numberOfActiveLoadBalancer'), 'numberOfActiveLoadBalancer', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_clusterDetails__numberOfActiveLoadBalancer', pyxb.binding.datatypes.int)
    
    numberOfActiveLoadBalancer = property(__numberOfActiveLoadBalancer.value, __numberOfActiveLoadBalancer.set, None, None)

    
    # Attribute noOfuniqueCustomer uses Python identifier noOfuniqueCustomer
    __noOfuniqueCustomer = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'noOfuniqueCustomer'), 'noOfuniqueCustomer', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_clusterDetails__noOfuniqueCustomer', pyxb.binding.datatypes.int)
    
    noOfuniqueCustomer = property(__noOfuniqueCustomer.value, __noOfuniqueCustomer.set, None, None)

    
    # Attribute averageUtilizationofHosts uses Python identifier averageUtilizationofHosts
    __averageUtilizationofHosts = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'averageUtilizationofHosts'), 'averageUtilizationofHosts', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_clusterDetails__averageUtilizationofHosts', pyxb.binding.datatypes.string)
    
    averageUtilizationofHosts = property(__averageUtilizationofHosts.value, __averageUtilizationofHosts.set, None, None)

    
    # Attribute numberOfHostMachines uses Python identifier numberOfHostMachines
    __numberOfHostMachines = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numberOfHostMachines'), 'numberOfHostMachines', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_clusterDetails__numberOfHostMachines', pyxb.binding.datatypes.int)
    
    numberOfHostMachines = property(__numberOfHostMachines.value, __numberOfHostMachines.set, None, None)

    
    # Attribute clusterStatus uses Python identifier clusterStatus
    __clusterStatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'clusterStatus'), 'clusterStatus', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_clusterDetails__clusterStatus', pyxb.binding.datatypes.string)
    
    clusterStatus = property(__clusterStatus.value, __clusterStatus.set, None, None)


    _ElementMap = {
        __virtualIpBlocks.name() : __virtualIpBlocks,
        __cluster.name() : __cluster,
        __hostMachineDetails.name() : __hostMachineDetails
    }
    _AttributeMap = {
        __numberOfActiveLoadBalancer.name() : __numberOfActiveLoadBalancer,
        __noOfuniqueCustomer.name() : __noOfuniqueCustomer,
        __averageUtilizationofHosts.name() : __averageUtilizationofHosts,
        __numberOfHostMachines.name() : __numberOfHostMachines,
        __clusterStatus.name() : __clusterStatus
    }
Namespace.addCategoryObject('typeBinding', u'clusterDetails', clusterDetails_)


# Complex type accountsInCluster_ with content type ELEMENT_ONLY
class accountsInCluster_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountsInCluster')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}accountInCluster uses Python identifier accountInCluster
    __accountInCluster = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountInCluster'), 'accountInCluster', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountsInCluster__httpdocs_openstack_orgloadbalancersapimanagementv1_0accountInCluster', True)

    
    accountInCluster = property(__accountInCluster.value, __accountInCluster.set, None, None)

    
    # Attribute totalAccounts uses Python identifier totalAccounts
    __totalAccounts = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'totalAccounts'), 'totalAccounts', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountsInCluster__totalAccounts', pyxb.binding.datatypes.int)
    
    totalAccounts = property(__totalAccounts.value, __totalAccounts.set, None, None)


    _ElementMap = {
        __accountInCluster.name() : __accountInCluster
    }
    _AttributeMap = {
        __totalAccounts.name() : __totalAccounts
    }
Namespace.addCategoryObject('typeBinding', u'accountsInCluster', accountsInCluster_)


# Complex type alert_ with content type EMPTY
class alert_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'alert')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_alert__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute alertType uses Python identifier alertType
    __alertType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'alertType'), 'alertType', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_alert__alertType', pyxb.binding.datatypes.string)
    
    alertType = property(__alertType.value, __alertType.set, None, None)

    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'created'), 'created', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_alert__created', pyxb.binding.datatypes.dateTime)
    
    created = property(__created.value, __created.set, None, None)

    
    # Attribute messageName uses Python identifier messageName
    __messageName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'messageName'), 'messageName', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_alert__messageName', pyxb.binding.datatypes.string)
    
    messageName = property(__messageName.value, __messageName.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_alert__status', alertStatus)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_alert__message', pyxb.binding.datatypes.string)
    
    message = property(__message.value, __message.set, None, None)

    
    # Attribute loadbalancerId uses Python identifier loadbalancerId
    __loadbalancerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadbalancerId'), 'loadbalancerId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_alert__loadbalancerId', pyxb.binding.datatypes.int)
    
    loadbalancerId = property(__loadbalancerId.value, __loadbalancerId.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_alert__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __id.name() : __id,
        __alertType.name() : __alertType,
        __created.name() : __created,
        __messageName.name() : __messageName,
        __status.name() : __status,
        __message.name() : __message,
        __loadbalancerId.name() : __loadbalancerId,
        __accountId.name() : __accountId
    }
Namespace.addCategoryObject('typeBinding', u'alert', alert_)


# Complex type groupRateLimits_ with content type ELEMENT_ONLY
class groupRateLimits_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'groupRateLimits')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}groupRateLimit uses Python identifier groupRateLimit
    __groupRateLimit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'groupRateLimit'), 'groupRateLimit', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_groupRateLimits__httpdocs_openstack_orgloadbalancersapimanagementv1_0groupRateLimit', True)

    
    groupRateLimit = property(__groupRateLimit.value, __groupRateLimit.set, None, None)


    _ElementMap = {
        __groupRateLimit.name() : __groupRateLimit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'groupRateLimits', groupRateLimits_)


# Complex type zeusRateLimitedLoadBalancers_ with content type ELEMENT_ONLY
class zeusRateLimitedLoadBalancers_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'zeusRateLimitedLoadBalancers')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}zeusRateLimitedLoadBalancer uses Python identifier zeusRateLimitedLoadBalancer
    __zeusRateLimitedLoadBalancer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'zeusRateLimitedLoadBalancer'), 'zeusRateLimitedLoadBalancer', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_zeusRateLimitedLoadBalancers__httpdocs_openstack_orgloadbalancersapimanagementv1_0zeusRateLimitedLoadBalancer', True)

    
    zeusRateLimitedLoadBalancer = property(__zeusRateLimitedLoadBalancer.value, __zeusRateLimitedLoadBalancer.set, None, None)


    _ElementMap = {
        __zeusRateLimitedLoadBalancer.name() : __zeusRateLimitedLoadBalancer
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'zeusRateLimitedLoadBalancers', zeusRateLimitedLoadBalancers_)


# Complex type account_ with content type EMPTY
class account_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'account')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_account__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __id.name() : __id
    }
Namespace.addCategoryObject('typeBinding', u'account', account_)


# Complex type healthCheck_ with content type EMPTY
class healthCheck_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'healthCheck')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_healthCheck__type', pyxb.binding.datatypes.string)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute time uses Python identifier time
    __time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'time'), 'time', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_healthCheck__time', pyxb.binding.datatypes.long)
    
    time = property(__time.value, __time.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_healthCheck__status', pyxb.binding.datatypes.string)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_healthCheck__message', pyxb.binding.datatypes.string)
    
    message = property(__message.value, __message.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __type.name() : __type,
        __time.name() : __time,
        __status.name() : __status,
        __message.name() : __message
    }
Namespace.addCategoryObject('typeBinding', u'healthCheck', healthCheck_)


# Complex type hostUsages_ with content type ELEMENT_ONLY
class hostUsages_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hostUsages')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}hostUsage uses Python identifier hostUsage
    __hostUsage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hostUsage'), 'hostUsage', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostUsages__httpdocs_openstack_orgloadbalancersapimanagementv1_0hostUsage', True)

    
    hostUsage = property(__hostUsage.value, __hostUsage.set, None, None)


    _ElementMap = {
        __hostUsage.name() : __hostUsage
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'hostUsages', hostUsages_)


# Complex type cidr_ with content type EMPTY
class cidr_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cidr')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute block uses Python identifier block
    __block = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'block'), 'block', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cidr__block', pyxb.binding.datatypes.string)
    
    block = property(__block.value, __block.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __block.name() : __block
    }
Namespace.addCategoryObject('typeBinding', u'cidr', cidr_)


# Complex type suspension_ with content type ELEMENT_ONLY
class suspension_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'suspension')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}ticket uses Python identifier ticket
    __ticket = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ticket'), 'ticket', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_suspension__httpdocs_openstack_orgloadbalancersapimanagementv1_0ticket', False)

    
    ticket = property(__ticket.value, __ticket.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_suspension__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute reason uses Python identifier reason
    __reason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'reason'), 'reason', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_suspension__reason', pyxb.binding.datatypes.string)
    
    reason = property(__reason.value, __reason.set, None, None)

    
    # Attribute user uses Python identifier user
    __user = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'user'), 'user', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_suspension__user', pyxb.binding.datatypes.string)
    
    user = property(__user.value, __user.set, None, None)


    _ElementMap = {
        __ticket.name() : __ticket
    }
    _AttributeMap = {
        __id.name() : __id,
        __reason.name() : __reason,
        __user.name() : __user
    }
Namespace.addCategoryObject('typeBinding', u'suspension', suspension_)


# Complex type allAbsoluteLimits_ with content type ELEMENT_ONLY
class allAbsoluteLimits_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'allAbsoluteLimits')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}defaultLimits uses Python identifier defaultLimits
    __defaultLimits = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'defaultLimits'), 'defaultLimits', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_allAbsoluteLimits__httpdocs_openstack_orgloadbalancersapimanagementv1_0defaultLimits', False)

    
    defaultLimits = property(__defaultLimits.value, __defaultLimits.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}customLimits uses Python identifier customLimits
    __customLimits = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customLimits'), 'customLimits', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_allAbsoluteLimits__httpdocs_openstack_orgloadbalancersapimanagementv1_0customLimits', False)

    
    customLimits = property(__customLimits.value, __customLimits.set, None, None)


    _ElementMap = {
        __defaultLimits.name() : __defaultLimits,
        __customLimits.name() : __customLimits
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'allAbsoluteLimits', allAbsoluteLimits_)


# Complex type zeusRateLimitedLoadBalancer_ with content type ELEMENT_ONLY
class zeusRateLimitedLoadBalancer_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'zeusRateLimitedLoadBalancer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}tickets uses Python identifier tickets
    __tickets = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tickets'), 'tickets', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_zeusRateLimitedLoadBalancer__httpdocs_openstack_orgloadbalancersapimanagementv1_0tickets', False)

    
    tickets = property(__tickets.value, __tickets.set, None, None)

    
    # Attribute loadbalancerId uses Python identifier loadbalancerId
    __loadbalancerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadbalancerId'), 'loadbalancerId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_zeusRateLimitedLoadBalancer__loadbalancerId', pyxb.binding.datatypes.int)
    
    loadbalancerId = property(__loadbalancerId.value, __loadbalancerId.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_zeusRateLimitedLoadBalancer__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)

    
    # Attribute maxRequestsPerSecond uses Python identifier maxRequestsPerSecond
    __maxRequestsPerSecond = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'maxRequestsPerSecond'), 'maxRequestsPerSecond', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_zeusRateLimitedLoadBalancer__maxRequestsPerSecond', pyxb.binding.datatypes.int)
    
    maxRequestsPerSecond = property(__maxRequestsPerSecond.value, __maxRequestsPerSecond.set, None, None)

    
    # Attribute expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'expirationTime'), 'expirationTime', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_zeusRateLimitedLoadBalancer__expirationTime', pyxb.binding.datatypes.string)
    
    expirationTime = property(__expirationTime.value, __expirationTime.set, None, None)


    _ElementMap = {
        __tickets.name() : __tickets
    }
    _AttributeMap = {
        __loadbalancerId.name() : __loadbalancerId,
        __accountId.name() : __accountId,
        __maxRequestsPerSecond.name() : __maxRequestsPerSecond,
        __expirationTime.name() : __expirationTime
    }
Namespace.addCategoryObject('typeBinding', u'zeusRateLimitedLoadBalancer', zeusRateLimitedLoadBalancer_)


# Complex type backups_ with content type ELEMENT_ONLY
class backups_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'backups')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}backup uses Python identifier backup
    __backup = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'backup'), 'backup', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_backups__httpdocs_openstack_orgloadbalancersapimanagementv1_0backup', True)

    
    backup = property(__backup.value, __backup.set, None, None)


    _ElementMap = {
        __backup.name() : __backup
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'backups', backups_)


# Complex type accountsInHost_ with content type ELEMENT_ONLY
class accountsInHost_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountsInHost')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}accountInHost uses Python identifier accountInHost
    __accountInHost = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountInHost'), 'accountInHost', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountsInHost__httpdocs_openstack_orgloadbalancersapimanagementv1_0accountInHost', True)

    
    accountInHost = property(__accountInHost.value, __accountInHost.set, None, None)

    
    # Attribute totalAccounts uses Python identifier totalAccounts
    __totalAccounts = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'totalAccounts'), 'totalAccounts', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountsInHost__totalAccounts', pyxb.binding.datatypes.int)
    
    totalAccounts = property(__totalAccounts.value, __totalAccounts.set, None, None)


    _ElementMap = {
        __accountInHost.name() : __accountInHost
    }
    _AttributeMap = {
        __totalAccounts.name() : __totalAccounts
    }
Namespace.addCategoryObject('typeBinding', u'accountsInHost', accountsInHost_)


# Complex type loadBalancerServiceEvents_ with content type ELEMENT_ONLY
class loadBalancerServiceEvents_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancerServiceEvents')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}loadBalancerServiceEvent uses Python identifier loadBalancerServiceEvent
    __loadBalancerServiceEvent = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerServiceEvent'), 'loadBalancerServiceEvent', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerServiceEvents__httpdocs_openstack_orgloadbalancersapimanagementv1_0loadBalancerServiceEvent', True)

    
    loadBalancerServiceEvent = property(__loadBalancerServiceEvent.value, __loadBalancerServiceEvent.set, None, None)

    
    # Attribute loadbalancerId uses Python identifier loadbalancerId
    __loadbalancerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadbalancerId'), 'loadbalancerId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerServiceEvents__loadbalancerId', pyxb.binding.datatypes.int)
    
    loadbalancerId = property(__loadbalancerId.value, __loadbalancerId.set, None, None)


    _ElementMap = {
        __loadBalancerServiceEvent.name() : __loadBalancerServiceEvent
    }
    _AttributeMap = {
        __loadbalancerId.name() : __loadbalancerId
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancerServiceEvents', loadBalancerServiceEvents_)


# Complex type loadBalancer_ with content type ELEMENT_ONLY
class loadBalancer_ (lbaas.loadBalancer_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancer')
    # Base type is lbaas.loadBalancer_
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}suspension uses Python identifier suspension
    __suspension = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'suspension'), 'suspension', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapimanagementv1_0suspension', False)

    
    suspension = property(__suspension.value, __suspension.set, None, None)

    
    # Element healthMonitor ({http://docs.openstack.org/loadbalancers/api/v1.0}healthMonitor) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}tickets uses Python identifier tickets
    __tickets = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tickets'), 'tickets', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapimanagementv1_0tickets', False)

    
    tickets = property(__tickets.value, __tickets.set, None, None)

    
    # Element loadBalancerUsage ({http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancerUsage) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element updated ({http://docs.openstack.org/loadbalancers/api/v1.0}updated) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element nodes ({http://docs.openstack.org/loadbalancers/api/v1.0}nodes) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element sslTermination ({http://docs.openstack.org/loadbalancers/api/v1.0}sslTermination) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element connectionLogging ({http://docs.openstack.org/loadbalancers/api/v1.0}connectionLogging) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}rateLimit uses Python identifier rateLimit
    __rateLimit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rateLimit'), 'rateLimit', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapimanagementv1_0rateLimit', False)

    
    rateLimit = property(__rateLimit.value, __rateLimit.set, None, None)

    
    # Element virtualIps ({http://docs.openstack.org/loadbalancers/api/v1.0}virtualIps) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}host uses Python identifier host
    __host = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'host'), 'host', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapimanagementv1_0host', False)

    
    host = property(__host.value, __host.set, None, None)

    
    # Element accessList ({http://docs.openstack.org/loadbalancers/api/v1.0}accessList) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element sourceAddresses ({http://docs.openstack.org/loadbalancers/api/v1.0}sourceAddresses) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element cluster ({http://docs.openstack.org/loadbalancers/api/v1.0}cluster) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element sessionPersistence ({http://docs.openstack.org/loadbalancers/api/v1.0}sessionPersistence) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}accountLoadBalancerServiceEvents uses Python identifier accountLoadBalancerServiceEvents
    __accountLoadBalancerServiceEvents = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountLoadBalancerServiceEvents'), 'accountLoadBalancerServiceEvents', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancer__httpdocs_openstack_orgloadbalancersapimanagementv1_0accountLoadBalancerServiceEvents', False)

    
    accountLoadBalancerServiceEvents = property(__accountLoadBalancerServiceEvents.value, __accountLoadBalancerServiceEvents.set, None, None)

    
    # Element connectionThrottle ({http://docs.openstack.org/loadbalancers/api/v1.0}connectionThrottle) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element contentCaching ({http://docs.openstack.org/loadbalancers/api/v1.0}contentCaching) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element metadata ({http://docs.openstack.org/loadbalancers/api/v1.0}metadata) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Element created ({http://docs.openstack.org/loadbalancers/api/v1.0}created) inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Attribute sticky uses Python identifier sticky
    __sticky = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'sticky'), 'sticky', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancer__sticky', pyxb.binding.datatypes.boolean)
    
    sticky = property(__sticky.value, __sticky.set, None, None)

    
    # Attribute isSticky inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Attribute id inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Attribute protocol inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Attribute nodeCount inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Attribute totalActiveConnections uses Python identifier totalActiveConnections
    __totalActiveConnections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'totalActiveConnections'), 'totalActiveConnections', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancer__totalActiveConnections', pyxb.binding.datatypes.int)
    
    totalActiveConnections = property(__totalActiveConnections.value, __totalActiveConnections.set, None, None)

    
    # Attribute port inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancer__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)

    
    # Attribute name inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Attribute status inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer
    
    # Attribute algorithm inherited from {http://docs.openstack.org/loadbalancers/api/v1.0}loadBalancer

    _ElementMap = lbaas.loadBalancer_._ElementMap.copy()
    _ElementMap.update({
        __suspension.name() : __suspension,
        __tickets.name() : __tickets,
        __rateLimit.name() : __rateLimit,
        __host.name() : __host,
        __accountLoadBalancerServiceEvents.name() : __accountLoadBalancerServiceEvents
    })
    _AttributeMap = lbaas.loadBalancer_._AttributeMap.copy()
    _AttributeMap.update({
        __sticky.name() : __sticky,
        __totalActiveConnections.name() : __totalActiveConnections,
        __accountId.name() : __accountId
    })
Namespace.addCategoryObject('typeBinding', u'loadBalancer', loadBalancer_)


# Complex type loadBalancerEvent_ with content type EMPTY
class loadBalancerEvent_ (event_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancerEvent')
    # Base type is event_
    
    # Attribute author inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute accountId inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute category inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute loadbalancerId inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute title inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute severity inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute description inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute relativeUri inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute id inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute type inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event
    
    # Attribute created inherited from {http://docs.openstack.org/loadbalancers/api/management/v1.0}event

    _ElementMap = event_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = event_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'loadBalancerEvent', loadBalancerEvent_)


# Complex type virtualIpBlock_ with content type EMPTY
class virtualIpBlock_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualIpBlock')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute firstIp uses Python identifier firstIp
    __firstIp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'firstIp'), 'firstIp', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpBlock__firstIp', pyxb.binding.datatypes.string)
    
    firstIp = property(__firstIp.value, __firstIp.set, None, None)

    
    # Attribute lastIp uses Python identifier lastIp
    __lastIp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lastIp'), 'lastIp', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpBlock__lastIp', pyxb.binding.datatypes.string)
    
    lastIp = property(__lastIp.value, __lastIp.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __firstIp.name() : __firstIp,
        __lastIp.name() : __lastIp
    }
Namespace.addCategoryObject('typeBinding', u'virtualIpBlock', virtualIpBlock_)


# Complex type hostMachineDetails_ with content type ELEMENT_ONLY
class hostMachineDetails_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hostMachineDetails')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}host uses Python identifier host
    __host = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'host'), 'host', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostMachineDetails__httpdocs_openstack_orgloadbalancersapimanagementv1_0host', False)

    
    host = property(__host.value, __host.set, None, None)

    
    # Attribute totalConcurrentConnections uses Python identifier totalConcurrentConnections
    __totalConcurrentConnections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'totalConcurrentConnections'), 'totalConcurrentConnections', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostMachineDetails__totalConcurrentConnections', pyxb.binding.datatypes.int)
    
    totalConcurrentConnections = property(__totalConcurrentConnections.value, __totalConcurrentConnections.set, None, None)

    
    # Attribute uniqueCustomers uses Python identifier uniqueCustomers
    __uniqueCustomers = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uniqueCustomers'), 'uniqueCustomers', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostMachineDetails__uniqueCustomers', pyxb.binding.datatypes.int)
    
    uniqueCustomers = property(__uniqueCustomers.value, __uniqueCustomers.set, None, None)

    
    # Attribute activeLBConfigurations uses Python identifier activeLBConfigurations
    __activeLBConfigurations = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'activeLBConfigurations'), 'activeLBConfigurations', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostMachineDetails__activeLBConfigurations', pyxb.binding.datatypes.long)
    
    activeLBConfigurations = property(__activeLBConfigurations.value, __activeLBConfigurations.set, None, None)

    
    # Attribute availableConcurrentConnections uses Python identifier availableConcurrentConnections
    __availableConcurrentConnections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'availableConcurrentConnections'), 'availableConcurrentConnections', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostMachineDetails__availableConcurrentConnections', pyxb.binding.datatypes.int)
    
    availableConcurrentConnections = property(__availableConcurrentConnections.value, __availableConcurrentConnections.set, None, None)

    
    # Attribute currentUtilization uses Python identifier currentUtilization
    __currentUtilization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'currentUtilization'), 'currentUtilization', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostMachineDetails__currentUtilization', pyxb.binding.datatypes.string)
    
    currentUtilization = property(__currentUtilization.value, __currentUtilization.set, None, None)


    _ElementMap = {
        __host.name() : __host
    }
    _AttributeMap = {
        __totalConcurrentConnections.name() : __totalConcurrentConnections,
        __uniqueCustomers.name() : __uniqueCustomers,
        __activeLBConfigurations.name() : __activeLBConfigurations,
        __availableConcurrentConnections.name() : __availableConcurrentConnections,
        __currentUtilization.name() : __currentUtilization
    }
Namespace.addCategoryObject('typeBinding', u'hostMachineDetails', hostMachineDetails_)


# Complex type accounts_ with content type ELEMENT_ONLY
class accounts_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accounts')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}account uses Python identifier account
    __account = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'account'), 'account', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accounts__httpdocs_openstack_orgloadbalancersapimanagementv1_0account', True)

    
    account = property(__account.value, __account.set, None, None)


    _ElementMap = {
        __account.name() : __account
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'accounts', accounts_)


# Complex type accountLoadBalancer_ with content type EMPTY
class accountLoadBalancer_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountLoadBalancer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute clusterName uses Python identifier clusterName
    __clusterName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'clusterName'), 'clusterName', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountLoadBalancer__clusterName', pyxb.binding.datatypes.string)
    
    clusterName = property(__clusterName.value, __clusterName.set, None, None)

    
    # Attribute loadBalancerName uses Python identifier loadBalancerName
    __loadBalancerName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadBalancerName'), 'loadBalancerName', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountLoadBalancer__loadBalancerName', pyxb.binding.datatypes.string)
    
    loadBalancerName = property(__loadBalancerName.value, __loadBalancerName.set, None, None)

    
    # Attribute loadBalancerId uses Python identifier loadBalancerId
    __loadBalancerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadBalancerId'), 'loadBalancerId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountLoadBalancer__loadBalancerId', pyxb.binding.datatypes.int)
    
    loadBalancerId = property(__loadBalancerId.value, __loadBalancerId.set, None, None)

    
    # Attribute protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'protocol'), 'protocol', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountLoadBalancer__protocol', pyxb.binding.datatypes.string)
    
    protocol = property(__protocol.value, __protocol.set, None, None)

    
    # Attribute loadBalancerStatus uses Python identifier loadBalancerStatus
    __loadBalancerStatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadBalancerStatus'), 'loadBalancerStatus', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountLoadBalancer__loadBalancerStatus', pyxb.binding.datatypes.string)
    
    loadBalancerStatus = property(__loadBalancerStatus.value, __loadBalancerStatus.set, None, None)

    
    # Attribute clusterId uses Python identifier clusterId
    __clusterId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'clusterId'), 'clusterId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountLoadBalancer__clusterId', pyxb.binding.datatypes.int)
    
    clusterId = property(__clusterId.value, __clusterId.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountLoadBalancer__status', pyxb.binding.datatypes.string)
    
    status = property(__status.value, __status.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __clusterName.name() : __clusterName,
        __loadBalancerName.name() : __loadBalancerName,
        __loadBalancerId.name() : __loadBalancerId,
        __protocol.name() : __protocol,
        __loadBalancerStatus.name() : __loadBalancerStatus,
        __clusterId.name() : __clusterId,
        __status.name() : __status
    }
Namespace.addCategoryObject('typeBinding', u'accountLoadBalancer', accountLoadBalancer_)


# Complex type rateLimit_ with content type ELEMENT_ONLY
class rateLimit_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rateLimit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}ticket uses Python identifier ticket
    __ticket = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ticket'), 'ticket', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_rateLimit__httpdocs_openstack_orgloadbalancersapimanagementv1_0ticket', False)

    
    ticket = property(__ticket.value, __ticket.set, None, None)

    
    # Attribute maxRequestsPerSecond uses Python identifier maxRequestsPerSecond
    __maxRequestsPerSecond = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'maxRequestsPerSecond'), 'maxRequestsPerSecond', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_rateLimit__maxRequestsPerSecond', pyxb.binding.datatypes.int)
    
    maxRequestsPerSecond = property(__maxRequestsPerSecond.value, __maxRequestsPerSecond.set, None, None)

    
    # Attribute expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'expirationTime'), 'expirationTime', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_rateLimit__expirationTime', pyxb.binding.datatypes.dateTime)
    
    expirationTime = property(__expirationTime.value, __expirationTime.set, None, None)


    _ElementMap = {
        __ticket.name() : __ticket
    }
    _AttributeMap = {
        __maxRequestsPerSecond.name() : __maxRequestsPerSecond,
        __expirationTime.name() : __expirationTime
    }
Namespace.addCategoryObject('typeBinding', u'rateLimit', rateLimit_)


# Complex type accountInCluster_ with content type EMPTY
class accountInCluster_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountInCluster')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute clusterId uses Python identifier clusterId
    __clusterId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'clusterId'), 'clusterId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountInCluster__clusterId', pyxb.binding.datatypes.int)
    
    clusterId = property(__clusterId.value, __clusterId.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountInCluster__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)

    
    # Attribute loadBalancerCount uses Python identifier loadBalancerCount
    __loadBalancerCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadBalancerCount'), 'loadBalancerCount', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountInCluster__loadBalancerCount', pyxb.binding.datatypes.long)
    
    loadBalancerCount = property(__loadBalancerCount.value, __loadBalancerCount.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __clusterId.name() : __clusterId,
        __accountId.name() : __accountId,
        __loadBalancerCount.name() : __loadBalancerCount
    }
Namespace.addCategoryObject('typeBinding', u'accountInCluster', accountInCluster_)


# Complex type userRole_ with content type EMPTY
class userRole_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'userRole')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute roleName uses Python identifier roleName
    __roleName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'roleName'), 'roleName', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_userRole__roleName', pyxb.binding.datatypes.string)
    
    roleName = property(__roleName.value, __roleName.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __roleName.name() : __roleName
    }
Namespace.addCategoryObject('typeBinding', u'userRole', userRole_)


# Complex type CustomLimits_ with content type ELEMENT_ONLY
class CustomLimits_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CustomLimits')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}limit uses Python identifier limit
    __limit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'limit'), 'limit', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_CustomLimits__httpdocs_openstack_orgloadbalancersapiv1_0limit', True)

    
    limit = property(__limit.value, __limit.set, None, None)


    _ElementMap = {
        __limit.name() : __limit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CustomLimits', CustomLimits_)


# Complex type DefaultLimits_ with content type ELEMENT_ONLY
class DefaultLimits_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DefaultLimits')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}limit uses Python identifier limit
    __limit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'limit'), 'limit', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_DefaultLimits__httpdocs_openstack_orgloadbalancersapiv1_0limit', True)

    
    limit = property(__limit.value, __limit.set, None, None)


    _ElementMap = {
        __limit.name() : __limit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DefaultLimits', DefaultLimits_)


# Complex type loadBalancerAudit_ with content type ELEMENT_ONLY
class loadBalancerAudit_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancerAudit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}alertAudits uses Python identifier alertAudits
    __alertAudits = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'alertAudits'), 'alertAudits', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerAudit__httpdocs_openstack_orgloadbalancersapimanagementv1_0alertAudits', True)

    
    alertAudits = property(__alertAudits.value, __alertAudits.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerAudit__status', pyxb.binding.datatypes.string)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerAudit__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'created'), 'created', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerAudit__created', pyxb.binding.datatypes.dateTime)
    
    created = property(__created.value, __created.set, None, None)

    
    # Attribute updated uses Python identifier updated
    __updated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'updated'), 'updated', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerAudit__updated', pyxb.binding.datatypes.dateTime)
    
    updated = property(__updated.value, __updated.set, None, None)


    _ElementMap = {
        __alertAudits.name() : __alertAudits
    }
    _AttributeMap = {
        __status.name() : __status,
        __id.name() : __id,
        __created.name() : __created,
        __updated.name() : __updated
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancerAudit', loadBalancerAudit_)


# Complex type cluster_ with content type EMPTY
class cluster_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cluster')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute username uses Python identifier username
    __username = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'username'), 'username', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cluster__username', pyxb.binding.datatypes.string)
    
    username = property(__username.value, __username.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cluster__description', pyxb.binding.datatypes.string)
    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute utilization uses Python identifier utilization
    __utilization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'utilization'), 'utilization', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cluster__utilization', pyxb.binding.datatypes.string)
    
    utilization = property(__utilization.value, __utilization.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cluster__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute clusterIpv6Cidr uses Python identifier clusterIpv6Cidr
    __clusterIpv6Cidr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'clusterIpv6Cidr'), 'clusterIpv6Cidr', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cluster__clusterIpv6Cidr', pyxb.binding.datatypes.string)
    
    clusterIpv6Cidr = property(__clusterIpv6Cidr.value, __clusterIpv6Cidr.set, None, None)

    
    # Attribute numberOfLoadBalancingConfigurations uses Python identifier numberOfLoadBalancingConfigurations
    __numberOfLoadBalancingConfigurations = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numberOfLoadBalancingConfigurations'), 'numberOfLoadBalancingConfigurations', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cluster__numberOfLoadBalancingConfigurations', pyxb.binding.datatypes.int)
    
    numberOfLoadBalancingConfigurations = property(__numberOfLoadBalancingConfigurations.value, __numberOfLoadBalancingConfigurations.set, None, None)

    
    # Attribute numberOfHostMachines uses Python identifier numberOfHostMachines
    __numberOfHostMachines = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numberOfHostMachines'), 'numberOfHostMachines', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cluster__numberOfHostMachines', pyxb.binding.datatypes.int)
    
    numberOfHostMachines = property(__numberOfHostMachines.value, __numberOfHostMachines.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cluster__status', clusterStatus)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute numberOfUniqueCustomers uses Python identifier numberOfUniqueCustomers
    __numberOfUniqueCustomers = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numberOfUniqueCustomers'), 'numberOfUniqueCustomers', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cluster__numberOfUniqueCustomers', pyxb.binding.datatypes.int)
    
    numberOfUniqueCustomers = property(__numberOfUniqueCustomers.value, __numberOfUniqueCustomers.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cluster__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute dataCenter uses Python identifier dataCenter
    __dataCenter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dataCenter'), 'dataCenter', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cluster__dataCenter', dataCenter)
    
    dataCenter = property(__dataCenter.value, __dataCenter.set, None, None)

    
    # Attribute password uses Python identifier password
    __password = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'password'), 'password', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cluster__password', pyxb.binding.datatypes.string)
    
    password = property(__password.value, __password.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __username.name() : __username,
        __description.name() : __description,
        __utilization.name() : __utilization,
        __id.name() : __id,
        __clusterIpv6Cidr.name() : __clusterIpv6Cidr,
        __numberOfLoadBalancingConfigurations.name() : __numberOfLoadBalancingConfigurations,
        __numberOfHostMachines.name() : __numberOfHostMachines,
        __status.name() : __status,
        __numberOfUniqueCustomers.name() : __numberOfUniqueCustomers,
        __name.name() : __name,
        __dataCenter.name() : __dataCenter,
        __password.name() : __password
    }
Namespace.addCategoryObject('typeBinding', u'cluster', cluster_)


# Complex type tickets_ with content type ELEMENT_ONLY
class tickets_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'tickets')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}ticket uses Python identifier ticket
    __ticket = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ticket'), 'ticket', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_tickets__httpdocs_openstack_orgloadbalancersapimanagementv1_0ticket', True)

    
    ticket = property(__ticket.value, __ticket.set, None, None)


    _ElementMap = {
        __ticket.name() : __ticket
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'tickets', tickets_)


# Complex type loadBalancerLimitGroups_ with content type ELEMENT_ONLY
class loadBalancerLimitGroups_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancerLimitGroups')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}loadBalancerLimitGroup uses Python identifier loadBalancerLimitGroup
    __loadBalancerLimitGroup = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerLimitGroup'), 'loadBalancerLimitGroup', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerLimitGroups__httpdocs_openstack_orgloadbalancersapimanagementv1_0loadBalancerLimitGroup', True)

    
    loadBalancerLimitGroup = property(__loadBalancerLimitGroup.value, __loadBalancerLimitGroup.set, None, None)


    _ElementMap = {
        __loadBalancerLimitGroup.name() : __loadBalancerLimitGroup
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancerLimitGroups', loadBalancerLimitGroups_)


# Complex type loadBalancerStatusHistory_ with content type EMPTY
class loadBalancerStatusHistory_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancerStatusHistory')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'created'), 'created', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerStatusHistory__created', pyxb.binding.datatypes.dateTime)
    
    created = property(__created.value, __created.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerStatusHistory__status', pyxb.binding.datatypes.string)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerStatusHistory__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)

    
    # Attribute loadBalancerId uses Python identifier loadBalancerId
    __loadBalancerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadBalancerId'), 'loadBalancerId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerStatusHistory__loadBalancerId', pyxb.binding.datatypes.int)
    
    loadBalancerId = property(__loadBalancerId.value, __loadBalancerId.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __created.name() : __created,
        __status.name() : __status,
        __accountId.name() : __accountId,
        __loadBalancerId.name() : __loadBalancerId
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancerStatusHistory', loadBalancerStatusHistory_)


# Complex type CTD_ANON with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), 'link', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_CTD_ANON_httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}accountUsageRecord uses Python identifier accountUsageRecord
    __accountUsageRecord = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountUsageRecord'), 'accountUsageRecord', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_CTD_ANON_httpdocs_openstack_orgloadbalancersapimanagementv1_0accountUsageRecord', True)

    
    accountUsageRecord = property(__accountUsageRecord.value, __accountUsageRecord.set, None, None)


    _ElementMap = {
        __link.name() : __link,
        __accountUsageRecord.name() : __accountUsageRecord
    }
    _AttributeMap = {
        
    }



# Complex type accountGroups_ with content type ELEMENT_ONLY
class accountGroups_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountGroups')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}accountGroup uses Python identifier accountGroup
    __accountGroup = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountGroup'), 'accountGroup', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountGroups__httpdocs_openstack_orgloadbalancersapimanagementv1_0accountGroup', True)

    
    accountGroup = property(__accountGroup.value, __accountGroup.set, None, None)


    _ElementMap = {
        __accountGroup.name() : __accountGroup
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'accountGroups', accountGroups_)


# Complex type accountUsageRecord_ with content type EMPTY
class accountUsageRecord_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountUsageRecord')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountUsageRecord__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)

    
    # Attribute startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'startTime'), 'startTime', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountUsageRecord__startTime', pyxb.binding.datatypes.dateTime)
    
    startTime = property(__startTime.value, __startTime.set, None, None)

    
    # Attribute numLoadBalancers uses Python identifier numLoadBalancers
    __numLoadBalancers = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numLoadBalancers'), 'numLoadBalancers', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountUsageRecord__numLoadBalancers', pyxb.binding.datatypes.int)
    
    numLoadBalancers = property(__numLoadBalancers.value, __numLoadBalancers.set, None, None)

    
    # Attribute numPublicVips uses Python identifier numPublicVips
    __numPublicVips = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numPublicVips'), 'numPublicVips', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountUsageRecord__numPublicVips', pyxb.binding.datatypes.int)
    
    numPublicVips = property(__numPublicVips.value, __numPublicVips.set, None, None)

    
    # Attribute numServicenetVips uses Python identifier numServicenetVips
    __numServicenetVips = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numServicenetVips'), 'numServicenetVips', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountUsageRecord__numServicenetVips', pyxb.binding.datatypes.int)
    
    numServicenetVips = property(__numServicenetVips.value, __numServicenetVips.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __accountId.name() : __accountId,
        __startTime.name() : __startTime,
        __numLoadBalancers.name() : __numLoadBalancers,
        __numPublicVips.name() : __numPublicVips,
        __numServicenetVips.name() : __numServicenetVips
    }
Namespace.addCategoryObject('typeBinding', u'accountUsageRecord', accountUsageRecord_)


# Complex type byIdOrName_ with content type EMPTY
class byIdOrName_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'byIdOrName')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_byIdOrName__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_byIdOrName__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __id.name() : __id,
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'byIdOrName', byIdOrName_)


# Complex type virtualIps_ with content type ELEMENT_ONLY
class virtualIps_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualIps')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}virtualIp uses Python identifier virtualIp
    __virtualIp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'virtualIp'), 'virtualIp', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIps__httpdocs_openstack_orgloadbalancersapimanagementv1_0virtualIp', True)

    
    virtualIp = property(__virtualIp.value, __virtualIp.set, None, None)


    _ElementMap = {
        __virtualIp.name() : __virtualIp
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'virtualIps', virtualIps_)


# Complex type customLimitAccount_ with content type ELEMENT_ONLY
class customLimitAccount_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customLimitAccount')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}customLimits uses Python identifier customLimits
    __customLimits = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customLimits'), 'customLimits', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_customLimitAccount__httpdocs_openstack_orgloadbalancersapimanagementv1_0customLimits', False)

    
    customLimits = property(__customLimits.value, __customLimits.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_customLimitAccount__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)


    _ElementMap = {
        __customLimits.name() : __customLimits
    }
    _AttributeMap = {
        __accountId.name() : __accountId
    }
Namespace.addCategoryObject('typeBinding', u'customLimitAccount', customLimitAccount_)


# Complex type virtualIpBlocks_ with content type ELEMENT_ONLY
class virtualIpBlocks_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualIpBlocks')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}virtualIpBlock uses Python identifier virtualIpBlock
    __virtualIpBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'virtualIpBlock'), 'virtualIpBlock', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpBlocks__httpdocs_openstack_orgloadbalancersapimanagementv1_0virtualIpBlock', True)

    
    virtualIpBlock = property(__virtualIpBlock.value, __virtualIpBlock.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpBlocks__type', lbaas.vipType)
    
    type = property(__type.value, __type.set, None, None)


    _ElementMap = {
        __virtualIpBlock.name() : __virtualIpBlock
    }
    _AttributeMap = {
        __type.name() : __type
    }
Namespace.addCategoryObject('typeBinding', u'virtualIpBlocks', virtualIpBlocks_)


# Complex type CTD_ANON_ with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), 'link', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_CTD_ANON__httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}loadBalancerUsageRecord uses Python identifier loadBalancerUsageRecord
    __loadBalancerUsageRecord = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsageRecord'), 'loadBalancerUsageRecord', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_CTD_ANON__httpdocs_openstack_orgloadbalancersapimanagementv1_0loadBalancerUsageRecord', True)

    
    loadBalancerUsageRecord = property(__loadBalancerUsageRecord.value, __loadBalancerUsageRecord.set, None, None)


    _ElementMap = {
        __link.name() : __link,
        __loadBalancerUsageRecord.name() : __loadBalancerUsageRecord
    }
    _AttributeMap = {
        
    }



# Complex type zeusEvent_ with content type EMPTY
class zeusEvent_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'zeusEvent')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute paramLine uses Python identifier paramLine
    __paramLine = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'paramLine'), 'paramLine', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_zeusEvent__paramLine', pyxb.binding.datatypes.string)
    
    paramLine = property(__paramLine.value, __paramLine.set, None, None)

    
    # Attribute eventType uses Python identifier eventType
    __eventType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'eventType'), 'eventType', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_zeusEvent__eventType', pyxb.binding.datatypes.string)
    
    eventType = property(__eventType.value, __eventType.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __paramLine.name() : __paramLine,
        __eventType.name() : __eventType
    }
Namespace.addCategoryObject('typeBinding', u'zeusEvent', zeusEvent_)


# Complex type host_ with content type EMPTY
class host_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'host')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute coreDeviceId uses Python identifier coreDeviceId
    __coreDeviceId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'coreDeviceId'), 'coreDeviceId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__coreDeviceId', pyxb.binding.datatypes.string)
    
    coreDeviceId = property(__coreDeviceId.value, __coreDeviceId.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute ipv6Servicenet uses Python identifier ipv6Servicenet
    __ipv6Servicenet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipv6Servicenet'), 'ipv6Servicenet', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__ipv6Servicenet', pyxb.binding.datatypes.string)
    
    ipv6Servicenet = property(__ipv6Servicenet.value, __ipv6Servicenet.set, None, None)

    
    # Attribute managementSoapInterface uses Python identifier managementSoapInterface
    __managementSoapInterface = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'managementSoapInterface'), 'managementSoapInterface', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__managementSoapInterface', pyxb.binding.datatypes.string)
    
    managementSoapInterface = property(__managementSoapInterface.value, __managementSoapInterface.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute zone uses Python identifier zone
    __zone = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'zone'), 'zone', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__zone', zone)
    
    zone = property(__zone.value, __zone.set, None, None)

    
    # Attribute maxConcurrentConnections uses Python identifier maxConcurrentConnections
    __maxConcurrentConnections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'maxConcurrentConnections'), 'maxConcurrentConnections', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__maxConcurrentConnections', pyxb.binding.datatypes.int)
    
    maxConcurrentConnections = property(__maxConcurrentConnections.value, __maxConcurrentConnections.set, None, None)

    
    # Attribute utilization uses Python identifier utilization
    __utilization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'utilization'), 'utilization', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__utilization', pyxb.binding.datatypes.string)
    
    utilization = property(__utilization.value, __utilization.set, None, None)

    
    # Attribute ipv4Servicenet uses Python identifier ipv4Servicenet
    __ipv4Servicenet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipv4Servicenet'), 'ipv4Servicenet', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__ipv4Servicenet', pyxb.binding.datatypes.string)
    
    ipv4Servicenet = property(__ipv4Servicenet.value, __ipv4Servicenet.set, None, None)

    
    # Attribute managementIp uses Python identifier managementIp
    __managementIp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'managementIp'), 'managementIp', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__managementIp', pyxb.binding.datatypes.string)
    
    managementIp = property(__managementIp.value, __managementIp.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__status', hostStatus)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute ipv4Public uses Python identifier ipv4Public
    __ipv4Public = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipv4Public'), 'ipv4Public', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__ipv4Public', pyxb.binding.datatypes.string)
    
    ipv4Public = property(__ipv4Public.value, __ipv4Public.set, None, None)

    
    # Attribute clusterId uses Python identifier clusterId
    __clusterId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'clusterId'), 'clusterId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__clusterId', pyxb.binding.datatypes.int)
    
    clusterId = property(__clusterId.value, __clusterId.set, None, None)

    
    # Attribute numberOfLoadBalancingConfigurations uses Python identifier numberOfLoadBalancingConfigurations
    __numberOfLoadBalancingConfigurations = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numberOfLoadBalancingConfigurations'), 'numberOfLoadBalancingConfigurations', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__numberOfLoadBalancingConfigurations', pyxb.binding.datatypes.int)
    
    numberOfLoadBalancingConfigurations = property(__numberOfLoadBalancingConfigurations.value, __numberOfLoadBalancingConfigurations.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__type', hostType)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute soapEndpointActive uses Python identifier soapEndpointActive
    __soapEndpointActive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'soapEndpointActive'), 'soapEndpointActive', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__soapEndpointActive', pyxb.binding.datatypes.boolean)
    
    soapEndpointActive = property(__soapEndpointActive.value, __soapEndpointActive.set, None, None)

    
    # Attribute numberOfUniqueCustomers uses Python identifier numberOfUniqueCustomers
    __numberOfUniqueCustomers = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numberOfUniqueCustomers'), 'numberOfUniqueCustomers', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__numberOfUniqueCustomers', pyxb.binding.datatypes.int)
    
    numberOfUniqueCustomers = property(__numberOfUniqueCustomers.value, __numberOfUniqueCustomers.set, None, None)

    
    # Attribute ipv6Public uses Python identifier ipv6Public
    __ipv6Public = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipv6Public'), 'ipv6Public', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__ipv6Public', pyxb.binding.datatypes.string)
    
    ipv6Public = property(__ipv6Public.value, __ipv6Public.set, None, None)

    
    # Attribute trafficManagerName uses Python identifier trafficManagerName
    __trafficManagerName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'trafficManagerName'), 'trafficManagerName', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_host__trafficManagerName', pyxb.binding.datatypes.string)
    
    trafficManagerName = property(__trafficManagerName.value, __trafficManagerName.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __coreDeviceId.name() : __coreDeviceId,
        __id.name() : __id,
        __ipv6Servicenet.name() : __ipv6Servicenet,
        __managementSoapInterface.name() : __managementSoapInterface,
        __name.name() : __name,
        __zone.name() : __zone,
        __maxConcurrentConnections.name() : __maxConcurrentConnections,
        __utilization.name() : __utilization,
        __ipv4Servicenet.name() : __ipv4Servicenet,
        __managementIp.name() : __managementIp,
        __status.name() : __status,
        __ipv4Public.name() : __ipv4Public,
        __clusterId.name() : __clusterId,
        __numberOfLoadBalancingConfigurations.name() : __numberOfLoadBalancingConfigurations,
        __type.name() : __type,
        __soapEndpointActive.name() : __soapEndpointActive,
        __numberOfUniqueCustomers.name() : __numberOfUniqueCustomers,
        __ipv6Public.name() : __ipv6Public,
        __trafficManagerName.name() : __trafficManagerName
    }
Namespace.addCategoryObject('typeBinding', u'host', host_)


# Complex type clusters_ with content type ELEMENT_ONLY
class clusters_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'clusters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}cluster uses Python identifier cluster
    __cluster = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cluster'), 'cluster', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_clusters__httpdocs_openstack_orgloadbalancersapimanagementv1_0cluster', True)

    
    cluster = property(__cluster.value, __cluster.set, None, None)


    _ElementMap = {
        __cluster.name() : __cluster
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'clusters', clusters_)


# Complex type cidrTest_ with content type ELEMENT_ONLY
class cidrTest_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cidrTest')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}cidrBlock uses Python identifier cidrBlock
    __cidrBlock = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cidrBlock'), 'cidrBlock', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cidrTest__httpdocs_openstack_orgloadbalancersapimanagementv1_0cidrBlock', True)

    
    cidrBlock = property(__cidrBlock.value, __cidrBlock.set, None, None)

    
    # Attribute ipVersion uses Python identifier ipVersion
    __ipVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipVersion'), 'ipVersion', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cidrTest__ipVersion', lbaas.ipVersion)
    
    ipVersion = property(__ipVersion.value, __ipVersion.set, None, None)

    
    # Attribute ipAddress uses Python identifier ipAddress
    __ipAddress = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipAddress'), 'ipAddress', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_cidrTest__ipAddress', pyxb.binding.datatypes.string)
    
    ipAddress = property(__ipAddress.value, __ipAddress.set, None, None)


    _ElementMap = {
        __cidrBlock.name() : __cidrBlock
    }
    _AttributeMap = {
        __ipVersion.name() : __ipVersion,
        __ipAddress.name() : __ipAddress
    }
Namespace.addCategoryObject('typeBinding', u'cidrTest', cidrTest_)


# Complex type hostUsageRecords_ with content type ELEMENT_ONLY
class hostUsageRecords_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hostUsageRecords')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}hostUsageRecord uses Python identifier hostUsageRecord
    __hostUsageRecord = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hostUsageRecord'), 'hostUsageRecord', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostUsageRecords__httpdocs_openstack_orgloadbalancersapimanagementv1_0hostUsageRecord', True)

    
    hostUsageRecord = property(__hostUsageRecord.value, __hostUsageRecord.set, None, None)


    _ElementMap = {
        __hostUsageRecord.name() : __hostUsageRecord
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'hostUsageRecords', hostUsageRecords_)


# Complex type healthChecks_ with content type ELEMENT_ONLY
class healthChecks_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'healthChecks')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}healthCheck uses Python identifier healthCheck
    __healthCheck = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'healthCheck'), 'healthCheck', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_healthChecks__httpdocs_openstack_orgloadbalancersapimanagementv1_0healthCheck', True)

    
    healthCheck = property(__healthCheck.value, __healthCheck.set, None, None)


    _ElementMap = {
        __healthCheck.name() : __healthCheck
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'healthChecks', healthChecks_)


# Complex type accountLoadBalancers_ with content type ELEMENT_ONLY
class accountLoadBalancers_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountLoadBalancers')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}accountLoadBalancer uses Python identifier accountLoadBalancer
    __accountLoadBalancer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountLoadBalancer'), 'accountLoadBalancer', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountLoadBalancers__httpdocs_openstack_orgloadbalancersapimanagementv1_0accountLoadBalancer', True)

    
    accountLoadBalancer = property(__accountLoadBalancer.value, __accountLoadBalancer.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountLoadBalancers__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)


    _ElementMap = {
        __accountLoadBalancer.name() : __accountLoadBalancer
    }
    _AttributeMap = {
        __accountId.name() : __accountId
    }
Namespace.addCategoryObject('typeBinding', u'accountLoadBalancers', accountLoadBalancers_)


# Complex type loadBalancerLimitGroup_ with content type ELEMENT_ONLY
class loadBalancerLimitGroup_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancerLimitGroup')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}accounts uses Python identifier accounts
    __accounts = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accounts'), 'accounts', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerLimitGroup__httpdocs_openstack_orgloadbalancersapimanagementv1_0accounts', False)

    
    accounts = property(__accounts.value, __accounts.set, None, None)

    
    # Attribute isDefault uses Python identifier isDefault
    __isDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'isDefault'), 'isDefault', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerLimitGroup__isDefault', pyxb.binding.datatypes.boolean)
    
    isDefault = property(__isDefault.value, __isDefault.set, None, None)

    
    # Attribute limit uses Python identifier limit
    __limit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limit'), 'limit', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerLimitGroup__limit', pyxb.binding.datatypes.int)
    
    limit = property(__limit.value, __limit.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerLimitGroup__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerLimitGroup__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)


    _ElementMap = {
        __accounts.name() : __accounts
    }
    _AttributeMap = {
        __isDefault.name() : __isDefault,
        __limit.name() : __limit,
        __name.name() : __name,
        __id.name() : __id
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancerLimitGroup', loadBalancerLimitGroup_)


# Complex type loadBalancersStatusHistory_ with content type ELEMENT_ONLY
class loadBalancersStatusHistory_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancersStatusHistory')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}loadBalancerStatusHistory uses Python identifier loadBalancerStatusHistory
    __loadBalancerStatusHistory = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerStatusHistory'), 'loadBalancerStatusHistory', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancersStatusHistory__httpdocs_openstack_orgloadbalancersapimanagementv1_0loadBalancerStatusHistory', True)

    
    loadBalancerStatusHistory = property(__loadBalancerStatusHistory.value, __loadBalancerStatusHistory.set, None, None)


    _ElementMap = {
        __loadBalancerStatusHistory.name() : __loadBalancerStatusHistory
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancersStatusHistory', loadBalancersStatusHistory_)


# Complex type hostUsageRecord_ with content type ELEMENT_ONLY
class hostUsageRecord_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hostUsageRecord')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}hostUsages uses Python identifier hostUsages
    __hostUsages = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hostUsages'), 'hostUsages', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostUsageRecord__httpdocs_openstack_orgloadbalancersapimanagementv1_0hostUsages', False)

    
    hostUsages = property(__hostUsages.value, __hostUsages.set, None, None)

    
    # Attribute hostId uses Python identifier hostId
    __hostId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'hostId'), 'hostId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostUsageRecord__hostId', pyxb.binding.datatypes.int)
    
    hostId = property(__hostId.value, __hostId.set, None, None)


    _ElementMap = {
        __hostUsages.name() : __hostUsages
    }
    _AttributeMap = {
        __hostId.name() : __hostId
    }
Namespace.addCategoryObject('typeBinding', u'hostUsageRecord', hostUsageRecord_)


# Complex type hosts_ with content type ELEMENT_ONLY
class hosts_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hosts')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}host uses Python identifier host
    __host = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'host'), 'host', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hosts__httpdocs_openstack_orgloadbalancersapimanagementv1_0host', True)

    
    host = property(__host.value, __host.set, None, None)

    
    # Attribute sticky uses Python identifier sticky
    __sticky = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'sticky'), 'sticky', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hosts__sticky', pyxb.binding.datatypes.boolean)
    
    sticky = property(__sticky.value, __sticky.set, None, None)


    _ElementMap = {
        __host.name() : __host
    }
    _AttributeMap = {
        __sticky.name() : __sticky
    }
Namespace.addCategoryObject('typeBinding', u'hosts', hosts_)


# Complex type groupRateLimit_ with content type EMPTY
class groupRateLimit_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'groupRateLimit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute isDefault uses Python identifier isDefault
    __isDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'isDefault'), 'isDefault', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_groupRateLimit__isDefault', pyxb.binding.datatypes.boolean)
    
    isDefault = property(__isDefault.value, __isDefault.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_groupRateLimit__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_groupRateLimit__description', pyxb.binding.datatypes.string)
    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_groupRateLimit__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __isDefault.name() : __isDefault,
        __name.name() : __name,
        __description.name() : __description,
        __id.name() : __id
    }
Namespace.addCategoryObject('typeBinding', u'groupRateLimit', groupRateLimit_)


# Complex type backup_ with content type EMPTY
class backup_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'backup')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute backupTime uses Python identifier backupTime
    __backupTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'backupTime'), 'backupTime', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_backup__backupTime', pyxb.binding.datatypes.dateTime)
    
    backupTime = property(__backupTime.value, __backupTime.set, None, None)

    
    # Attribute hostId uses Python identifier hostId
    __hostId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'hostId'), 'hostId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_backup__hostId', pyxb.binding.datatypes.int)
    
    hostId = property(__hostId.value, __hostId.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_backup__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_backup__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __backupTime.name() : __backupTime,
        __hostId.name() : __hostId,
        __name.name() : __name,
        __id.name() : __id
    }
Namespace.addCategoryObject('typeBinding', u'backup', backup_)


# Complex type accountInHost_ with content type EMPTY
class accountInHost_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountInHost')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute hostId uses Python identifier hostId
    __hostId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'hostId'), 'hostId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountInHost__hostId', pyxb.binding.datatypes.int)
    
    hostId = property(__hostId.value, __hostId.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountInHost__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)

    
    # Attribute loadBalancerCount uses Python identifier loadBalancerCount
    __loadBalancerCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadBalancerCount'), 'loadBalancerCount', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountInHost__loadBalancerCount', pyxb.binding.datatypes.long)
    
    loadBalancerCount = property(__loadBalancerCount.value, __loadBalancerCount.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __hostId.name() : __hostId,
        __accountId.name() : __accountId,
        __loadBalancerCount.name() : __loadBalancerCount
    }
Namespace.addCategoryObject('typeBinding', u'accountInHost', accountInHost_)


# Complex type customerList_ with content type ELEMENT_ONLY
class customerList_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customerList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}customers uses Python identifier customers
    __customers = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customers'), 'customers', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_customerList__httpdocs_openstack_orgloadbalancersapimanagementv1_0customers', False)

    
    customers = property(__customers.value, __customers.set, None, None)


    _ElementMap = {
        __customers.name() : __customers
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'customerList', customerList_)


# Complex type ldapInfo_ with content type ELEMENT_ONLY
class ldapInfo_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ldapInfo')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}userRole uses Python identifier userRole
    __userRole = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'userRole'), 'userRole', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_ldapInfo__httpdocs_openstack_orgloadbalancersapimanagementv1_0userRole', True)

    
    userRole = property(__userRole.value, __userRole.set, None, None)

    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}ldapGroup uses Python identifier ldapGroup
    __ldapGroup = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ldapGroup'), 'ldapGroup', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_ldapInfo__httpdocs_openstack_orgloadbalancersapimanagementv1_0ldapGroup', True)

    
    ldapGroup = property(__ldapGroup.value, __ldapGroup.set, None, None)

    
    # Attribute userName uses Python identifier userName
    __userName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'userName'), 'userName', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_ldapInfo__userName', pyxb.binding.datatypes.string)
    
    userName = property(__userName.value, __userName.set, None, None)


    _ElementMap = {
        __userRole.name() : __userRole,
        __ldapGroup.name() : __ldapGroup
    }
    _AttributeMap = {
        __userName.name() : __userName
    }
Namespace.addCategoryObject('typeBinding', u'ldapInfo', ldapInfo_)


# Complex type blacklist_ with content type ELEMENT_ONLY
class blacklist_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'blacklist')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}blacklistItem uses Python identifier blacklistItem
    __blacklistItem = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'blacklistItem'), 'blacklistItem', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_blacklist__httpdocs_openstack_orgloadbalancersapimanagementv1_0blacklistItem', True)

    
    blacklistItem = property(__blacklistItem.value, __blacklistItem.set, None, None)


    _ElementMap = {
        __blacklistItem.name() : __blacklistItem
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'blacklist', blacklist_)


# Complex type accountGroup_ with content type ELEMENT_ONLY
class accountGroup_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountGroup')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'group'), 'group', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountGroup__httpdocs_openstack_orgloadbalancersapimanagementv1_0group', False)

    
    group = property(__group.value, __group.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountGroup__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountGroup__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)


    _ElementMap = {
        __group.name() : __group
    }
    _AttributeMap = {
        __id.name() : __id,
        __accountId.name() : __accountId
    }
Namespace.addCategoryObject('typeBinding', u'accountGroup', accountGroup_)


# Complex type customLimitAccounts_ with content type ELEMENT_ONLY
class customLimitAccounts_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customLimitAccounts')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}customLimitAccount uses Python identifier customLimitAccount
    __customLimitAccount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customLimitAccount'), 'customLimitAccount', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_customLimitAccounts__httpdocs_openstack_orgloadbalancersapimanagementv1_0customLimitAccount', True)

    
    customLimitAccount = property(__customLimitAccount.value, __customLimitAccount.set, None, None)


    _ElementMap = {
        __customLimitAccount.name() : __customLimitAccount
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'customLimitAccounts', customLimitAccounts_)


# Complex type accountBillings_ with content type ELEMENT_ONLY
class accountBillings_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountBillings')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/v1.0}accountBilling uses Python identifier accountBilling
    __accountBilling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'accountBilling'), 'accountBilling', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_accountBillings__httpdocs_openstack_orgloadbalancersapiv1_0accountBilling', True)

    
    accountBilling = property(__accountBilling.value, __accountBilling.set, None, None)


    _ElementMap = {
        __accountBilling.name() : __accountBilling
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'accountBillings', accountBillings_)


# Complex type loadBalancerAudits_ with content type ELEMENT_ONLY
class loadBalancerAudits_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loadBalancerAudits')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}loadBalancerAudit uses Python identifier loadBalancerAudit
    __loadBalancerAudit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerAudit'), 'loadBalancerAudit', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_loadBalancerAudits__httpdocs_openstack_orgloadbalancersapimanagementv1_0loadBalancerAudit', True)

    
    loadBalancerAudit = property(__loadBalancerAudit.value, __loadBalancerAudit.set, None, None)


    _ElementMap = {
        __loadBalancerAudit.name() : __loadBalancerAudit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'loadBalancerAudits', loadBalancerAudits_)


# Complex type customers_ with content type ELEMENT_ONLY
class customers_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customers')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}customer uses Python identifier customer
    __customer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customer'), 'customer', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_customers__httpdocs_openstack_orgloadbalancersapimanagementv1_0customer', True)

    
    customer = property(__customer.value, __customer.set, None, None)


    _ElementMap = {
        __customer.name() : __customer
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'customers', customers_)


# Complex type hostUsageList_ with content type ELEMENT_ONLY
class hostUsageList_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hostUsageList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}hostUsageRecords uses Python identifier hostUsageRecords
    __hostUsageRecords = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hostUsageRecords'), 'hostUsageRecords', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostUsageList__httpdocs_openstack_orgloadbalancersapimanagementv1_0hostUsageRecords', False)

    
    hostUsageRecords = property(__hostUsageRecords.value, __hostUsageRecords.set, None, None)


    _ElementMap = {
        __hostUsageRecords.name() : __hostUsageRecords
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'hostUsageList', hostUsageList_)


# Complex type customer_ with content type ELEMENT_ONLY
class customer_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}loadBalancers uses Python identifier loadBalancers
    __loadBalancers = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loadBalancers'), 'loadBalancers', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_customer__httpdocs_openstack_orgloadbalancersapimanagementv1_0loadBalancers', False)

    
    loadBalancers = property(__loadBalancers.value, __loadBalancers.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_customer__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)


    _ElementMap = {
        __loadBalancers.name() : __loadBalancers
    }
    _AttributeMap = {
        __accountId.name() : __accountId
    }
Namespace.addCategoryObject('typeBinding', u'customer', customer_)


# Complex type listOfInts_ with content type ELEMENT_ONLY
class listOfInts_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfInts')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}ints uses Python identifier ints
    __ints = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ints'), 'ints', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_listOfInts__httpdocs_openstack_orgloadbalancersapimanagementv1_0ints', True)

    
    ints = property(__ints.value, __ints.set, None, None)


    _ElementMap = {
        __ints.name() : __ints
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'listOfInts', listOfInts_)


# Complex type hostCapacityReports_ with content type ELEMENT_ONLY
class hostCapacityReports_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hostCapacityReports')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}hostCapacityReport uses Python identifier hostCapacityReport
    __hostCapacityReport = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hostCapacityReport'), 'hostCapacityReport', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostCapacityReports__httpdocs_openstack_orgloadbalancersapimanagementv1_0hostCapacityReport', True)

    
    hostCapacityReport = property(__hostCapacityReport.value, __hostCapacityReport.set, None, None)


    _ElementMap = {
        __hostCapacityReport.name() : __hostCapacityReport
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'hostCapacityReports', hostCapacityReports_)


# Complex type hostCapacityReport_ with content type EMPTY
class hostCapacityReport_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hostCapacityReport')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute remainingDaysOfCapacity uses Python identifier remainingDaysOfCapacity
    __remainingDaysOfCapacity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'remainingDaysOfCapacity'), 'remainingDaysOfCapacity', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostCapacityReport__remainingDaysOfCapacity', pyxb.binding.datatypes.double)
    
    remainingDaysOfCapacity = property(__remainingDaysOfCapacity.value, __remainingDaysOfCapacity.set, None, None)

    
    # Attribute hostId uses Python identifier hostId
    __hostId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'hostId'), 'hostId', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostCapacityReport__hostId', pyxb.binding.datatypes.int)
    
    hostId = property(__hostId.value, __hostId.set, None, None)

    
    # Attribute allocatedConcurrentConnections uses Python identifier allocatedConcurrentConnections
    __allocatedConcurrentConnections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'allocatedConcurrentConnections'), 'allocatedConcurrentConnections', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostCapacityReport__allocatedConcurrentConnections', pyxb.binding.datatypes.int)
    
    allocatedConcurrentConnections = property(__allocatedConcurrentConnections.value, __allocatedConcurrentConnections.set, None, None)

    
    # Attribute hostName uses Python identifier hostName
    __hostName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'hostName'), 'hostName', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostCapacityReport__hostName', pyxb.binding.datatypes.string)
    
    hostName = property(__hostName.value, __hostName.set, None, None)

    
    # Attribute allocatedConcurrentConnectionsToday uses Python identifier allocatedConcurrentConnectionsToday
    __allocatedConcurrentConnectionsToday = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'allocatedConcurrentConnectionsToday'), 'allocatedConcurrentConnectionsToday', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostCapacityReport__allocatedConcurrentConnectionsToday', pyxb.binding.datatypes.int)
    
    allocatedConcurrentConnectionsToday = property(__allocatedConcurrentConnectionsToday.value, __allocatedConcurrentConnectionsToday.set, None, None)

    
    # Attribute totalConcurrentConnectionCapacity uses Python identifier totalConcurrentConnectionCapacity
    __totalConcurrentConnectionCapacity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'totalConcurrentConnectionCapacity'), 'totalConcurrentConnectionCapacity', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostCapacityReport__totalConcurrentConnectionCapacity', pyxb.binding.datatypes.int)
    
    totalConcurrentConnectionCapacity = property(__totalConcurrentConnectionCapacity.value, __totalConcurrentConnectionCapacity.set, None, None)

    
    # Attribute allocatedConcurrentConnectionsInLastSevenDays uses Python identifier allocatedConcurrentConnectionsInLastSevenDays
    __allocatedConcurrentConnectionsInLastSevenDays = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'allocatedConcurrentConnectionsInLastSevenDays'), 'allocatedConcurrentConnectionsInLastSevenDays', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostCapacityReport__allocatedConcurrentConnectionsInLastSevenDays', pyxb.binding.datatypes.int)
    
    allocatedConcurrentConnectionsInLastSevenDays = property(__allocatedConcurrentConnectionsInLastSevenDays.value, __allocatedConcurrentConnectionsInLastSevenDays.set, None, None)

    
    # Attribute availableConcurrentConnections uses Python identifier availableConcurrentConnections
    __availableConcurrentConnections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'availableConcurrentConnections'), 'availableConcurrentConnections', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostCapacityReport__availableConcurrentConnections', pyxb.binding.datatypes.int)
    
    availableConcurrentConnections = property(__availableConcurrentConnections.value, __availableConcurrentConnections.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __remainingDaysOfCapacity.name() : __remainingDaysOfCapacity,
        __hostId.name() : __hostId,
        __allocatedConcurrentConnections.name() : __allocatedConcurrentConnections,
        __hostName.name() : __hostName,
        __allocatedConcurrentConnectionsToday.name() : __allocatedConcurrentConnectionsToday,
        __totalConcurrentConnectionCapacity.name() : __totalConcurrentConnectionCapacity,
        __allocatedConcurrentConnectionsInLastSevenDays.name() : __allocatedConcurrentConnectionsInLastSevenDays,
        __availableConcurrentConnections.name() : __availableConcurrentConnections
    }
Namespace.addCategoryObject('typeBinding', u'hostCapacityReport', hostCapacityReport_)


# Complex type virtualIpAvailabilityReports_ with content type ELEMENT_ONLY
class virtualIpAvailabilityReports_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualIpAvailabilityReports')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}virtualIpAvailabilityReport uses Python identifier virtualIpAvailabilityReport
    __virtualIpAvailabilityReport = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'virtualIpAvailabilityReport'), 'virtualIpAvailabilityReport', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_virtualIpAvailabilityReports__httpdocs_openstack_orgloadbalancersapimanagementv1_0virtualIpAvailabilityReport', True)

    
    virtualIpAvailabilityReport = property(__virtualIpAvailabilityReport.value, __virtualIpAvailabilityReport.set, None, None)


    _ElementMap = {
        __virtualIpAvailabilityReport.name() : __virtualIpAvailabilityReport
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'virtualIpAvailabilityReports', virtualIpAvailabilityReports_)


# Complex type ports_ with content type ELEMENT_ONLY
class ports_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ports')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/loadbalancers/api/management/v1.0}port uses Python identifier port
    __port = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'port'), 'port', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_ports__httpdocs_openstack_orgloadbalancersapimanagementv1_0port', True)

    
    port = property(__port.value, __port.set, None, None)


    _ElementMap = {
        __port.name() : __port
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ports', ports_)


# Complex type hostUsage_ with content type EMPTY
class hostUsage_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hostUsage')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute bandwidthOut uses Python identifier bandwidthOut
    __bandwidthOut = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'bandwidthOut'), 'bandwidthOut', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostUsage__bandwidthOut', pyxb.binding.datatypes.long)
    
    bandwidthOut = property(__bandwidthOut.value, __bandwidthOut.set, None, None)

    
    # Attribute bandwidthIn uses Python identifier bandwidthIn
    __bandwidthIn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'bandwidthIn'), 'bandwidthIn', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostUsage__bandwidthIn', pyxb.binding.datatypes.long)
    
    bandwidthIn = property(__bandwidthIn.value, __bandwidthIn.set, None, None)

    
    # Attribute day uses Python identifier day
    __day = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'day'), 'day', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_hostUsage__day', pyxb.binding.datatypes.date)
    
    day = property(__day.value, __day.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __bandwidthOut.name() : __bandwidthOut,
        __bandwidthIn.name() : __bandwidthIn,
        __day.name() : __day
    }
Namespace.addCategoryObject('typeBinding', u'hostUsage', hostUsage_)


# Complex type capacityPlanningVirtualIpBlocks with content type EMPTY
class capacityPlanningVirtualIpBlocks (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'capacityPlanningVirtualIpBlocks')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute configuredServiceNet uses Python identifier configuredServiceNet
    __configuredServiceNet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'configuredServiceNet'), 'configuredServiceNet', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_capacityPlanningVirtualIpBlocks_configuredServiceNet', pyxb.binding.datatypes.long)
    
    configuredServiceNet = property(__configuredServiceNet.value, __configuredServiceNet.set, None, None)

    
    # Attribute receltyAllocatedServiceNet uses Python identifier receltyAllocatedServiceNet
    __receltyAllocatedServiceNet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'receltyAllocatedServiceNet'), 'receltyAllocatedServiceNet', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_capacityPlanningVirtualIpBlocks_receltyAllocatedServiceNet', pyxb.binding.datatypes.long)
    
    receltyAllocatedServiceNet = property(__receltyAllocatedServiceNet.value, __receltyAllocatedServiceNet.set, None, None)

    
    # Attribute deallocatedServiceNet uses Python identifier deallocatedServiceNet
    __deallocatedServiceNet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'deallocatedServiceNet'), 'deallocatedServiceNet', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_capacityPlanningVirtualIpBlocks_deallocatedServiceNet', pyxb.binding.datatypes.long)
    
    deallocatedServiceNet = property(__deallocatedServiceNet.value, __deallocatedServiceNet.set, None, None)

    
    # Attribute freeIP uses Python identifier freeIP
    __freeIP = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'freeIP'), 'freeIP', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_capacityPlanningVirtualIpBlocks_freeIP', pyxb.binding.datatypes.long)
    
    freeIP = property(__freeIP.value, __freeIP.set, None, None)

    
    # Attribute freeServiceNet uses Python identifier freeServiceNet
    __freeServiceNet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'freeServiceNet'), 'freeServiceNet', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_capacityPlanningVirtualIpBlocks_freeServiceNet', pyxb.binding.datatypes.long)
    
    freeServiceNet = property(__freeServiceNet.value, __freeServiceNet.set, None, None)

    
    # Attribute ipdaysavailable uses Python identifier ipdaysavailable
    __ipdaysavailable = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ipdaysavailable'), 'ipdaysavailable', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_capacityPlanningVirtualIpBlocks_ipdaysavailable', pyxb.binding.datatypes.long)
    
    ipdaysavailable = property(__ipdaysavailable.value, __ipdaysavailable.set, None, None)

    
    # Attribute allocatedServiceNet uses Python identifier allocatedServiceNet
    __allocatedServiceNet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'allocatedServiceNet'), 'allocatedServiceNet', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_capacityPlanningVirtualIpBlocks_allocatedServiceNet', pyxb.binding.datatypes.long)
    
    allocatedServiceNet = property(__allocatedServiceNet.value, __allocatedServiceNet.set, None, None)

    
    # Attribute serviceNetdaysavailable uses Python identifier serviceNetdaysavailable
    __serviceNetdaysavailable = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'serviceNetdaysavailable'), 'serviceNetdaysavailable', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_capacityPlanningVirtualIpBlocks_serviceNetdaysavailable', pyxb.binding.datatypes.long)
    
    serviceNetdaysavailable = property(__serviceNetdaysavailable.value, __serviceNetdaysavailable.set, None, None)

    
    # Attribute recentlyAllocatedIP uses Python identifier recentlyAllocatedIP
    __recentlyAllocatedIP = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'recentlyAllocatedIP'), 'recentlyAllocatedIP', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_capacityPlanningVirtualIpBlocks_recentlyAllocatedIP', pyxb.binding.datatypes.long)
    
    recentlyAllocatedIP = property(__recentlyAllocatedIP.value, __recentlyAllocatedIP.set, None, None)

    
    # Attribute configuredIP uses Python identifier configuredIP
    __configuredIP = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'configuredIP'), 'configuredIP', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_capacityPlanningVirtualIpBlocks_configuredIP', pyxb.binding.datatypes.long)
    
    configuredIP = property(__configuredIP.value, __configuredIP.set, None, None)

    
    # Attribute deallocatiedIP uses Python identifier deallocatiedIP
    __deallocatiedIP = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'deallocatiedIP'), 'deallocatiedIP', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_capacityPlanningVirtualIpBlocks_deallocatiedIP', pyxb.binding.datatypes.long)
    
    deallocatiedIP = property(__deallocatiedIP.value, __deallocatiedIP.set, None, None)

    
    # Attribute allocatedIP uses Python identifier allocatedIP
    __allocatedIP = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'allocatedIP'), 'allocatedIP', '__httpdocs_openstack_orgloadbalancersapimanagementv1_0_capacityPlanningVirtualIpBlocks_allocatedIP', pyxb.binding.datatypes.long)
    
    allocatedIP = property(__allocatedIP.value, __allocatedIP.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __configuredServiceNet.name() : __configuredServiceNet,
        __receltyAllocatedServiceNet.name() : __receltyAllocatedServiceNet,
        __deallocatedServiceNet.name() : __deallocatedServiceNet,
        __freeIP.name() : __freeIP,
        __freeServiceNet.name() : __freeServiceNet,
        __ipdaysavailable.name() : __ipdaysavailable,
        __allocatedServiceNet.name() : __allocatedServiceNet,
        __serviceNetdaysavailable.name() : __serviceNetdaysavailable,
        __recentlyAllocatedIP.name() : __recentlyAllocatedIP,
        __configuredIP.name() : __configuredIP,
        __deallocatiedIP.name() : __deallocatiedIP,
        __allocatedIP.name() : __allocatedIP
    }
Namespace.addCategoryObject('typeBinding', u'capacityPlanningVirtualIpBlocks', capacityPlanningVirtualIpBlocks)


port = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'port'), port_)
Namespace.addCategoryObject('elementBinding', port.name().localName(), port)

jobs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'jobs'), jobs_)
Namespace.addCategoryObject('elementBinding', jobs.name().localName(), jobs)

accountLoadBalancerServiceEvents = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountLoadBalancerServiceEvents'), accountLoadBalancerServiceEvents_)
Namespace.addCategoryObject('elementBinding', accountLoadBalancerServiceEvents.name().localName(), accountLoadBalancerServiceEvents)

virtualIpAvailabilityReport = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIpAvailabilityReport'), virtualIpAvailabilityReport_)
Namespace.addCategoryObject('elementBinding', virtualIpAvailabilityReport.name().localName(), virtualIpAvailabilityReport)

hostssubnet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostssubnet'), hostssubnet_)
Namespace.addCategoryObject('elementBinding', hostssubnet.name().localName(), hostssubnet)

blacklistItem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'blacklistItem'), blacklistItem_)
Namespace.addCategoryObject('elementBinding', blacklistItem.name().localName(), blacklistItem)

job = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'job'), job_)
Namespace.addCategoryObject('elementBinding', job.name().localName(), job)

ldapGroup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ldapGroup'), ldapGroup_)
Namespace.addCategoryObject('elementBinding', ldapGroup.name().localName(), ldapGroup)

alerts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alerts'), alerts_)
Namespace.addCategoryObject('elementBinding', alerts.name().localName(), alerts)

hostsubnet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostsubnet'), hostsubnet_)
Namespace.addCategoryObject('elementBinding', hostsubnet.name().localName(), hostsubnet)

netInterface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netInterface'), netInterface_)
Namespace.addCategoryObject('elementBinding', netInterface.name().localName(), netInterface)

clusterDetails = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'clusterDetails'), clusterDetails_)
Namespace.addCategoryObject('elementBinding', clusterDetails.name().localName(), clusterDetails)

accountsInCluster = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountsInCluster'), accountsInCluster_)
Namespace.addCategoryObject('elementBinding', accountsInCluster.name().localName(), accountsInCluster)

loadBalancers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancers'), loadBalancers_)
Namespace.addCategoryObject('elementBinding', loadBalancers.name().localName(), loadBalancers)

groupRateLimits = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'groupRateLimits'), groupRateLimits_)
Namespace.addCategoryObject('elementBinding', groupRateLimits.name().localName(), groupRateLimits)

zeusRateLimitedLoadBalancers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zeusRateLimitedLoadBalancers'), zeusRateLimitedLoadBalancers_)
Namespace.addCategoryObject('elementBinding', zeusRateLimitedLoadBalancers.name().localName(), zeusRateLimitedLoadBalancers)

account = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'account'), account_)
Namespace.addCategoryObject('elementBinding', account.name().localName(), account)

healthCheck = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'healthCheck'), healthCheck_)
Namespace.addCategoryObject('elementBinding', healthCheck.name().localName(), healthCheck)

cidr = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cidr'), cidr_)
Namespace.addCategoryObject('elementBinding', cidr.name().localName(), cidr)

allAbsoluteLimits = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'allAbsoluteLimits'), allAbsoluteLimits_)
Namespace.addCategoryObject('elementBinding', allAbsoluteLimits.name().localName(), allAbsoluteLimits)

alert = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alert'), alert_)
Namespace.addCategoryObject('elementBinding', alert.name().localName(), alert)

zeusRateLimitedLoadBalancer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zeusRateLimitedLoadBalancer'), zeusRateLimitedLoadBalancer_)
Namespace.addCategoryObject('elementBinding', zeusRateLimitedLoadBalancer.name().localName(), zeusRateLimitedLoadBalancer)

backups = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'backups'), backups_)
Namespace.addCategoryObject('elementBinding', backups.name().localName(), backups)

accountsInHost = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountsInHost'), accountsInHost_)
Namespace.addCategoryObject('elementBinding', accountsInHost.name().localName(), accountsInHost)

loadBalancer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancer'), loadBalancer_)
Namespace.addCategoryObject('elementBinding', loadBalancer.name().localName(), loadBalancer)

loadBalancerEvent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerEvent'), loadBalancerEvent_)
Namespace.addCategoryObject('elementBinding', loadBalancerEvent.name().localName(), loadBalancerEvent)

virtualIpBlock = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIpBlock'), virtualIpBlock_)
Namespace.addCategoryObject('elementBinding', virtualIpBlock.name().localName(), virtualIpBlock)

accounts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accounts'), accounts_)
Namespace.addCategoryObject('elementBinding', accounts.name().localName(), accounts)

accountLoadBalancer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountLoadBalancer'), accountLoadBalancer_)
Namespace.addCategoryObject('elementBinding', accountLoadBalancer.name().localName(), accountLoadBalancer)

rateLimit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rateLimit'), rateLimit_)
Namespace.addCategoryObject('elementBinding', rateLimit.name().localName(), rateLimit)

accountInCluster = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountInCluster'), accountInCluster_)
Namespace.addCategoryObject('elementBinding', accountInCluster.name().localName(), accountInCluster)

userRole = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'userRole'), userRole_)
Namespace.addCategoryObject('elementBinding', userRole.name().localName(), userRole)

DefaultLimits = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DefaultLimits'), DefaultLimits_)
Namespace.addCategoryObject('elementBinding', DefaultLimits.name().localName(), DefaultLimits)

loadBalancerAudit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerAudit'), loadBalancerAudit_)
Namespace.addCategoryObject('elementBinding', loadBalancerAudit.name().localName(), loadBalancerAudit)

loadBalancerLimitGroups = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerLimitGroups'), loadBalancerLimitGroups_)
Namespace.addCategoryObject('elementBinding', loadBalancerLimitGroups.name().localName(), loadBalancerLimitGroups)

loadBalancerStatusHistory = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerStatusHistory'), loadBalancerStatusHistory_)
Namespace.addCategoryObject('elementBinding', loadBalancerStatusHistory.name().localName(), loadBalancerStatusHistory)

accountUsageRecords = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUsageRecords'), CTD_ANON)
Namespace.addCategoryObject('elementBinding', accountUsageRecords.name().localName(), accountUsageRecords)

accountGroups = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountGroups'), accountGroups_)
Namespace.addCategoryObject('elementBinding', accountGroups.name().localName(), accountGroups)

loadBalancerServiceEvents = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerServiceEvents'), loadBalancerServiceEvents_)
Namespace.addCategoryObject('elementBinding', loadBalancerServiceEvents.name().localName(), loadBalancerServiceEvents)

CustomLimits = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CustomLimits'), CustomLimits_)
Namespace.addCategoryObject('elementBinding', CustomLimits.name().localName(), CustomLimits)

byIdOrName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'byIdOrName'), byIdOrName_)
Namespace.addCategoryObject('elementBinding', byIdOrName.name().localName(), byIdOrName)

virtualIps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIps'), virtualIps_)
Namespace.addCategoryObject('elementBinding', virtualIps.name().localName(), virtualIps)

event = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'event'), event_)
Namespace.addCategoryObject('elementBinding', event.name().localName(), event)

virtualIpBlocks = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIpBlocks'), virtualIpBlocks_)
Namespace.addCategoryObject('elementBinding', virtualIpBlocks.name().localName(), virtualIpBlocks)

loadBalancerUsageRecords = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsageRecords'), CTD_ANON_)
Namespace.addCategoryObject('elementBinding', loadBalancerUsageRecords.name().localName(), loadBalancerUsageRecords)

zeusEvent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zeusEvent'), zeusEvent_)
Namespace.addCategoryObject('elementBinding', zeusEvent.name().localName(), zeusEvent)

customLimitAccount = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customLimitAccount'), customLimitAccount_)
Namespace.addCategoryObject('elementBinding', customLimitAccount.name().localName(), customLimitAccount)

ticket = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ticket'), ticket_)
Namespace.addCategoryObject('elementBinding', ticket.name().localName(), ticket)

host = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'host'), host_)
Namespace.addCategoryObject('elementBinding', host.name().localName(), host)

clusters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'clusters'), clusters_)
Namespace.addCategoryObject('elementBinding', clusters.name().localName(), clusters)

cidrTest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cidrTest'), cidrTest_)
Namespace.addCategoryObject('elementBinding', cidrTest.name().localName(), cidrTest)

hostUsageRecords = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostUsageRecords'), hostUsageRecords_)
Namespace.addCategoryObject('elementBinding', hostUsageRecords.name().localName(), hostUsageRecords)

hostUsages = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostUsages'), hostUsages_)
Namespace.addCategoryObject('elementBinding', hostUsages.name().localName(), hostUsages)

healthChecks = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'healthChecks'), healthChecks_)
Namespace.addCategoryObject('elementBinding', healthChecks.name().localName(), healthChecks)

accountLoadBalancers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountLoadBalancers'), accountLoadBalancers_)
Namespace.addCategoryObject('elementBinding', accountLoadBalancers.name().localName(), accountLoadBalancers)

loadBalancersStatusHistory = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancersStatusHistory'), loadBalancersStatusHistory_)
Namespace.addCategoryObject('elementBinding', loadBalancersStatusHistory.name().localName(), loadBalancersStatusHistory)

accountUsageRecord = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUsageRecord'), accountUsageRecord_)
Namespace.addCategoryObject('elementBinding', accountUsageRecord.name().localName(), accountUsageRecord)

hosts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hosts'), hosts_)
Namespace.addCategoryObject('elementBinding', hosts.name().localName(), hosts)

cluster = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cluster'), cluster_)
Namespace.addCategoryObject('elementBinding', cluster.name().localName(), cluster)

groupRateLimit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'groupRateLimit'), groupRateLimit_)
Namespace.addCategoryObject('elementBinding', groupRateLimit.name().localName(), groupRateLimit)

backup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'backup'), backup_)
Namespace.addCategoryObject('elementBinding', backup.name().localName(), backup)

customerList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerList'), customerList_)
Namespace.addCategoryObject('elementBinding', customerList.name().localName(), customerList)

ldapInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ldapInfo'), ldapInfo_)
Namespace.addCategoryObject('elementBinding', ldapInfo.name().localName(), ldapInfo)

blacklist = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'blacklist'), blacklist_)
Namespace.addCategoryObject('elementBinding', blacklist.name().localName(), blacklist)

loadBalancerServiceEvent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerServiceEvent'), loadBalancerServiceEvent_)
Namespace.addCategoryObject('elementBinding', loadBalancerServiceEvent.name().localName(), loadBalancerServiceEvent)

customLimitAccounts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customLimitAccounts'), customLimitAccounts_)
Namespace.addCategoryObject('elementBinding', customLimitAccounts.name().localName(), customLimitAccounts)

tickets = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tickets'), tickets_)
Namespace.addCategoryObject('elementBinding', tickets.name().localName(), tickets)

accountBillings = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountBillings'), accountBillings_)
Namespace.addCategoryObject('elementBinding', accountBillings.name().localName(), accountBillings)

loadBalancerAudits = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerAudits'), loadBalancerAudits_)
Namespace.addCategoryObject('elementBinding', loadBalancerAudits.name().localName(), loadBalancerAudits)

accountInHost = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountInHost'), accountInHost_)
Namespace.addCategoryObject('elementBinding', accountInHost.name().localName(), accountInHost)

customers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customers'), customers_)
Namespace.addCategoryObject('elementBinding', customers.name().localName(), customers)

hostUsageList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostUsageList'), hostUsageList_)
Namespace.addCategoryObject('elementBinding', hostUsageList.name().localName(), hostUsageList)

accountGroup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountGroup'), accountGroup_)
Namespace.addCategoryObject('elementBinding', accountGroup.name().localName(), accountGroup)

listOfInts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'listOfInts'), listOfInts_)
Namespace.addCategoryObject('elementBinding', listOfInts.name().localName(), listOfInts)

customer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customer'), customer_)
Namespace.addCategoryObject('elementBinding', customer.name().localName(), customer)

loadBalancerLimitGroup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerLimitGroup'), loadBalancerLimitGroup_)
Namespace.addCategoryObject('elementBinding', loadBalancerLimitGroup.name().localName(), loadBalancerLimitGroup)

hostUsageRecord = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostUsageRecord'), hostUsageRecord_)
Namespace.addCategoryObject('elementBinding', hostUsageRecord.name().localName(), hostUsageRecord)

hostCapacityReports = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostCapacityReports'), hostCapacityReports_)
Namespace.addCategoryObject('elementBinding', hostCapacityReports.name().localName(), hostCapacityReports)

hostMachineDetails = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostMachineDetails'), hostMachineDetails_)
Namespace.addCategoryObject('elementBinding', hostMachineDetails.name().localName(), hostMachineDetails)

virtualIp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIp'), virtualIp_)
Namespace.addCategoryObject('elementBinding', virtualIp.name().localName(), virtualIp)

suspension = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'suspension'), suspension_)
Namespace.addCategoryObject('elementBinding', suspension.name().localName(), suspension)

hostCapacityReport = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostCapacityReport'), hostCapacityReport_)
Namespace.addCategoryObject('elementBinding', hostCapacityReport.name().localName(), hostCapacityReport)

virtualIpAvailabilityReports = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIpAvailabilityReports'), virtualIpAvailabilityReports_)
Namespace.addCategoryObject('elementBinding', virtualIpAvailabilityReports.name().localName(), virtualIpAvailabilityReports)

ports = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ports'), ports_)
Namespace.addCategoryObject('elementBinding', ports.name().localName(), ports)

hostUsage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostUsage'), hostUsage_)
Namespace.addCategoryObject('elementBinding', hostUsage.name().localName(), hostUsage)



port_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancers'), loadBalancers_, scope=port_))
port_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(port_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancers')), min_occurs=0L, max_occurs=1)
    )
port_._ContentModel = pyxb.binding.content.ParticleModel(port_._GroupModel, min_occurs=1, max_occurs=1)



jobs_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'job'), job_, scope=jobs_))
jobs_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(jobs_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'job')), min_occurs=1L, max_occurs=None)
    )
jobs_._ContentModel = pyxb.binding.content.ParticleModel(jobs_._GroupModel, min_occurs=1, max_occurs=1)



accountLoadBalancerServiceEvents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerServiceEvents'), loadBalancerServiceEvents_, scope=accountLoadBalancerServiceEvents_))
accountLoadBalancerServiceEvents_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accountLoadBalancerServiceEvents_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerServiceEvents')), min_occurs=1L, max_occurs=None)
    )
accountLoadBalancerServiceEvents_._ContentModel = pyxb.binding.content.ParticleModel(accountLoadBalancerServiceEvents_._GroupModel, min_occurs=1, max_occurs=1)



netInterface_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cidr'), cidr_, scope=netInterface_))
netInterface_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(netInterface_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cidr')), min_occurs=0L, max_occurs=None)
    )
netInterface_._ContentModel = pyxb.binding.content.ParticleModel(netInterface_._GroupModel, min_occurs=1, max_occurs=1)



loadBalancers_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancer'), loadBalancer_, scope=loadBalancers_))
loadBalancers_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancers_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancer')), min_occurs=0L, max_occurs=None)
    )
loadBalancers_._ContentModel = pyxb.binding.content.ParticleModel(loadBalancers_._GroupModel, min_occurs=1, max_occurs=1)



hostssubnet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostsubnet'), hostsubnet_, scope=hostssubnet_))
hostssubnet_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hostssubnet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hostsubnet')), min_occurs=0L, max_occurs=None)
    )
hostssubnet_._ContentModel = pyxb.binding.content.ParticleModel(hostssubnet_._GroupModel, min_occurs=1, max_occurs=1)



alerts_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alert'), alert_, scope=alerts_))
alerts_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(alerts_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'alert')), min_occurs=0L, max_occurs=None)
    )
alerts_._ContentModel = pyxb.binding.content.ParticleModel(alerts_._GroupModel, min_occurs=1, max_occurs=1)



hostsubnet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'netInterface'), netInterface_, scope=hostsubnet_))
hostsubnet_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hostsubnet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'netInterface')), min_occurs=0L, max_occurs=None)
    )
hostsubnet_._ContentModel = pyxb.binding.content.ParticleModel(hostsubnet_._GroupModel, min_occurs=1, max_occurs=1)



virtualIp_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ticket'), ticket_, scope=virtualIp_))
virtualIp_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(virtualIp_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ticket')), min_occurs=1, max_occurs=1)
    )
virtualIp_._ContentModel = pyxb.binding.content.ParticleModel(virtualIp_._GroupModel, min_occurs=1, max_occurs=1)



clusterDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIpBlocks'), capacityPlanningVirtualIpBlocks, scope=clusterDetails_))

clusterDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cluster'), cluster_, scope=clusterDetails_))

clusterDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostMachineDetails'), hostMachineDetails_, scope=clusterDetails_))
clusterDetails_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(clusterDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cluster')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(clusterDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hostMachineDetails')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(clusterDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'virtualIpBlocks')), min_occurs=1, max_occurs=1)
    )
clusterDetails_._ContentModel = pyxb.binding.content.ParticleModel(clusterDetails_._GroupModel, min_occurs=1, max_occurs=1)



accountsInCluster_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountInCluster'), accountInCluster_, scope=accountsInCluster_))
accountsInCluster_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accountsInCluster_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountInCluster')), min_occurs=0L, max_occurs=None)
    )
accountsInCluster_._ContentModel = pyxb.binding.content.ParticleModel(accountsInCluster_._GroupModel, min_occurs=1, max_occurs=1)



groupRateLimits_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'groupRateLimit'), groupRateLimit_, scope=groupRateLimits_))
groupRateLimits_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(groupRateLimits_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'groupRateLimit')), min_occurs=0L, max_occurs=None)
    )
groupRateLimits_._ContentModel = pyxb.binding.content.ParticleModel(groupRateLimits_._GroupModel, min_occurs=1, max_occurs=1)



zeusRateLimitedLoadBalancers_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zeusRateLimitedLoadBalancer'), zeusRateLimitedLoadBalancer_, scope=zeusRateLimitedLoadBalancers_))
zeusRateLimitedLoadBalancers_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(zeusRateLimitedLoadBalancers_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zeusRateLimitedLoadBalancer')), min_occurs=0L, max_occurs=None)
    )
zeusRateLimitedLoadBalancers_._ContentModel = pyxb.binding.content.ParticleModel(zeusRateLimitedLoadBalancers_._GroupModel, min_occurs=1, max_occurs=1)



hostUsages_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostUsage'), hostUsage_, scope=hostUsages_))
hostUsages_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hostUsages_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hostUsage')), min_occurs=1L, max_occurs=None)
    )
hostUsages_._ContentModel = pyxb.binding.content.ParticleModel(hostUsages_._GroupModel, min_occurs=1, max_occurs=1)



suspension_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ticket'), ticket_, scope=suspension_))
suspension_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(suspension_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ticket')), min_occurs=1, max_occurs=1)
    )
suspension_._ContentModel = pyxb.binding.content.ParticleModel(suspension_._GroupModel, min_occurs=1, max_occurs=1)



allAbsoluteLimits_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'defaultLimits'), DefaultLimits_, scope=allAbsoluteLimits_))

allAbsoluteLimits_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customLimits'), CustomLimits_, scope=allAbsoluteLimits_))
allAbsoluteLimits_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(allAbsoluteLimits_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customLimits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(allAbsoluteLimits_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'defaultLimits')), min_occurs=0L, max_occurs=1)
    )
allAbsoluteLimits_._ContentModel = pyxb.binding.content.ParticleModel(allAbsoluteLimits_._GroupModel, min_occurs=1, max_occurs=1)



zeusRateLimitedLoadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tickets'), tickets_, scope=zeusRateLimitedLoadBalancer_))
zeusRateLimitedLoadBalancer_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(zeusRateLimitedLoadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tickets')), min_occurs=1, max_occurs=1)
    )
zeusRateLimitedLoadBalancer_._ContentModel = pyxb.binding.content.ParticleModel(zeusRateLimitedLoadBalancer_._GroupModel, min_occurs=1, max_occurs=1)



backups_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'backup'), backup_, scope=backups_))
backups_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(backups_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'backup')), min_occurs=1L, max_occurs=None)
    )
backups_._ContentModel = pyxb.binding.content.ParticleModel(backups_._GroupModel, min_occurs=1, max_occurs=1)



accountsInHost_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountInHost'), accountInHost_, scope=accountsInHost_))
accountsInHost_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accountsInHost_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountInHost')), min_occurs=0L, max_occurs=None)
    )
accountsInHost_._ContentModel = pyxb.binding.content.ParticleModel(accountsInHost_._GroupModel, min_occurs=1, max_occurs=1)



loadBalancerServiceEvents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerServiceEvent'), loadBalancerServiceEvent_, scope=loadBalancerServiceEvents_))
loadBalancerServiceEvents_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancerServiceEvents_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerServiceEvent')), min_occurs=1L, max_occurs=None)
    )
loadBalancerServiceEvents_._ContentModel = pyxb.binding.content.ParticleModel(loadBalancerServiceEvents_._GroupModel, min_occurs=1, max_occurs=1)



loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'suspension'), suspension_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tickets'), tickets_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rateLimit'), rateLimit_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'host'), host_, scope=loadBalancer_))

loadBalancer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountLoadBalancerServiceEvents'), accountLoadBalancerServiceEvents_, scope=loadBalancer_))
loadBalancer_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'virtualIps')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'nodes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'metadata')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'loadBalancerUsage')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'sessionPersistence')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'healthMonitor')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'connectionThrottle')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'accessList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'cluster')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'created')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'updated')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'connectionLogging')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'contentCaching')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'sourceAddresses')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'sslTermination')), min_occurs=0L, max_occurs=1)
    )
loadBalancer_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'host')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rateLimit')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'suspension')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tickets')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountLoadBalancerServiceEvents')), min_occurs=0L, max_occurs=1)
    )
loadBalancer_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancer_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(loadBalancer_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
loadBalancer_._ContentModel = pyxb.binding.content.ParticleModel(loadBalancer_._GroupModel, min_occurs=1, max_occurs=1)



hostMachineDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'host'), host_, scope=hostMachineDetails_))
hostMachineDetails_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hostMachineDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'host')), min_occurs=0L, max_occurs=1)
    )
hostMachineDetails_._ContentModel = pyxb.binding.content.ParticleModel(hostMachineDetails_._GroupModel, min_occurs=1, max_occurs=1)



accounts_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'account'), account_, scope=accounts_))
accounts_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accounts_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'account')), min_occurs=1L, max_occurs=None)
    )
accounts_._ContentModel = pyxb.binding.content.ParticleModel(accounts_._GroupModel, min_occurs=1, max_occurs=1)



rateLimit_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ticket'), ticket_, scope=rateLimit_))
rateLimit_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rateLimit_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ticket')), min_occurs=1, max_occurs=1)
    )
rateLimit_._ContentModel = pyxb.binding.content.ParticleModel(rateLimit_._GroupModel, min_occurs=1, max_occurs=1)



CustomLimits_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'limit'), lbaas.limit_, scope=CustomLimits_))
CustomLimits_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CustomLimits_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'limit')), min_occurs=1L, max_occurs=None)
    )
CustomLimits_._ContentModel = pyxb.binding.content.ParticleModel(CustomLimits_._GroupModel, min_occurs=1, max_occurs=1)



DefaultLimits_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'limit'), lbaas.limit_, scope=DefaultLimits_))
DefaultLimits_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DefaultLimits_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'limit')), min_occurs=1L, max_occurs=None)
    )
DefaultLimits_._ContentModel = pyxb.binding.content.ParticleModel(DefaultLimits_._GroupModel, min_occurs=1, max_occurs=1)



loadBalancerAudit_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alertAudits'), alerts_, scope=loadBalancerAudit_))
loadBalancerAudit_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancerAudit_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'alertAudits')), min_occurs=0L, max_occurs=None)
    )
loadBalancerAudit_._ContentModel = pyxb.binding.content.ParticleModel(loadBalancerAudit_._GroupModel, min_occurs=1, max_occurs=1)



tickets_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ticket'), ticket_, scope=tickets_))
tickets_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(tickets_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ticket')), min_occurs=1L, max_occurs=None)
    )
tickets_._ContentModel = pyxb.binding.content.ParticleModel(tickets_._GroupModel, min_occurs=1, max_occurs=1)



loadBalancerLimitGroups_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerLimitGroup'), loadBalancerLimitGroup_, scope=loadBalancerLimitGroups_))
loadBalancerLimitGroups_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancerLimitGroups_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerLimitGroup')), min_occurs=1L, max_occurs=None)
    )
loadBalancerLimitGroups_._ContentModel = pyxb.binding.content.ParticleModel(loadBalancerLimitGroups_._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), atom.linkType, scope=CTD_ANON))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUsageRecord'), accountUsageRecord_, scope=CTD_ANON))
CTD_ANON._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountUsageRecord')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON._GroupModel, min_occurs=1, max_occurs=1)



accountGroups_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountGroup'), accountGroup_, scope=accountGroups_))
accountGroups_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accountGroups_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountGroup')), min_occurs=0L, max_occurs=None)
    )
accountGroups_._ContentModel = pyxb.binding.content.ParticleModel(accountGroups_._GroupModel, min_occurs=1, max_occurs=1)



virtualIps_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIp'), virtualIp_, scope=virtualIps_))
virtualIps_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(virtualIps_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'virtualIp')), min_occurs=0L, max_occurs=None)
    )
virtualIps_._ContentModel = pyxb.binding.content.ParticleModel(virtualIps_._GroupModel, min_occurs=1, max_occurs=1)



customLimitAccount_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customLimits'), CustomLimits_, scope=customLimitAccount_))
customLimitAccount_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(customLimitAccount_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customLimits')), min_occurs=1L, max_occurs=1L)
    )
customLimitAccount_._ContentModel = pyxb.binding.content.ParticleModel(customLimitAccount_._GroupModel, min_occurs=1, max_occurs=1)



virtualIpBlocks_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIpBlock'), virtualIpBlock_, scope=virtualIpBlocks_))
virtualIpBlocks_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(virtualIpBlocks_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'virtualIpBlock')), min_occurs=0L, max_occurs=None)
    )
virtualIpBlocks_._ContentModel = pyxb.binding.content.ParticleModel(virtualIpBlocks_._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), atom.linkType, scope=CTD_ANON_))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsageRecord'), loadBalancerUsageRecord, scope=CTD_ANON_))
CTD_ANON_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerUsageRecord')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_._GroupModel, min_occurs=1, max_occurs=1)



clusters_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cluster'), cluster_, scope=clusters_))
clusters_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(clusters_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cluster')), min_occurs=1L, max_occurs=None)
    )
clusters_._ContentModel = pyxb.binding.content.ParticleModel(clusters_._GroupModel, min_occurs=1, max_occurs=1)



cidrTest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cidrBlock'), cidr_, scope=cidrTest_))
cidrTest_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cidrTest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cidrBlock')), min_occurs=0L, max_occurs=None)
    )
cidrTest_._ContentModel = pyxb.binding.content.ParticleModel(cidrTest_._GroupModel, min_occurs=1, max_occurs=1)



hostUsageRecords_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostUsageRecord'), hostUsageRecord_, scope=hostUsageRecords_))
hostUsageRecords_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hostUsageRecords_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hostUsageRecord')), min_occurs=1L, max_occurs=None)
    )
hostUsageRecords_._ContentModel = pyxb.binding.content.ParticleModel(hostUsageRecords_._GroupModel, min_occurs=1, max_occurs=1)



healthChecks_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'healthCheck'), healthCheck_, scope=healthChecks_))
healthChecks_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(healthChecks_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'healthCheck')), min_occurs=1L, max_occurs=None)
    )
healthChecks_._ContentModel = pyxb.binding.content.ParticleModel(healthChecks_._GroupModel, min_occurs=1, max_occurs=1)



accountLoadBalancers_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountLoadBalancer'), accountLoadBalancer_, scope=accountLoadBalancers_))
accountLoadBalancers_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accountLoadBalancers_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountLoadBalancer')), min_occurs=0L, max_occurs=None)
    )
accountLoadBalancers_._ContentModel = pyxb.binding.content.ParticleModel(accountLoadBalancers_._GroupModel, min_occurs=1, max_occurs=1)



loadBalancerLimitGroup_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accounts'), accounts_, scope=loadBalancerLimitGroup_))
loadBalancerLimitGroup_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancerLimitGroup_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accounts')), min_occurs=0L, max_occurs=1)
    )
loadBalancerLimitGroup_._ContentModel = pyxb.binding.content.ParticleModel(loadBalancerLimitGroup_._GroupModel, min_occurs=1, max_occurs=1)



loadBalancersStatusHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerStatusHistory'), loadBalancerStatusHistory_, scope=loadBalancersStatusHistory_))
loadBalancersStatusHistory_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancersStatusHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerStatusHistory')), min_occurs=0L, max_occurs=None)
    )
loadBalancersStatusHistory_._ContentModel = pyxb.binding.content.ParticleModel(loadBalancersStatusHistory_._GroupModel, min_occurs=1, max_occurs=1)



hostUsageRecord_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostUsages'), hostUsages_, scope=hostUsageRecord_))
hostUsageRecord_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hostUsageRecord_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hostUsages')), min_occurs=1L, max_occurs=1)
    )
hostUsageRecord_._ContentModel = pyxb.binding.content.ParticleModel(hostUsageRecord_._GroupModel, min_occurs=1, max_occurs=1)



hosts_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'host'), host_, scope=hosts_))
hosts_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hosts_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'host')), min_occurs=0L, max_occurs=None)
    )
hosts_._ContentModel = pyxb.binding.content.ParticleModel(hosts_._GroupModel, min_occurs=1, max_occurs=1)



customerList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customers'), customers_, scope=customerList_))
customerList_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(customerList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customers')), min_occurs=0L, max_occurs=1)
    )
customerList_._ContentModel = pyxb.binding.content.ParticleModel(customerList_._GroupModel, min_occurs=1, max_occurs=1)



ldapInfo_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'userRole'), userRole_, scope=ldapInfo_))

ldapInfo_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ldapGroup'), ldapGroup_, scope=ldapInfo_))
ldapInfo_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ldapInfo_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ldapGroup')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(ldapInfo_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'userRole')), min_occurs=0L, max_occurs=None)
    )
ldapInfo_._ContentModel = pyxb.binding.content.ParticleModel(ldapInfo_._GroupModel, min_occurs=1, max_occurs=1)



blacklist_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'blacklistItem'), blacklistItem_, scope=blacklist_))
blacklist_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(blacklist_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'blacklistItem')), min_occurs=0L, max_occurs=None)
    )
blacklist_._ContentModel = pyxb.binding.content.ParticleModel(blacklist_._GroupModel, min_occurs=1, max_occurs=1)



accountGroup_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'group'), groupRateLimit_, scope=accountGroup_))
accountGroup_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accountGroup_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'group')), min_occurs=1, max_occurs=1)
    )
accountGroup_._ContentModel = pyxb.binding.content.ParticleModel(accountGroup_._GroupModel, min_occurs=1, max_occurs=1)



customLimitAccounts_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customLimitAccount'), customLimitAccount_, scope=customLimitAccounts_))
customLimitAccounts_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(customLimitAccounts_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customLimitAccount')), min_occurs=0L, max_occurs=None)
    )
customLimitAccounts_._ContentModel = pyxb.binding.content.ParticleModel(customLimitAccounts_._GroupModel, min_occurs=1, max_occurs=1)



accountBillings_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'accountBilling'), lbaas.accountBilling_, scope=accountBillings_))
accountBillings_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accountBillings_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/loadbalancers/api/v1.0'), u'accountBilling')), min_occurs=0L, max_occurs=None)
    )
accountBillings_._ContentModel = pyxb.binding.content.ParticleModel(accountBillings_._GroupModel, min_occurs=1, max_occurs=1)



loadBalancerAudits_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerAudit'), loadBalancerAudit_, scope=loadBalancerAudits_))
loadBalancerAudits_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(loadBalancerAudits_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancerAudit')), min_occurs=1L, max_occurs=None)
    )
loadBalancerAudits_._ContentModel = pyxb.binding.content.ParticleModel(loadBalancerAudits_._GroupModel, min_occurs=1, max_occurs=1)



customers_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customer'), customer_, scope=customers_))
customers_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(customers_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customer')), min_occurs=1L, max_occurs=None)
    )
customers_._ContentModel = pyxb.binding.content.ParticleModel(customers_._GroupModel, min_occurs=1, max_occurs=1)



hostUsageList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostUsageRecords'), hostUsageRecords_, scope=hostUsageList_))
hostUsageList_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hostUsageList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hostUsageRecords')), min_occurs=0L, max_occurs=1)
    )
hostUsageList_._ContentModel = pyxb.binding.content.ParticleModel(hostUsageList_._GroupModel, min_occurs=1, max_occurs=1)



customer_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadBalancers'), loadBalancers_, scope=customer_))
customer_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(customer_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loadBalancers')), min_occurs=0L, max_occurs=1)
    )
customer_._ContentModel = pyxb.binding.content.ParticleModel(customer_._GroupModel, min_occurs=1, max_occurs=1)



listOfInts_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ints'), pyxb.binding.datatypes.int, scope=listOfInts_))
listOfInts_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(listOfInts_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ints')), min_occurs=0L, max_occurs=None)
    )
listOfInts_._ContentModel = pyxb.binding.content.ParticleModel(listOfInts_._GroupModel, min_occurs=1, max_occurs=1)



hostCapacityReports_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hostCapacityReport'), hostCapacityReport_, scope=hostCapacityReports_))
hostCapacityReports_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(hostCapacityReports_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hostCapacityReport')), min_occurs=0L, max_occurs=None)
    )
hostCapacityReports_._ContentModel = pyxb.binding.content.ParticleModel(hostCapacityReports_._GroupModel, min_occurs=1, max_occurs=1)



virtualIpAvailabilityReports_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualIpAvailabilityReport'), virtualIpAvailabilityReport_, scope=virtualIpAvailabilityReports_))
virtualIpAvailabilityReports_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(virtualIpAvailabilityReports_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'virtualIpAvailabilityReport')), min_occurs=0L, max_occurs=None)
    )
virtualIpAvailabilityReports_._ContentModel = pyxb.binding.content.ParticleModel(virtualIpAvailabilityReports_._GroupModel, min_occurs=1, max_occurs=1)



ports_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'port'), port_, scope=ports_))
ports_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ports_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'port')), min_occurs=0L, max_occurs=None)
    )
ports_._ContentModel = pyxb.binding.content.ParticleModel(ports_._GroupModel, min_occurs=1, max_occurs=1)
