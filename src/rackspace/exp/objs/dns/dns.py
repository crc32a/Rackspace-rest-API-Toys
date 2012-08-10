# ./dns.py
# PyXB bindings for NM:667e9e802600ff597c2744508bdb91f48c323c7e
# Generated 2012-08-10 11:25:00.642483 by PyXB version 1.1.3
# Namespace http://docs.rackspacecloud.com/dns/api/v1.0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:eea10da8-e307-11e1-979e-002564955ea1')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _atom

Namespace = pyxb.namespace.NamespaceForURI(u'http://docs.rackspacecloud.com/dns/api/v1.0', create_if_missing=True)
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
class publicRecordType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'publicRecordType')
    _Documentation = None
publicRecordType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=publicRecordType, enum_prefix=None)
publicRecordType.A = publicRecordType._CF_enumeration.addEnumeration(unicode_value=u'A', tag=u'A')
publicRecordType.CNAME = publicRecordType._CF_enumeration.addEnumeration(unicode_value=u'CNAME', tag=u'CNAME')
publicRecordType.TXT = publicRecordType._CF_enumeration.addEnumeration(unicode_value=u'TXT', tag=u'TXT')
publicRecordType.NS = publicRecordType._CF_enumeration.addEnumeration(unicode_value=u'NS', tag=u'NS')
publicRecordType.AAAA = publicRecordType._CF_enumeration.addEnumeration(unicode_value=u'AAAA', tag=u'AAAA')
publicRecordType.MX = publicRecordType._CF_enumeration.addEnumeration(unicode_value=u'MX', tag=u'MX')
publicRecordType._InitializeFacetMap(publicRecordType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'publicRecordType', publicRecordType)

# Atomic SimpleTypeDefinition
class dnsContentFileType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dnsContentFileType')
    _Documentation = None
dnsContentFileType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dnsContentFileType, enum_prefix=None)
dnsContentFileType.BIND_9 = dnsContentFileType._CF_enumeration.addEnumeration(unicode_value=u'BIND_9', tag=u'BIND_9')
dnsContentFileType._InitializeFacetMap(dnsContentFileType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'dnsContentFileType', dnsContentFileType)

# Atomic SimpleTypeDefinition
class dnsStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dnsStatus')
    _Documentation = None
dnsStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dnsStatus, enum_prefix=None)
dnsStatus.INITIALIZED = dnsStatus._CF_enumeration.addEnumeration(unicode_value=u'INITIALIZED', tag=u'INITIALIZED')
dnsStatus.ACTIVE = dnsStatus._CF_enumeration.addEnumeration(unicode_value=u'ACTIVE', tag=u'ACTIVE')
dnsStatus.ERROR = dnsStatus._CF_enumeration.addEnumeration(unicode_value=u'ERROR', tag=u'ERROR')
dnsStatus.PENDING = dnsStatus._CF_enumeration.addEnumeration(unicode_value=u'PENDING', tag=u'PENDING')
dnsStatus.SUSPENDED = dnsStatus._CF_enumeration.addEnumeration(unicode_value=u'SUSPENDED', tag=u'SUSPENDED')
dnsStatus.DELETED = dnsStatus._CF_enumeration.addEnumeration(unicode_value=u'DELETED', tag=u'DELETED')
dnsStatus._InitializeFacetMap(dnsStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'dnsStatus', dnsStatus)

# Atomic SimpleTypeDefinition
class recordType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recordType')
    _Documentation = None
recordType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=recordType, enum_prefix=None)
recordType.A = recordType._CF_enumeration.addEnumeration(unicode_value=u'A', tag=u'A')
recordType.CNAME = recordType._CF_enumeration.addEnumeration(unicode_value=u'CNAME', tag=u'CNAME')
recordType.TXT = recordType._CF_enumeration.addEnumeration(unicode_value=u'TXT', tag=u'TXT')
recordType.NS = recordType._CF_enumeration.addEnumeration(unicode_value=u'NS', tag=u'NS')
recordType.AAAA = recordType._CF_enumeration.addEnumeration(unicode_value=u'AAAA', tag=u'AAAA')
recordType.MX = recordType._CF_enumeration.addEnumeration(unicode_value=u'MX', tag=u'MX')
recordType.SRV = recordType._CF_enumeration.addEnumeration(unicode_value=u'SRV', tag=u'SRV')
recordType.PTR = recordType._CF_enumeration.addEnumeration(unicode_value=u'PTR', tag=u'PTR')
recordType.SOA = recordType._CF_enumeration.addEnumeration(unicode_value=u'SOA', tag=u'SOA')
recordType.DKIM = recordType._CF_enumeration.addEnumeration(unicode_value=u'DKIM', tag=u'DKIM')
recordType.DNAME = recordType._CF_enumeration.addEnumeration(unicode_value=u'DNAME', tag=u'DNAME')
recordType._InitializeFacetMap(recordType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'recordType', recordType)

# Atomic SimpleTypeDefinition
class verb (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'verb')
    _Documentation = None
verb._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=verb, enum_prefix=None)
verb.GET = verb._CF_enumeration.addEnumeration(unicode_value=u'GET', tag=u'GET')
verb.POST = verb._CF_enumeration.addEnumeration(unicode_value=u'POST', tag=u'POST')
verb.PUT = verb._CF_enumeration.addEnumeration(unicode_value=u'PUT', tag=u'PUT')
verb.DELETE = verb._CF_enumeration.addEnumeration(unicode_value=u'DELETE', tag=u'DELETE')
verb._InitializeFacetMap(verb._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'verb', verb)

