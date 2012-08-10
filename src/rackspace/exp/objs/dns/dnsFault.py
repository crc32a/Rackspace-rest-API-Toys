# ./dnsFault.py
# PyXB bindings for NM:e04564f5701f8cd13e9a26295913518c59e63e81
# Generated 2012-08-10 11:25:43.431894 by PyXB version 1.1.3
# Namespace http://docs.openstack.org/common/api/v1.0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:082925d0-e308-11e1-ac11-002564955ea1')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.NamespaceForURI(u'http://docs.openstack.org/common/api/v1.0', create_if_missing=True)
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
class TimeUnit (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TimeUnit')
    _Documentation = u'\n                \n            '
TimeUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TimeUnit, enum_prefix=None)
TimeUnit.SECOND = TimeUnit._CF_enumeration.addEnumeration(unicode_value=u'SECOND', tag=u'SECOND')
TimeUnit.MINUTE = TimeUnit._CF_enumeration.addEnumeration(unicode_value=u'MINUTE', tag=u'MINUTE')
TimeUnit.HOUR = TimeUnit._CF_enumeration.addEnumeration(unicode_value=u'HOUR', tag=u'HOUR')
TimeUnit.DAY = TimeUnit._CF_enumeration.addEnumeration(unicode_value=u'DAY', tag=u'DAY')
TimeUnit._InitializeFacetMap(TimeUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TimeUnit', TimeUnit)

# Atomic SimpleTypeDefinition
class HttpMethod (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HttpMethod')
    _Documentation = u'\n                \n            '
HttpMethod._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HttpMethod, enum_prefix=None)
HttpMethod.GET = HttpMethod._CF_enumeration.addEnumeration(unicode_value=u'GET', tag=u'GET')
HttpMethod.DELETE = HttpMethod._CF_enumeration.addEnumeration(unicode_value=u'DELETE', tag=u'DELETE')
HttpMethod.POST = HttpMethod._CF_enumeration.addEnumeration(unicode_value=u'POST', tag=u'POST')
HttpMethod.PUT = HttpMethod._CF_enumeration.addEnumeration(unicode_value=u'PUT', tag=u'PUT')
HttpMethod.HEAD = HttpMethod._CF_enumeration.addEnumeration(unicode_value=u'HEAD', tag=u'HEAD')
HttpMethod.OPTIONS = HttpMethod._CF_enumeration.addEnumeration(unicode_value=u'OPTIONS', tag=u'OPTIONS')
HttpMethod.CONNECT = HttpMethod._CF_enumeration.addEnumeration(unicode_value=u'CONNECT', tag=u'CONNECT')
HttpMethod.TRACE = HttpMethod._CF_enumeration.addEnumeration(unicode_value=u'TRACE', tag=u'TRACE')
HttpMethod.ALL = HttpMethod._CF_enumeration.addEnumeration(unicode_value=u'ALL', tag=u'ALL')
HttpMethod._InitializeFacetMap(HttpMethod._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'HttpMethod', HttpMethod)

# Complex type RateLimit with content type ELEMENT_ONLY
class RateLimit (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RateLimit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__httpdocs_openstack_orgcommonapiv1_0_RateLimit_unit', TimeUnit, required=True)
    
    unit = property(__unit.value, __unit.set, None, u'\n                    \n                ')

    
    # Attribute remaining uses Python identifier remaining
    __remaining = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'remaining'), 'remaining', '__httpdocs_openstack_orgcommonapiv1_0_RateLimit_remaining', pyxb.binding.datatypes.int, required=True)
    
    remaining = property(__remaining.value, __remaining.set, None, u'\n                    \n                ')

    
    # Attribute verb uses Python identifier verb
    __verb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'verb'), 'verb', '__httpdocs_openstack_orgcommonapiv1_0_RateLimit_verb', HttpMethod, required=True)
    
    verb = property(__verb.value, __verb.set, None, u'\n                    \n                ')

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpdocs_openstack_orgcommonapiv1_0_RateLimit_value', pyxb.binding.datatypes.int, required=True)
    
    value_ = property(__value.value, __value.set, None, u'\n                    \n                ')

    
    # Attribute next-available uses Python identifier next_available
    __next_available = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'next-available'), 'next_available', '__httpdocs_openstack_orgcommonapiv1_0_RateLimit_next_available', pyxb.binding.datatypes.dateTime, required=True)
    
    next_available = property(__next_available.value, __next_available.set, None, u'\n                    \n                ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.openstack.org/common/api/v1.0'))
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        __unit.name() : __unit,
        __remaining.name() : __remaining,
        __verb.name() : __verb,
        __value.name() : __value,
        __next_available.name() : __next_available
    }
Namespace.addCategoryObject('typeBinding', u'RateLimit', RateLimit)


# Complex type ResourceRateLimits with content type ELEMENT_ONLY
class ResourceRateLimits (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ResourceRateLimits')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/common/api/v1.0}limit uses Python identifier limit
    __limit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'limit'), 'limit', '__httpdocs_openstack_orgcommonapiv1_0_ResourceRateLimits_httpdocs_openstack_orgcommonapiv1_0limit', True)

    
    limit = property(__limit.value, __limit.set, None, None)

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpdocs_openstack_orgcommonapiv1_0_ResourceRateLimits_uri', pyxb.binding.datatypes.string, required=True)
    
    uri = property(__uri.value, __uri.set, None, u'\n                    \n                ')

    
    # Attribute regex uses Python identifier regex
    __regex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'regex'), 'regex', '__httpdocs_openstack_orgcommonapiv1_0_ResourceRateLimits_regex', pyxb.binding.datatypes.string, required=True)
    
    regex = property(__regex.value, __regex.set, None, u'\n                    \n                ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.openstack.org/common/api/v1.0'))
    _HasWildcardElement = True

    _ElementMap = {
        __limit.name() : __limit
    }
    _AttributeMap = {
        __uri.name() : __uri,
        __regex.name() : __regex
    }
