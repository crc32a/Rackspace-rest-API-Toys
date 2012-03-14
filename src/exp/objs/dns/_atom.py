# ./_atom.py
# PyXB bindings for NM:741a4e51acfa398449878d8690bb692b0b09b93a
# Generated 2012-04-03 13:47:40.922434 by PyXB version 1.1.3
# Namespace http://www.w3.org/2005/Atom [xmlns:atom]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:7da26872-7dbd-11e1-9372-002564955ea1')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/Atom', create_if_missing=True)
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


# Complex type linkType with content type MIXED
class linkType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'linkType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute hreflang uses Python identifier hreflang
    __hreflang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'hreflang'), 'hreflang', '__httpwww_w3_org2005Atom_linkType_hreflang', pyxb.binding.datatypes.NMTOKEN)
    
    hreflang = property(__hreflang.value, __hreflang.set, None, None)

    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'href'), 'href', '__httpwww_w3_org2005Atom_linkType_href', pyxb.binding.datatypes.anyURI, required=True)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute rel uses Python identifier rel
    __rel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rel'), 'rel', '__httpwww_w3_org2005Atom_linkType_rel', pyxb.binding.datatypes.string)
    
    rel = property(__rel.value, __rel.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_w3_org2005Atom_linkType_type', pyxb.binding.datatypes.string)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__httpwww_w3_org2005Atom_linkType_title', pyxb.binding.datatypes.string)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'length'), 'length', '__httpwww_w3_org2005Atom_linkType_length', pyxb.binding.datatypes.positiveInteger)
    
    length = property(__length.value, __length.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __hreflang.name() : __hreflang,
        __href.name() : __href,
        __rel.name() : __rel,
        __type.name() : __type,
        __title.name() : __title,
        __length.name() : __length
    }
Namespace.addCategoryObject('typeBinding', u'linkType', linkType)


link = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'), linkType)
Namespace.addCategoryObject('elementBinding', link.name().localName(), link)


linkType._GroupModel = pyxb.binding.content.GroupSequence(
    
    )
linkType._ContentModel = pyxb.binding.content.ParticleModel(linkType._GroupModel, min_occurs=1, max_occurs=1)