# Atomic SimpleTypeDefinition
class asyncStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'asyncStatus')
    _Documentation = None
asyncStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=asyncStatus, enum_prefix=None)
asyncStatus.INITIALIZED = asyncStatus._CF_enumeration.addEnumeration(unicode_value=u'INITIALIZED', tag=u'INITIALIZED')
asyncStatus.RUNNING = asyncStatus._CF_enumeration.addEnumeration(unicode_value=u'RUNNING', tag=u'RUNNING')
asyncStatus.COMPLETED = asyncStatus._CF_enumeration.addEnumeration(unicode_value=u'COMPLETED', tag=u'COMPLETED')
asyncStatus.ERROR = asyncStatus._CF_enumeration.addEnumeration(unicode_value=u'ERROR', tag=u'ERROR')
asyncStatus.CANCELED = asyncStatus._CF_enumeration.addEnumeration(unicode_value=u'CANCELED', tag=u'CANCELED')
asyncStatus._InitializeFacetMap(asyncStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'asyncStatus', asyncStatus)

# Complex type changeDetail_ with content type EMPTY
class changeDetail_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'changeDetail')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute field uses Python identifier field
    __field = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'field'), 'field', '__httpdocs_rackspacecloud_comdnsapiv1_0_changeDetail__field', pyxb.binding.datatypes.string)
    
    field = property(__field.value, __field.set, None, None)

    
    # Attribute originalValue uses Python identifier originalValue
    __originalValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'originalValue'), 'originalValue', '__httpdocs_rackspacecloud_comdnsapiv1_0_changeDetail__originalValue', pyxb.binding.datatypes.string)
    
    originalValue = property(__originalValue.value, __originalValue.set, None, None)

    
    # Attribute newValue uses Python identifier newValue
    __newValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'newValue'), 'newValue', '__httpdocs_rackspacecloud_comdnsapiv1_0_changeDetail__newValue', pyxb.binding.datatypes.string)
    
    newValue = property(__newValue.value, __newValue.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __field.name() : __field,
        __originalValue.name() : __originalValue,
        __newValue.name() : __newValue
    }
Namespace.addCategoryObject('typeBinding', u'changeDetail', changeDetail_)


# Complex type dnsFault_ with content type ELEMENT_ONLY
class dnsFault_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dnsFault')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}details uses Python identifier details
    __details = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'details'), 'details', '__httpdocs_rackspacecloud_comdnsapiv1_0_dnsFault__httpdocs_rackspacecloud_comdnsapiv1_0details', False)

    
    details = property(__details.value, __details.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpdocs_rackspacecloud_comdnsapiv1_0_dnsFault__httpdocs_rackspacecloud_comdnsapiv1_0message', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'code'), 'code', '__httpdocs_rackspacecloud_comdnsapiv1_0_dnsFault__code', pyxb.binding.datatypes.int)
    
    code = property(__code.value, __code.set, None, None)


    _ElementMap = {
        __details.name() : __details,
        __message.name() : __message
    }
    _AttributeMap = {
        __code.name() : __code
    }
Namespace.addCategoryObject('typeBinding', u'dnsFault', dnsFault_)


# Complex type itemAlreadyExists_ with content type ELEMENT_ONLY
class itemAlreadyExists_ (dnsFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'itemAlreadyExists')
    # Base type is dnsFault_
    
    # Element details ({http://docs.rackspacecloud.com/dns/api/v1.0}details) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Element message ({http://docs.rackspacecloud.com/dns/api/v1.0}message) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Attribute code inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault

    _ElementMap = dnsFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = dnsFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'itemAlreadyExists', itemAlreadyExists_)


# Complex type rdns_ with content type ELEMENT_ONLY
class rdns_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'rdns')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}recordsList uses Python identifier recordsList
    __recordsList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recordsList'), 'recordsList', '__httpdocs_rackspacecloud_comdnsapiv1_0_rdns__httpdocs_rackspacecloud_comdnsapiv1_0recordsList', False)

    
    recordsList = property(__recordsList.value, __recordsList.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), 'link', '__httpdocs_rackspacecloud_comdnsapiv1_0_rdns__httpwww_w3_org2005Atomlink', False)

    
    link = property(__link.value, __link.set, None, None)


    _ElementMap = {
        __recordsList.name() : __recordsList,
        __link.name() : __link
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'rdns', rdns_)


# Complex type change_ with content type ELEMENT_ONLY
class change_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'change')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}changeDetail uses Python identifier changeDetail
    __changeDetail = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'changeDetail'), 'changeDetail', '__httpdocs_rackspacecloud_comdnsapiv1_0_change__httpdocs_rackspacecloud_comdnsapiv1_0changeDetail', True)

    
    changeDetail = property(__changeDetail.value, __changeDetail.set, None, None)

    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'action'), 'action', '__httpdocs_rackspacecloud_comdnsapiv1_0_change__action', pyxb.binding.datatypes.string)
    
    action = property(__action.value, __action.set, None, None)

    
    # Attribute changeDate uses Python identifier changeDate
    __changeDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'changeDate'), 'changeDate', '__httpdocs_rackspacecloud_comdnsapiv1_0_change__changeDate', pyxb.binding.datatypes.dateTime)
    
    changeDate = property(__changeDate.value, __changeDate.set, None, None)

    
    # Attribute domain uses Python identifier domain
    __domain = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'domain'), 'domain', '__httpdocs_rackspacecloud_comdnsapiv1_0_change__domain', pyxb.binding.datatypes.string)
    
    domain = property(__domain.value, __domain.set, None, None)

    
    # Attribute targetId uses Python identifier targetId
    __targetId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'targetId'), 'targetId', '__httpdocs_rackspacecloud_comdnsapiv1_0_change__targetId', pyxb.binding.datatypes.int)
    
    targetId = property(__targetId.value, __targetId.set, None, None)

    
    # Attribute targetType uses Python identifier targetType
    __targetType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'targetType'), 'targetType', '__httpdocs_rackspacecloud_comdnsapiv1_0_change__targetType', pyxb.binding.datatypes.string)
    
    targetType = property(__targetType.value, __targetType.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_rackspacecloud_comdnsapiv1_0_change__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)


    _ElementMap = {
        __changeDetail.name() : __changeDetail
    }
    _AttributeMap = {
        __action.name() : __action,
        __changeDate.name() : __changeDate,
        __domain.name() : __domain,
        __targetId.name() : __targetId,
        __targetType.name() : __targetType,
        __accountId.name() : __accountId
    }
