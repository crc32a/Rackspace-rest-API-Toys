# ./atom.py
# PyXB bindings for NM:741a4e51acfa398449878d8690bb692b0b09b93a
# Generated 2012-08-14 20:55:59.184923 by PyXB version 1.1.3
# Namespace http://www.w3.org/2005/Atom [xmlns:atom]

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
import pyxb.binding.xml_

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


# Atomic SimpleTypeDefinition
class STD_ANON (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.text = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'text', tag=u'text')
STD_ANON.html = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'html', tag=u'html')
STD_ANON.xhtml = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'xhtml', tag=u'xhtml')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic SimpleTypeDefinition
class emailType (pyxb.binding.datatypes.normalizedString):

    """
                Schema definition for an email address.
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'emailType')
    _Documentation = u'\n                Schema definition for an email address.\n            '
emailType._CF_pattern = pyxb.binding.facets.CF_pattern()
emailType._CF_pattern.addPattern(pattern=u'\\w+@(\\w+\\.)+\\w+')
emailType._InitializeFacetMap(emailType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'emailType', emailType)

# Complex type textType with content type MIXED
class textType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'textType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_textType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_w3_org2005Atom_textType_type', STD_ANON)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_textType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __type.name() : __type,
        __base.name() : __base
    }
Namespace.addCategoryObject('typeBinding', u'textType', textType)


# Complex type linkType with content type MIXED
class linkType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'linkType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__httpwww_w3_org2005Atom_linkType_title', pyxb.binding.datatypes.string)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_linkType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_linkType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute rel uses Python identifier rel
    __rel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rel'), 'rel', '__httpwww_w3_org2005Atom_linkType_rel', pyxb.binding.datatypes.string)
    
    rel = property(__rel.value, __rel.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_w3_org2005Atom_linkType_type', pyxb.binding.datatypes.string)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'length'), 'length', '__httpwww_w3_org2005Atom_linkType_length', pyxb.binding.datatypes.positiveInteger)
    
    length = property(__length.value, __length.set, None, None)

    
    # Attribute hreflang uses Python identifier hreflang
    __hreflang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'hreflang'), 'hreflang', '__httpwww_w3_org2005Atom_linkType_hreflang', pyxb.binding.datatypes.NMTOKEN)
    
    hreflang = property(__hreflang.value, __hreflang.set, None, None)

    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'href'), 'href', '__httpwww_w3_org2005Atom_linkType_href', pyxb.binding.datatypes.anyURI, required=True)
    
    href = property(__href.value, __href.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))

    _ElementMap = {
        
    }
    _AttributeMap = {
        __title.name() : __title,
        __base.name() : __base,
        __lang.name() : __lang,
        __rel.name() : __rel,
        __type.name() : __type,
        __length.name() : __length,
        __hreflang.name() : __hreflang,
        __href.name() : __href
    }
Namespace.addCategoryObject('typeBinding', u'linkType', linkType)


# Complex type personType with content type ELEMENT_ONLY
class personType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'personType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'uri'), 'uri', '__httpwww_w3_org2005Atom_personType_httpwww_w3_org2005Atomuri', True)

    
    uri = property(__uri.value, __uri.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}email uses Python identifier email
    __email = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'email'), 'email', '__httpwww_w3_org2005Atom_personType_httpwww_w3_org2005Atomemail', True)

    
    email = property(__email.value, __email.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}name uses Python identifier name
    __name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_w3_org2005Atom_personType_httpwww_w3_org2005Atomname', True)

    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_personType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_personType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))
    _HasWildcardElement = True

    _ElementMap = {
        __uri.name() : __uri,
        __email.name() : __email,
        __name.name() : __name
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __base.name() : __base
    }
Namespace.addCategoryObject('typeBinding', u'personType', personType)


# Complex type feedType with content type ELEMENT_ONLY
class feedType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'feedType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}icon uses Python identifier icon
    __icon = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'icon'), 'icon', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomicon', True)

    
    icon = property(__icon.value, __icon.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}contributor uses Python identifier contributor
    __contributor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'contributor'), 'contributor', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomcontributor', True)

    
    contributor = property(__contributor.value, __contributor.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomentry', True)

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'link'), 'link', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}rights uses Python identifier rights
    __rights = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rights'), 'rights', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomrights', True)

    
    rights = property(__rights.value, __rights.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}logo uses Python identifier logo
    __logo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'logo'), 'logo', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomlogo', True)

    
    logo = property(__logo.value, __logo.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}updated uses Python identifier updated
    __updated = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'updated'), 'updated', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomupdated', True)

    
    updated = property(__updated.value, __updated.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}id uses Python identifier id
    __id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'id'), 'id', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomid', True)

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}generator uses Python identifier generator
    __generator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'generator'), 'generator', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomgenerator', True)

    
    generator = property(__generator.value, __generator.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}author uses Python identifier author
    __author = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'author'), 'author', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomauthor', True)

    
    author = property(__author.value, __author.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}subtitle uses Python identifier subtitle
    __subtitle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'subtitle'), 'subtitle', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomsubtitle', True)

    
    subtitle = property(__subtitle.value, __subtitle.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}category uses Python identifier category
    __category = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'category'), 'category', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomcategory', True)

    
    category = property(__category.value, __category.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}title uses Python identifier title
    __title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomtitle', True)

    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))
    _HasWildcardElement = True

    _ElementMap = {
        __icon.name() : __icon,
        __contributor.name() : __contributor,
        __entry.name() : __entry,
        __link.name() : __link,
        __rights.name() : __rights,
        __logo.name() : __logo,
        __updated.name() : __updated,
        __id.name() : __id,
        __generator.name() : __generator,
        __author.name() : __author,
        __subtitle.name() : __subtitle,
        __category.name() : __category,
        __title.name() : __title
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __base.name() : __base
    }
Namespace.addCategoryObject('typeBinding', u'feedType', feedType)


# Complex type sourceType with content type ELEMENT_ONLY
class sourceType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sourceType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'link'), 'link', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}subtitle uses Python identifier subtitle
    __subtitle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'subtitle'), 'subtitle', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomsubtitle', True)

    
    subtitle = property(__subtitle.value, __subtitle.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}icon uses Python identifier icon
    __icon = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'icon'), 'icon', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomicon', True)

    
    icon = property(__icon.value, __icon.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}title uses Python identifier title
    __title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomtitle', True)

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}rights uses Python identifier rights
    __rights = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rights'), 'rights', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomrights', True)

    
    rights = property(__rights.value, __rights.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}updated uses Python identifier updated
    __updated = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'updated'), 'updated', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomupdated', True)

    
    updated = property(__updated.value, __updated.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}author uses Python identifier author
    __author = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'author'), 'author', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomauthor', True)

    
    author = property(__author.value, __author.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}category uses Python identifier category
    __category = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'category'), 'category', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomcategory', True)

    
    category = property(__category.value, __category.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}generator uses Python identifier generator
    __generator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'generator'), 'generator', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomgenerator', True)

    
    generator = property(__generator.value, __generator.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}logo uses Python identifier logo
    __logo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'logo'), 'logo', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomlogo', True)

    
    logo = property(__logo.value, __logo.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}id uses Python identifier id
    __id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'id'), 'id', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomid', True)

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}contributor uses Python identifier contributor
    __contributor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'contributor'), 'contributor', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomcontributor', True)

    
    contributor = property(__contributor.value, __contributor.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))
    _HasWildcardElement = True

    _ElementMap = {
        __link.name() : __link,
        __subtitle.name() : __subtitle,
        __icon.name() : __icon,
        __title.name() : __title,
        __rights.name() : __rights,
        __updated.name() : __updated,
        __author.name() : __author,
        __category.name() : __category,
        __generator.name() : __generator,
        __logo.name() : __logo,
        __id.name() : __id,
        __contributor.name() : __contributor
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __base.name() : __base
    }
Namespace.addCategoryObject('typeBinding', u'sourceType', sourceType)


# Complex type dateTimeType with content type SIMPLE
class dateTimeType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.dateTime
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dateTimeType')
    # Base type is pyxb.binding.datatypes.dateTime
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_dateTimeType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_dateTimeType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))

    _ElementMap = {
        
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __base.name() : __base
    }
Namespace.addCategoryObject('typeBinding', u'dateTimeType', dateTimeType)


# Complex type categoryType with content type EMPTY
class categoryType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'categoryType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_categoryType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute term uses Python identifier term
    __term = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'term'), 'term', '__httpwww_w3_org2005Atom_categoryType_term', pyxb.binding.datatypes.string, required=True)
    
    term = property(__term.value, __term.set, None, None)

    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'label'), 'label', '__httpwww_w3_org2005Atom_categoryType_label', pyxb.binding.datatypes.string)
    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_categoryType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute scheme uses Python identifier scheme
    __scheme = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scheme'), 'scheme', '__httpwww_w3_org2005Atom_categoryType_scheme', pyxb.binding.datatypes.anyURI)
    
    scheme = property(__scheme.value, __scheme.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))

    _ElementMap = {
        
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __term.name() : __term,
        __label.name() : __label,
        __base.name() : __base,
        __scheme.name() : __scheme
    }
Namespace.addCategoryObject('typeBinding', u'categoryType', categoryType)


# Complex type uriType with content type SIMPLE
class uriType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'uriType')
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_uriType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_uriType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))

    _ElementMap = {
        
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __base.name() : __base
    }
Namespace.addCategoryObject('typeBinding', u'uriType', uriType)


# Complex type generatorType with content type SIMPLE
class generatorType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'generatorType')
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_w3_org2005Atom_generatorType_version', pyxb.binding.datatypes.string)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_generatorType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_generatorType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpwww_w3_org2005Atom_generatorType_uri', pyxb.binding.datatypes.anyURI)
    
    uri = property(__uri.value, __uri.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))

    _ElementMap = {
        
    }
    _AttributeMap = {
        __version.name() : __version,
        __base.name() : __base,
        __lang.name() : __lang,
        __uri.name() : __uri
    }
Namespace.addCategoryObject('typeBinding', u'generatorType', generatorType)


# Complex type iconType with content type SIMPLE
class iconType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'iconType')
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_iconType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_iconType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))

    _ElementMap = {
        
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __base.name() : __base
    }
Namespace.addCategoryObject('typeBinding', u'iconType', iconType)


# Complex type idType with content type SIMPLE
class idType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'idType')
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_idType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_idType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))

    _ElementMap = {
        
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __base.name() : __base
    }
Namespace.addCategoryObject('typeBinding', u'idType', idType)


# Complex type logoType with content type SIMPLE
class logoType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'logoType')
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_logoType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_logoType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))

    _ElementMap = {
        
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __base.name() : __base
    }
Namespace.addCategoryObject('typeBinding', u'logoType', logoType)


# Complex type entryType with content type ELEMENT_ONLY
class entryType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'entryType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}summary uses Python identifier summary
    __summary = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'summary'), 'summary', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomsummary', True)

    
    summary = property(__summary.value, __summary.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}content uses Python identifier content_
    __content = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'content'), 'content_', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomcontent', True)

    
    content_ = property(__content.value, __content.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}source uses Python identifier source
    __source = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'source'), 'source', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomsource', True)

    
    source = property(__source.value, __source.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}category uses Python identifier category
    __category = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'category'), 'category', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomcategory', True)

    
    category = property(__category.value, __category.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}published uses Python identifier published
    __published = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'published'), 'published', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atompublished', True)

    
    published = property(__published.value, __published.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}title uses Python identifier title
    __title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomtitle', True)

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}rights uses Python identifier rights
    __rights = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rights'), 'rights', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomrights', True)

    
    rights = property(__rights.value, __rights.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}contributor uses Python identifier contributor
    __contributor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'contributor'), 'contributor', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomcontributor', True)

    
    contributor = property(__contributor.value, __contributor.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'link'), 'link', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomlink', True)

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}author uses Python identifier author
    __author = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'author'), 'author', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomauthor', True)

    
    author = property(__author.value, __author.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}id uses Python identifier id
    __id = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'id'), 'id', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomid', True)

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}updated uses Python identifier updated
    __updated = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'updated'), 'updated', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomupdated', True)

    
    updated = property(__updated.value, __updated.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))
    _HasWildcardElement = True

    _ElementMap = {
        __summary.name() : __summary,
        __content.name() : __content,
        __source.name() : __source,
        __category.name() : __category,
        __published.name() : __published,
        __title.name() : __title,
        __rights.name() : __rights,
        __contributor.name() : __contributor,
        __link.name() : __link,
        __author.name() : __author,
        __id.name() : __id,
        __updated.name() : __updated
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __base.name() : __base
    }
Namespace.addCategoryObject('typeBinding', u'entryType', entryType)


# Complex type contentType with content type MIXED
class contentType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'contentType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute src uses Python identifier src
    __src = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'src'), 'src', '__httpwww_w3_org2005Atom_contentType_src', pyxb.binding.datatypes.anyURI)
    
    src = property(__src.value, __src.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_contentType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_contentType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_w3_org2005Atom_contentType_type', pyxb.binding.datatypes.string)
    
    type = property(__type.value, __type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom'))
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        __src.name() : __src,
        __base.name() : __base,
        __lang.name() : __lang,
        __type.name() : __type
    }
Namespace.addCategoryObject('typeBinding', u'contentType', contentType)


feed = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'feed'), feedType)
Namespace.addCategoryObject('elementBinding', feed.name().localName(), feed)

entry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), entryType)
Namespace.addCategoryObject('elementBinding', entry.name().localName(), entry)

link = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'), linkType)
Namespace.addCategoryObject('elementBinding', link.name().localName(), link)


textType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=set(['http://www.w3.org/1999/xhtml'])), min_occurs=0L, max_occurs=1)
    )
textType._ContentModel = pyxb.binding.content.ParticleModel(textType._GroupModel, min_occurs=1, max_occurs=1)


linkType._GroupModel = pyxb.binding.content.GroupSequence(
    
    )
linkType._ContentModel = pyxb.binding.content.ParticleModel(linkType._GroupModel, min_occurs=1, max_occurs=1)



personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'uri'), uriType, scope=personType))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'email'), emailType, scope=personType))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=personType))
personType._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'uri')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'email')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom')), min_occurs=1, max_occurs=1)
    )
personType._ContentModel = pyxb.binding.content.ParticleModel(personType._GroupModel, min_occurs=1L, max_occurs=None)



feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'icon'), iconType, scope=feedType))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contributor'), personType, scope=feedType))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), entryType, scope=feedType))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'), linkType, scope=feedType))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rights'), textType, scope=feedType))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'logo'), logoType, scope=feedType))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updated'), dateTimeType, scope=feedType))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'id'), idType, scope=feedType))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'generator'), generatorType, scope=feedType))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'author'), personType, scope=feedType))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subtitle'), textType, scope=feedType))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'category'), categoryType, scope=feedType))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), textType, scope=feedType))
feedType._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'author')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'category')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contributor')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'generator')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'icon')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'link')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'logo')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rights')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subtitle')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updated')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom')), min_occurs=0L, max_occurs=None)
    )
feedType._ContentModel = pyxb.binding.content.ParticleModel(feedType._GroupModel, min_occurs=3L, max_occurs=None)



sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'), linkType, scope=sourceType))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subtitle'), textType, scope=sourceType))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'icon'), iconType, scope=sourceType))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), textType, scope=sourceType))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rights'), textType, scope=sourceType))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updated'), dateTimeType, scope=sourceType))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'author'), personType, scope=sourceType))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'category'), categoryType, scope=sourceType))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'generator'), generatorType, scope=sourceType))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'logo'), logoType, scope=sourceType))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'id'), idType, scope=sourceType))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contributor'), personType, scope=sourceType))
sourceType._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'author')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'category')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contributor')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'generator')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'icon')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'link')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'logo')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rights')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subtitle')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updated')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom')), min_occurs=0L, max_occurs=None)
    )
sourceType._ContentModel = pyxb.binding.content.ParticleModel(sourceType._GroupModel, min_occurs=1, max_occurs=None)



entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'summary'), textType, scope=entryType))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'content'), contentType, scope=entryType))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'source'), textType, scope=entryType))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'category'), categoryType, scope=entryType))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'published'), dateTimeType, scope=entryType))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), textType, scope=entryType))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rights'), textType, scope=entryType))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contributor'), personType, scope=entryType))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'), linkType, scope=entryType))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'author'), personType, scope=entryType))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'id'), idType, scope=entryType))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updated'), dateTimeType, scope=entryType))
entryType._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'author')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'category')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'content')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contributor')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'link')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'published')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rights')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'source')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'summary')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updated')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom')), min_occurs=0L, max_occurs=None)
    )
entryType._ContentModel = pyxb.binding.content.ParticleModel(entryType._GroupModel, min_occurs=1, max_occurs=None)


contentType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/Atom')), min_occurs=0L, max_occurs=None)
    )
contentType._ContentModel = pyxb.binding.content.ParticleModel(contentType._GroupModel, min_occurs=1, max_occurs=1)