Namespace.addCategoryObject('typeBinding', u'ResourceRateLimits', ResourceRateLimits)


# Complex type AbsoluteLimit with content type ELEMENT_ONLY
class AbsoluteLimit (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AbsoluteLimit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpdocs_openstack_orgcommonapiv1_0_AbsoluteLimit_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'\n                    \n                ')

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpdocs_openstack_orgcommonapiv1_0_AbsoluteLimit_value', pyxb.binding.datatypes.int, required=True)
    
    value_ = property(__value.value, __value.set, None, u'\n                    \n                ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.openstack.org/common/api/v1.0'))
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        __name.name() : __name,
        __value.name() : __value
    }
Namespace.addCategoryObject('typeBinding', u'AbsoluteLimit', AbsoluteLimit)


# Complex type Limits with content type ELEMENT_ONLY
class Limits (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Limits')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/common/api/v1.0}rates uses Python identifier rates
    __rates = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rates'), 'rates', '__httpdocs_openstack_orgcommonapiv1_0_Limits_httpdocs_openstack_orgcommonapiv1_0rates', False)

    
    rates = property(__rates.value, __rates.set, None, None)

    
    # Element {http://docs.openstack.org/common/api/v1.0}absolute uses Python identifier absolute
    __absolute = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'absolute'), 'absolute', '__httpdocs_openstack_orgcommonapiv1_0_Limits_httpdocs_openstack_orgcommonapiv1_0absolute', False)

    
    absolute = property(__absolute.value, __absolute.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.openstack.org/common/api/v1.0'))
    _HasWildcardElement = True

    _ElementMap = {
        __rates.name() : __rates,
        __absolute.name() : __absolute
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Limits', Limits)


# Complex type RateLimitList with content type ELEMENT_ONLY
class RateLimitList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RateLimitList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/common/api/v1.0}rate uses Python identifier rate
    __rate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rate'), 'rate', '__httpdocs_openstack_orgcommonapiv1_0_RateLimitList_httpdocs_openstack_orgcommonapiv1_0rate', True)

    
    rate = property(__rate.value, __rate.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.openstack.org/common/api/v1.0'))
    _HasWildcardElement = True

    _ElementMap = {
        __rate.name() : __rate
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'RateLimitList', RateLimitList)


# Complex type AbsoluteLimitList with content type ELEMENT_ONLY
class AbsoluteLimitList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AbsoluteLimitList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.openstack.org/common/api/v1.0}limit uses Python identifier limit
    __limit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'limit'), 'limit', '__httpdocs_openstack_orgcommonapiv1_0_AbsoluteLimitList_httpdocs_openstack_orgcommonapiv1_0limit', True)

    
    limit = property(__limit.value, __limit.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.openstack.org/common/api/v1.0'))
    _HasWildcardElement = True

    _ElementMap = {
        __limit.name() : __limit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'AbsoluteLimitList', AbsoluteLimitList)


limits = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'limits'), Limits)
Namespace.addCategoryObject('elementBinding', limits.name().localName(), limits)


RateLimit._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.openstack.org/common/api/v1.0')), min_occurs=0L, max_occurs=None)
    )
RateLimit._ContentModel = pyxb.binding.content.ParticleModel(RateLimit._GroupModel, min_occurs=1, max_occurs=1)



ResourceRateLimits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'limit'), RateLimit, scope=ResourceRateLimits))
ResourceRateLimits._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ResourceRateLimits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'limit')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.openstack.org/common/api/v1.0')), min_occurs=0L, max_occurs=None)
    )
ResourceRateLimits._ContentModel = pyxb.binding.content.ParticleModel(ResourceRateLimits._GroupModel, min_occurs=1, max_occurs=1)


AbsoluteLimit._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.openstack.org/common/api/v1.0')), min_occurs=0L, max_occurs=None)
    )
AbsoluteLimit._ContentModel = pyxb.binding.content.ParticleModel(AbsoluteLimit._GroupModel, min_occurs=1, max_occurs=1)



Limits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rates'), RateLimitList, scope=Limits))

Limits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'absolute'), AbsoluteLimitList, scope=Limits))
Limits._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Limits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rates')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(Limits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'absolute')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.openstack.org/common/api/v1.0')), min_occurs=0L, max_occurs=None)
    )
Limits._ContentModel = pyxb.binding.content.ParticleModel(Limits._GroupModel, min_occurs=1, max_occurs=1)



RateLimitList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rate'), ResourceRateLimits, scope=RateLimitList))
RateLimitList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(RateLimitList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rate')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.openstack.org/common/api/v1.0')), min_occurs=0L, max_occurs=None)
    )
RateLimitList._ContentModel = pyxb.binding.content.ParticleModel(RateLimitList._GroupModel, min_occurs=1, max_occurs=1)



AbsoluteLimitList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'limit'), AbsoluteLimit, scope=AbsoluteLimitList))
AbsoluteLimitList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(AbsoluteLimitList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'limit')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.openstack.org/common/api/v1.0')), min_occurs=0L, max_occurs=None)
    )
AbsoluteLimitList._ContentModel = pyxb.binding.content.ParticleModel(AbsoluteLimitList._GroupModel, min_occurs=1, max_occurs=1)