Namespace.addCategoryObject('typeBinding', u'change', change_)


# Complex type domain_ with content type ELEMENT_ONLY
class domain_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'domain')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}contents uses Python identifier contents
    __contents = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'contents'), 'contents', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__httpdocs_rackspacecloud_comdnsapiv1_0contents', False)

    
    contents = property(__contents.value, __contents.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}recordsList uses Python identifier recordsList
    __recordsList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recordsList'), 'recordsList', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__httpdocs_rackspacecloud_comdnsapiv1_0recordsList', False)

    
    recordsList = property(__recordsList.value, __recordsList.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}nameservers uses Python identifier nameservers
    __nameservers = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nameservers'), 'nameservers', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__httpdocs_rackspacecloud_comdnsapiv1_0nameservers', False)

    
    nameservers = property(__nameservers.value, __nameservers.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}subdomains uses Python identifier subdomains
    __subdomains = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'subdomains'), 'subdomains', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__httpdocs_rackspacecloud_comdnsapiv1_0subdomains', False)

    
    subdomains = property(__subdomains.value, __subdomains.set, None, None)

    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'created'), 'created', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__created', pyxb.binding.datatypes.dateTime)
    
    created = property(__created.value, __created.set, None, None)

    
    # Attribute contentType uses Python identifier contentType
    __contentType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'contentType'), 'contentType', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__contentType', dnsContentFileType)
    
    contentType = property(__contentType.value, __contentType.set, None, None)

    
    # Attribute emailAddress uses Python identifier emailAddress
    __emailAddress = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'emailAddress'), 'emailAddress', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__emailAddress', pyxb.binding.datatypes.string)
    
    emailAddress = property(__emailAddress.value, __emailAddress.set, None, None)

    
    # Attribute accountId uses Python identifier accountId
    __accountId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'accountId'), 'accountId', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__accountId', pyxb.binding.datatypes.int)
    
    accountId = property(__accountId.value, __accountId.set, None, None)

    
    # Attribute ttl uses Python identifier ttl
    __ttl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ttl'), 'ttl', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__ttl', pyxb.binding.datatypes.int)
    
    ttl = property(__ttl.value, __ttl.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__status', dnsStatus)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute owner uses Python identifier owner
    __owner = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'owner'), 'owner', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__owner', pyxb.binding.datatypes.string)
    
    owner = property(__owner.value, __owner.set, None, None)

    
    # Attribute updated uses Python identifier updated
    __updated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'updated'), 'updated', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__updated', pyxb.binding.datatypes.dateTime)
    
    updated = property(__updated.value, __updated.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__id', pyxb.binding.datatypes.int)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute comment uses Python identifier comment
    __comment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'comment'), 'comment', '__httpdocs_rackspacecloud_comdnsapiv1_0_domain__comment', pyxb.binding.datatypes.string)
    
    comment = property(__comment.value, __comment.set, None, None)


    _ElementMap = {
        __contents.name() : __contents,
        __recordsList.name() : __recordsList,
        __nameservers.name() : __nameservers,
        __subdomains.name() : __subdomains
    }
    _AttributeMap = {
        __created.name() : __created,
        __contentType.name() : __contentType,
        __emailAddress.name() : __emailAddress,
        __accountId.name() : __accountId,
        __ttl.name() : __ttl,
        __status.name() : __status,
        __owner.name() : __owner,
        __updated.name() : __updated,
        __name.name() : __name,
        __id.name() : __id,
        __comment.name() : __comment
    }
Namespace.addCategoryObject('typeBinding', u'domain', domain_)


# Complex type unauthorized_ with content type ELEMENT_ONLY
class unauthorized_ (dnsFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'unauthorized')
    # Base type is dnsFault_
    
    # Element details ({http://docs.rackspacecloud.com/dns/api/v1.0}details) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Element message ({http://docs.rackspacecloud.com/dns/api/v1.0}message) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Attribute code inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault

    _ElementMap = dnsFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = dnsFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'unauthorized', unauthorized_)


# Complex type nameservers_ with content type ELEMENT_ONLY
class nameservers_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameservers')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}nameserver uses Python identifier nameserver
    __nameserver = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nameserver'), 'nameserver', '__httpdocs_rackspacecloud_comdnsapiv1_0_nameservers__httpdocs_rackspacecloud_comdnsapiv1_0nameserver', True)

    
    nameserver = property(__nameserver.value, __nameserver.set, None, None)


    _ElementMap = {
        __nameserver.name() : __nameserver
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'nameservers', nameservers_)


# Complex type domains_ with content type ELEMENT_ONLY
class domains_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'domains')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}domain uses Python identifier domain
    __domain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'domain'), 'domain', '__httpdocs_rackspacecloud_comdnsapiv1_0_domains__httpdocs_rackspacecloud_comdnsapiv1_0domain', True)

    
    domain = property(__domain.value, __domain.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), 'link', '__httpdocs_rackspacecloud_comdnsapiv1_0_domains__httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Attribute totalEntries uses Python identifier totalEntries
    __totalEntries = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'totalEntries'), 'totalEntries', '__httpdocs_rackspacecloud_comdnsapiv1_0_domains__totalEntries', pyxb.binding.datatypes.int)
    
    totalEntries = property(__totalEntries.value, __totalEntries.set, None, None)


    _ElementMap = {
        __domain.name() : __domain,
        __link.name() : __link
    }
    _AttributeMap = {
        __totalEntries.name() : __totalEntries
    }
Namespace.addCategoryObject('typeBinding', u'domains', domains_)


# Complex type deleteFault_ with content type ELEMENT_ONLY
class deleteFault_ (dnsFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'deleteFault')
    # Base type is dnsFault_
    
    # Element details ({http://docs.rackspacecloud.com/dns/api/v1.0}details) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}failedItems uses Python identifier failedItems
    __failedItems = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'failedItems'), 'failedItems', '__httpdocs_rackspacecloud_comdnsapiv1_0_deleteFault__httpdocs_rackspacecloud_comdnsapiv1_0failedItems', False)

    
    failedItems = property(__failedItems.value, __failedItems.set, None, None)

    
    # Element message ({http://docs.rackspacecloud.com/dns/api/v1.0}message) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Attribute code inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault

    _ElementMap = dnsFault_._ElementMap.copy()
    _ElementMap.update({
        __failedItems.name() : __failedItems
    })
    _AttributeMap = dnsFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'deleteFault', deleteFault_)


# Complex type serviceUnavailable_ with content type ELEMENT_ONLY
class serviceUnavailable_ (dnsFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'serviceUnavailable')
    # Base type is dnsFault_
    
    # Element details ({http://docs.rackspacecloud.com/dns/api/v1.0}details) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Element message ({http://docs.rackspacecloud.com/dns/api/v1.0}message) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Attribute code inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault

    _ElementMap = dnsFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = dnsFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'serviceUnavailable', serviceUnavailable_)


# Complex type asyncResponse_ with content type ELEMENT_ONLY
class asyncResponse_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'asyncResponse')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpdocs_rackspacecloud_comdnsapiv1_0_asyncResponse__httpdocs_rackspacecloud_comdnsapiv1_0response', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}error uses Python identifier error
    __error = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'error'), 'error', '__httpdocs_rackspacecloud_comdnsapiv1_0_asyncResponse__httpdocs_rackspacecloud_comdnsapiv1_0error', False)

    
    error = property(__error.value, __error.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}requestUrl uses Python identifier requestUrl
    __requestUrl = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'requestUrl'), 'requestUrl', '__httpdocs_rackspacecloud_comdnsapiv1_0_asyncResponse__httpdocs_rackspacecloud_comdnsapiv1_0requestUrl', False)

    
    requestUrl = property(__requestUrl.value, __requestUrl.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}callbackUrl uses Python identifier callbackUrl
    __callbackUrl = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'callbackUrl'), 'callbackUrl', '__httpdocs_rackspacecloud_comdnsapiv1_0_asyncResponse__httpdocs_rackspacecloud_comdnsapiv1_0callbackUrl', False)

    
    callbackUrl = property(__callbackUrl.value, __callbackUrl.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}jobId uses Python identifier jobId
    __jobId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'jobId'), 'jobId', '__httpdocs_rackspacecloud_comdnsapiv1_0_asyncResponse__httpdocs_rackspacecloud_comdnsapiv1_0jobId', False)

    
    jobId = property(__jobId.value, __jobId.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}request uses Python identifier request
    __request = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'request'), 'request', '__httpdocs_rackspacecloud_comdnsapiv1_0_asyncResponse__httpdocs_rackspacecloud_comdnsapiv1_0request', False)

    
    request = property(__request.value, __request.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}status uses Python identifier status
    __status = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'status'), 'status', '__httpdocs_rackspacecloud_comdnsapiv1_0_asyncResponse__httpdocs_rackspacecloud_comdnsapiv1_0status', False)

    
    status = property(__status.value, __status.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}verb uses Python identifier verb
    __verb = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'verb'), 'verb', '__httpdocs_rackspacecloud_comdnsapiv1_0_asyncResponse__httpdocs_rackspacecloud_comdnsapiv1_0verb', False)

    
    verb = property(__verb.value, __verb.set, None, None)


    _ElementMap = {
        __response.name() : __response,
        __error.name() : __error,
        __requestUrl.name() : __requestUrl,
        __callbackUrl.name() : __callbackUrl,
        __jobId.name() : __jobId,
        __request.name() : __request,
        __status.name() : __status,
        __verb.name() : __verb
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'asyncResponse', asyncResponse_)


# Complex type validationFaults with content type ELEMENT_ONLY
class validationFaults (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'validationFaults')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}fault uses Python identifier fault
    __fault = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fault'), 'fault', '__httpdocs_rackspacecloud_comdnsapiv1_0_validationFaults_httpdocs_rackspacecloud_comdnsapiv1_0fault', True)

    
    fault = property(__fault.value, __fault.set, None, None)


    _ElementMap = {
        __fault.name() : __fault
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'validationFaults', validationFaults)


# Complex type recordsList_ with content type ELEMENT_ONLY
class recordsList_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recordsList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), 'link', '__httpdocs_rackspacecloud_comdnsapiv1_0_recordsList__httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}record uses Python identifier record
    __record = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'record'), 'record', '__httpdocs_rackspacecloud_comdnsapiv1_0_recordsList__httpdocs_rackspacecloud_comdnsapiv1_0record', True)

    
    record = property(__record.value, __record.set, None, None)

    
    # Attribute totalEntries uses Python identifier totalEntries
    __totalEntries = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'totalEntries'), 'totalEntries', '__httpdocs_rackspacecloud_comdnsapiv1_0_recordsList__totalEntries', pyxb.binding.datatypes.int)
    
    totalEntries = property(__totalEntries.value, __totalEntries.set, None, None)


    _ElementMap = {
        __link.name() : __link,
        __record.name() : __record
    }
    _AttributeMap = {
        __totalEntries.name() : __totalEntries
    }
Namespace.addCategoryObject('typeBinding', u'recordsList', recordsList_)


# Complex type subdomains_ with content type ELEMENT_ONLY
class subdomains_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'subdomains')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), 'link', '__httpdocs_rackspacecloud_comdnsapiv1_0_subdomains__httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}domain uses Python identifier domain
    __domain = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'domain'), 'domain', '__httpdocs_rackspacecloud_comdnsapiv1_0_subdomains__httpdocs_rackspacecloud_comdnsapiv1_0domain', True)

    
    domain = property(__domain.value, __domain.set, None, None)

    
    # Attribute totalEntries uses Python identifier totalEntries
    __totalEntries = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'totalEntries'), 'totalEntries', '__httpdocs_rackspacecloud_comdnsapiv1_0_subdomains__totalEntries', pyxb.binding.datatypes.int)
    
    totalEntries = property(__totalEntries.value, __totalEntries.set, None, None)


    _ElementMap = {
        __link.name() : __link,
        __domain.name() : __domain
    }
    _AttributeMap = {
        __totalEntries.name() : __totalEntries
    }
Namespace.addCategoryObject('typeBinding', u'subdomains', subdomains_)


# Complex type record_ with content type EMPTY
class record_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'record')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute data uses Python identifier data
    __data = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'data'), 'data', '__httpdocs_rackspacecloud_comdnsapiv1_0_record__data', pyxb.binding.datatypes.string)
    
    data = property(__data.value, __data.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_rackspacecloud_comdnsapiv1_0_record__name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute updated uses Python identifier updated
    __updated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'updated'), 'updated', '__httpdocs_rackspacecloud_comdnsapiv1_0_record__updated', pyxb.binding.datatypes.dateTime)
    
    updated = property(__updated.value, __updated.set, None, None)

    
    # Attribute priority uses Python identifier priority
    __priority = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'priority'), 'priority', '__httpdocs_rackspacecloud_comdnsapiv1_0_record__priority', pyxb.binding.datatypes.int)
    
    priority = property(__priority.value, __priority.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdocs_rackspacecloud_comdnsapiv1_0_record__id', pyxb.binding.datatypes.string)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute ttl uses Python identifier ttl
    __ttl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ttl'), 'ttl', '__httpdocs_rackspacecloud_comdnsapiv1_0_record__ttl', pyxb.binding.datatypes.int)
    
    ttl = property(__ttl.value, __ttl.set, None, None)

    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'created'), 'created', '__httpdocs_rackspacecloud_comdnsapiv1_0_record__created', pyxb.binding.datatypes.dateTime)
    
    created = property(__created.value, __created.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpdocs_rackspacecloud_comdnsapiv1_0_record__type', recordType)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute comment uses Python identifier comment
    __comment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'comment'), 'comment', '__httpdocs_rackspacecloud_comdnsapiv1_0_record__comment', pyxb.binding.datatypes.string)
    
    comment = property(__comment.value, __comment.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpdocs_rackspacecloud_comdnsapiv1_0_record__status', dnsStatus)
    
    status = property(__status.value, __status.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __data.name() : __data,
        __name.name() : __name,
        __updated.name() : __updated,
        __priority.name() : __priority,
        __id.name() : __id,
        __ttl.name() : __ttl,
        __created.name() : __created,
        __type.name() : __type,
        __comment.name() : __comment,
        __status.name() : __status
    }
Namespace.addCategoryObject('typeBinding', u'record', record_)


# Complex type nameserver with content type EMPTY
class nameserver (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameserver')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_rackspacecloud_comdnsapiv1_0_nameserver_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'nameserver', nameserver)


# Complex type internalServerError_ with content type ELEMENT_ONLY
class internalServerError_ (dnsFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'internalServerError')
    # Base type is dnsFault_
    
    # Element details ({http://docs.rackspacecloud.com/dns/api/v1.0}details) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Element message ({http://docs.rackspacecloud.com/dns/api/v1.0}message) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Attribute code inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault

    _ElementMap = dnsFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = dnsFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'internalServerError', internalServerError_)


# Complex type validationErrors with content type ELEMENT_ONLY
class validationErrors (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'validationErrors')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}messages uses Python identifier messages
    __messages = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'messages'), 'messages', '__httpdocs_rackspacecloud_comdnsapiv1_0_validationErrors_httpdocs_rackspacecloud_comdnsapiv1_0messages', True)

    
    messages = property(__messages.value, __messages.set, None, None)


    _ElementMap = {
        __messages.name() : __messages
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'validationErrors', validationErrors)


# Complex type itemNotFound_ with content type ELEMENT_ONLY
class itemNotFound_ (dnsFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'itemNotFound')
    # Base type is dnsFault_
    
    # Element details ({http://docs.rackspacecloud.com/dns/api/v1.0}details) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Element message ({http://docs.rackspacecloud.com/dns/api/v1.0}message) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Attribute code inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault

    _ElementMap = dnsFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = dnsFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'itemNotFound', itemNotFound_)


# Complex type badRequest_ with content type ELEMENT_ONLY
class badRequest_ (dnsFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'badRequest')
    # Base type is dnsFault_
    
    # Element details ({http://docs.rackspacecloud.com/dns/api/v1.0}details) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}validationErrors uses Python identifier validationErrors
    __validationErrors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'validationErrors'), 'validationErrors', '__httpdocs_rackspacecloud_comdnsapiv1_0_badRequest__httpdocs_rackspacecloud_comdnsapiv1_0validationErrors', False)

    
    validationErrors = property(__validationErrors.value, __validationErrors.set, None, None)

    
    # Element message ({http://docs.rackspacecloud.com/dns/api/v1.0}message) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Attribute code inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault

    _ElementMap = dnsFault_._ElementMap.copy()
    _ElementMap.update({
        __validationErrors.name() : __validationErrors
    })
    _AttributeMap = dnsFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'badRequest', badRequest_)


# Complex type asyncJobsStatus_ with content type ELEMENT_ONLY
class asyncJobsStatus_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'asyncJobsStatus')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), 'link', '__httpdocs_rackspacecloud_comdnsapiv1_0_asyncJobsStatus__httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}asyncResponse uses Python identifier asyncResponse
    __asyncResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'asyncResponse'), 'asyncResponse', '__httpdocs_rackspacecloud_comdnsapiv1_0_asyncJobsStatus__httpdocs_rackspacecloud_comdnsapiv1_0asyncResponse', True)

    
    asyncResponse = property(__asyncResponse.value, __asyncResponse.set, None, None)

    
    # Attribute totalEntries uses Python identifier totalEntries
    __totalEntries = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'totalEntries'), 'totalEntries', '__httpdocs_rackspacecloud_comdnsapiv1_0_asyncJobsStatus__totalEntries', pyxb.binding.datatypes.int)
    
    totalEntries = property(__totalEntries.value, __totalEntries.set, None, None)


    _ElementMap = {
        __link.name() : __link,
        __asyncResponse.name() : __asyncResponse
    }
    _AttributeMap = {
        __totalEntries.name() : __totalEntries
    }
Namespace.addCategoryObject('typeBinding', u'asyncJobsStatus', asyncJobsStatus_)


# Complex type changes_ with content type ELEMENT_ONLY
class changes_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'changes')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}change uses Python identifier change
    __change = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'change'), 'change', '__httpdocs_rackspacecloud_comdnsapiv1_0_changes__httpdocs_rackspacecloud_comdnsapiv1_0change', True)

    
    change = property(__change.value, __change.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), 'link', '__httpdocs_rackspacecloud_comdnsapiv1_0_changes__httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'from'), 'from_', '__httpdocs_rackspacecloud_comdnsapiv1_0_changes__from', pyxb.binding.datatypes.dateTime)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'to'), 'to', '__httpdocs_rackspacecloud_comdnsapiv1_0_changes__to', pyxb.binding.datatypes.dateTime)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute totalEntries uses Python identifier totalEntries
    __totalEntries = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'totalEntries'), 'totalEntries', '__httpdocs_rackspacecloud_comdnsapiv1_0_changes__totalEntries', pyxb.binding.datatypes.int)
    
    totalEntries = property(__totalEntries.value, __totalEntries.set, None, None)


    _ElementMap = {
        __change.name() : __change,
        __link.name() : __link
    }
    _AttributeMap = {
        __from.name() : __from,
        __to.name() : __to,
        __totalEntries.name() : __totalEntries
    }
Namespace.addCategoryObject('typeBinding', u'changes', changes_)


# Complex type overLimit_ with content type ELEMENT_ONLY
class overLimit_ (dnsFault_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'overLimit')
    # Base type is dnsFault_
    
    # Element details ({http://docs.rackspacecloud.com/dns/api/v1.0}details) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Element message ({http://docs.rackspacecloud.com/dns/api/v1.0}message) inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault
    
    # Attribute code inherited from {http://docs.rackspacecloud.com/dns/api/v1.0}dnsFault

    _ElementMap = dnsFault_._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = dnsFault_._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'overLimit', overLimit_)


# Complex type recordTypes_ with content type ELEMENT_ONLY
class recordTypes_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recordTypes')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.rackspacecloud.com/dns/api/v1.0}recordType uses Python identifier recordType
    __recordType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recordType'), 'recordType', '__httpdocs_rackspacecloud_comdnsapiv1_0_recordTypes__httpdocs_rackspacecloud_comdnsapiv1_0recordType', True)

    
    recordType = property(__recordType.value, __recordType.set, None, None)


    _ElementMap = {
        __recordType.name() : __recordType
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'recordTypes', recordTypes_)


changeDetail = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'changeDetail'), changeDetail_)
Namespace.addCategoryObject('elementBinding', changeDetail.name().localName(), changeDetail)

itemAlreadyExists = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'itemAlreadyExists'), itemAlreadyExists_)
Namespace.addCategoryObject('elementBinding', itemAlreadyExists.name().localName(), itemAlreadyExists)

rdns = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rdns'), rdns_)
Namespace.addCategoryObject('elementBinding', rdns.name().localName(), rdns)

change = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'change'), change_)
Namespace.addCategoryObject('elementBinding', change.name().localName(), change)

unauthorized = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unauthorized'), unauthorized_)
Namespace.addCategoryObject('elementBinding', unauthorized.name().localName(), unauthorized)

domains = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'domains'), domains_)
Namespace.addCategoryObject('elementBinding', domains.name().localName(), domains)

deleteFault = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'deleteFault'), deleteFault_)
Namespace.addCategoryObject('elementBinding', deleteFault.name().localName(), deleteFault)

serviceUnavailable = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'serviceUnavailable'), serviceUnavailable_)
Namespace.addCategoryObject('elementBinding', serviceUnavailable.name().localName(), serviceUnavailable)

asyncResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'asyncResponse'), asyncResponse_)
Namespace.addCategoryObject('elementBinding', asyncResponse.name().localName(), asyncResponse)

domain = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'domain'), domain_)
Namespace.addCategoryObject('elementBinding', domain.name().localName(), domain)

record = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'record'), record_)
Namespace.addCategoryObject('elementBinding', record.name().localName(), record)

internalServerError = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'internalServerError'), internalServerError_)
Namespace.addCategoryObject('elementBinding', internalServerError.name().localName(), internalServerError)

recordsList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recordsList'), recordsList_)
Namespace.addCategoryObject('elementBinding', recordsList.name().localName(), recordsList)

nameservers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameservers'), nameservers_)
Namespace.addCategoryObject('elementBinding', nameservers.name().localName(), nameservers)

itemNotFound = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'itemNotFound'), itemNotFound_)
Namespace.addCategoryObject('elementBinding', itemNotFound.name().localName(), itemNotFound)

badRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'badRequest'), badRequest_)
Namespace.addCategoryObject('elementBinding', badRequest.name().localName(), badRequest)

asyncJobsStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'asyncJobsStatus'), asyncJobsStatus_)
Namespace.addCategoryObject('elementBinding', asyncJobsStatus.name().localName(), asyncJobsStatus)

subdomains = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subdomains'), subdomains_)
Namespace.addCategoryObject('elementBinding', subdomains.name().localName(), subdomains)

changes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'changes'), changes_)
Namespace.addCategoryObject('elementBinding', changes.name().localName(), changes)

overLimit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'overLimit'), overLimit_)
Namespace.addCategoryObject('elementBinding', overLimit.name().localName(), overLimit)

recordTypes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recordTypes'), recordTypes_)
Namespace.addCategoryObject('elementBinding', recordTypes.name().localName(), recordTypes)

dnsFault = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dnsFault'), dnsFault_)
Namespace.addCategoryObject('elementBinding', dnsFault.name().localName(), dnsFault)



dnsFault_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'details'), pyxb.binding.datatypes.string, scope=dnsFault_))

dnsFault_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), pyxb.binding.datatypes.string, scope=dnsFault_))
dnsFault_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(dnsFault_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(dnsFault_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=1L, max_occurs=1L)
    )
dnsFault_._ContentModel = pyxb.binding.content.ParticleModel(dnsFault_._GroupModel, min_occurs=1, max_occurs=1)


itemAlreadyExists_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(itemAlreadyExists_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(itemAlreadyExists_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=1L, max_occurs=1L)
    )
itemAlreadyExists_._ContentModel = pyxb.binding.content.ParticleModel(itemAlreadyExists_._GroupModel, min_occurs=1, max_occurs=1)



rdns_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recordsList'), recordsList_, scope=rdns_))

rdns_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), _atom.linkType, scope=rdns_))
rdns_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(rdns_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(rdns_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recordsList')), min_occurs=0L, max_occurs=1L)
    )
rdns_._ContentModel = pyxb.binding.content.ParticleModel(rdns_._GroupModel, min_occurs=1, max_occurs=1)



change_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'changeDetail'), changeDetail_, scope=change_))
change_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(change_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'changeDetail')), min_occurs=0L, max_occurs=None)
    )
change_._ContentModel = pyxb.binding.content.ParticleModel(change_._GroupModel, min_occurs=1, max_occurs=1)



domain_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contents'), pyxb.binding.datatypes.string, scope=domain_))

domain_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recordsList'), recordsList_, scope=domain_))

domain_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameservers'), nameservers_, scope=domain_))

domain_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subdomains'), subdomains_, scope=domain_))
domain_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(domain_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameservers')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(domain_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recordsList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(domain_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subdomains')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(domain_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contents')), min_occurs=0L, max_occurs=1)
    )
domain_._ContentModel = pyxb.binding.content.ParticleModel(domain_._GroupModel, min_occurs=1, max_occurs=1)


unauthorized_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(unauthorized_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(unauthorized_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=1L, max_occurs=1L)
    )
unauthorized_._ContentModel = pyxb.binding.content.ParticleModel(unauthorized_._GroupModel, min_occurs=1, max_occurs=1)



nameservers_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameserver'), nameserver, scope=nameservers_))
nameservers_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nameservers_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameserver')), min_occurs=0L, max_occurs=None)
    )
nameservers_._ContentModel = pyxb.binding.content.ParticleModel(nameservers_._GroupModel, min_occurs=1, max_occurs=1)



domains_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'domain'), domain_, scope=domains_))

domains_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), _atom.linkType, scope=domains_))
domains_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(domains_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'domain')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(domains_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link')), min_occurs=0L, max_occurs=2L)
    )
domains_._ContentModel = pyxb.binding.content.ParticleModel(domains_._GroupModel, min_occurs=1, max_occurs=1)



deleteFault_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'failedItems'), validationFaults, scope=deleteFault_))
deleteFault_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(deleteFault_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(deleteFault_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=1L, max_occurs=1L)
    )
deleteFault_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(deleteFault_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'failedItems')), min_occurs=1L, max_occurs=1L)
    )
deleteFault_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(deleteFault_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(deleteFault_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
deleteFault_._ContentModel = pyxb.binding.content.ParticleModel(deleteFault_._GroupModel, min_occurs=1, max_occurs=1)


serviceUnavailable_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(serviceUnavailable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(serviceUnavailable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=1L, max_occurs=1L)
    )
serviceUnavailable_._ContentModel = pyxb.binding.content.ParticleModel(serviceUnavailable_._GroupModel, min_occurs=1, max_occurs=1)



asyncResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), pyxb.binding.datatypes.anySimpleType, scope=asyncResponse_))

asyncResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'error'), dnsFault_, scope=asyncResponse_))

asyncResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'requestUrl'), pyxb.binding.datatypes.anyURI, scope=asyncResponse_))

asyncResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'callbackUrl'), pyxb.binding.datatypes.string, scope=asyncResponse_))

asyncResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'jobId'), pyxb.binding.datatypes.string, scope=asyncResponse_))

asyncResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'request'), pyxb.binding.datatypes.string, scope=asyncResponse_))

asyncResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'status'), asyncStatus, scope=asyncResponse_))

asyncResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'verb'), verb, scope=asyncResponse_))
asyncResponse_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(asyncResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'jobId')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(asyncResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'callbackUrl')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(asyncResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'status')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(asyncResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'requestUrl')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(asyncResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'verb')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(asyncResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'request')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(asyncResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(asyncResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'error')), min_occurs=0L, max_occurs=1L)
    )
asyncResponse_._ContentModel = pyxb.binding.content.ParticleModel(asyncResponse_._GroupModel, min_occurs=1, max_occurs=1)



validationFaults._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fault'), dnsFault_, scope=validationFaults))
validationFaults._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(validationFaults._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fault')), min_occurs=1, max_occurs=None)
    )
validationFaults._ContentModel = pyxb.binding.content.ParticleModel(validationFaults._GroupModel, min_occurs=1, max_occurs=1)



recordsList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), _atom.linkType, scope=recordsList_))

recordsList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'record'), record_, scope=recordsList_))
recordsList_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(recordsList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'record')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(recordsList_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link')), min_occurs=0L, max_occurs=2L)
    )
recordsList_._ContentModel = pyxb.binding.content.ParticleModel(recordsList_._GroupModel, min_occurs=1, max_occurs=1)



subdomains_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), _atom.linkType, scope=subdomains_))

subdomains_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'domain'), domain_, scope=subdomains_))
subdomains_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(subdomains_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'domain')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(subdomains_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link')), min_occurs=0L, max_occurs=2L)
    )
subdomains_._ContentModel = pyxb.binding.content.ParticleModel(subdomains_._GroupModel, min_occurs=1, max_occurs=1)


internalServerError_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(internalServerError_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(internalServerError_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=1L, max_occurs=1L)
    )
internalServerError_._ContentModel = pyxb.binding.content.ParticleModel(internalServerError_._GroupModel, min_occurs=1, max_occurs=1)



validationErrors._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'messages'), pyxb.binding.datatypes.string, scope=validationErrors))
validationErrors._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(validationErrors._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'messages')), min_occurs=1, max_occurs=None)
    )
validationErrors._ContentModel = pyxb.binding.content.ParticleModel(validationErrors._GroupModel, min_occurs=1, max_occurs=1)


itemNotFound_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(itemNotFound_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(itemNotFound_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=1L, max_occurs=1L)
    )
itemNotFound_._ContentModel = pyxb.binding.content.ParticleModel(itemNotFound_._GroupModel, min_occurs=1, max_occurs=1)



badRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'validationErrors'), validationErrors, scope=badRequest_))
badRequest_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(badRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(badRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=1L, max_occurs=1L)
    )
badRequest_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(badRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'validationErrors')), min_occurs=1L, max_occurs=1L)
    )
badRequest_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(badRequest_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(badRequest_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
badRequest_._ContentModel = pyxb.binding.content.ParticleModel(badRequest_._GroupModel, min_occurs=1, max_occurs=1)



asyncJobsStatus_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), _atom.linkType, scope=asyncJobsStatus_))

asyncJobsStatus_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'asyncResponse'), asyncResponse_, scope=asyncJobsStatus_))
asyncJobsStatus_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(asyncJobsStatus_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'asyncResponse')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(asyncJobsStatus_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link')), min_occurs=0L, max_occurs=2L)
    )
asyncJobsStatus_._ContentModel = pyxb.binding.content.ParticleModel(asyncJobsStatus_._GroupModel, min_occurs=1, max_occurs=1)



changes_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'change'), change_, scope=changes_))

changes_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link'), _atom.linkType, scope=changes_))
changes_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(changes_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'change')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(changes_._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom'), u'link')), min_occurs=0L, max_occurs=2L)
    )
changes_._ContentModel = pyxb.binding.content.ParticleModel(changes_._GroupModel, min_occurs=1, max_occurs=1)


overLimit_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(overLimit_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(overLimit_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'details')), min_occurs=1L, max_occurs=1L)
    )
overLimit_._ContentModel = pyxb.binding.content.ParticleModel(overLimit_._GroupModel, min_occurs=1, max_occurs=1)



recordTypes_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recordType'), recordType, scope=recordTypes_))
recordTypes_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(recordTypes_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recordType')), min_occurs=0L, max_occurs=None)
    )
recordTypes_._ContentModel = pyxb.binding.content.ParticleModel(recordTypes_._GroupModel, min_occurs=1, max_occurs=1)
