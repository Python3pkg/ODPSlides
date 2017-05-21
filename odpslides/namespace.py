# Support Python 2 and 3






def python_def_from_tag( tag ):
    """Make a legal function name from an element tag"""
    short = force_to_short( tag )
    short = short.replace(':','_8_')
    short = short.replace('-','_')
    short = short.replace(' ','_')
    short = short.replace(',','_')
    return short

def python_param_from_tag( tag ):
    """Make a legal function name from an element tag"""
    short = force_to_short( tag )
    sL = short.split(':')
    short = sL[-1]
    short = short.replace('-','_')
    short = short.replace(' ','_')
    short = short.replace(',','_')
    return short

def force_to_short( short_or_tag ):
    """force into tag format like: 'table:table' """
    
    # Just in case, eliminate any special/custom file prefix
    short_or_tag = short_or_tag.split('|')[-1]
    
    if short_or_tag.find('}') >= 0:
        sL = short_or_tag.split('}')
        s = sL[0][1:]
        if s in REV_ODF_NAMESPACES:
            short = REV_ODF_NAMESPACES[s] + ':' + sL[1]
        else:
            short = '...SHORT NAME ERROR...'
    else:
        short = short_or_tag
    return short


def force_to_tag( path_or_tag ):
    """force into tag format like: '{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table' """
    
    # Just in case, eliminate any special file prefix
    path_or_tag = path_or_tag.split('|')[-1]
    
    if path_or_tag.startswith('{'):
        return path_or_tag

    
    pathL = path_or_tag.split('/')
    ansL = []
    for path in pathL:
        
        sL = path.split(':')
        if len(sL)!=2:
            print('...ERROR... in force_to_tag: %s'%path_or_tag)
            return path_or_tag # bail out if any part is wrong

        tag_part = '{%s}%s'%( ODF_NAMESPACES[sL[0]], sL[1] )
        
        ansL.append( tag_part )
    return '/'.join( ansL )




ODF_NAMESPACES = {
    'anim': "urn:oasis:names:tc:opendocument:xmlns:animation:1.0",
    'chart': "urn:oasis:names:tc:opendocument:xmlns:chart:1.0",
    'config': "urn:oasis:names:tc:opendocument:xmlns:config:1.0",
    'dc': "http://purl.org/dc/elements/1.1/",
    'dom': "http://www.w3.org/2001/xml-events",
    'dr3d': "urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0",
    'draw': "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
    'fo': "urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
    'form': "urn:oasis:names:tc:opendocument:xmlns:form:1.0",
    'math': "http://www.w3.org/1998/Math/MathML",
    'meta': "urn:oasis:names:tc:opendocument:xmlns:meta:1.0",
    'number': "urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0",
    'of': "urn:oasis:names:tc:opendocument:xmlns:of:1.2",
    'office': "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    'ooo': "http://openoffice.org/2004/office",
    'oooc': "http://openoffice.org/2004/calc",
    'ooow': "http://openoffice.org/2004/writer",
    'presentation': "urn:oasis:names:tc:opendocument:xmlns:presentation:1.0",
    'rdfa': "http://docs.oasis-open.org/opendocument/meta/rdfa#",
    'rpt': "http://openoffice.org/2005/report",
    'script': "urn:oasis:names:tc:opendocument:xmlns:script:1.0",
    'smil': "urn:oasis:names:tc:opendocument:xmlns:smil-compatible:1.0",
    'style': "urn:oasis:names:tc:opendocument:xmlns:style:1.0",
    'svg': "urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0",
    'table': "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    'text': "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    'xforms': "http://www.w3.org/2002/xforms",
    'xlink': "http://www.w3.org/1999/xlink",
    'xsd': "http://www.w3.org/2001/XMLSchema",
    'xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'manifest': "urn:oasis:names:tc:opendocument:xmlns:manifest:1.0",
    'xml': 'http://www.w3.org/XML/1998/namespace',
    'msoxl': "http://schemas.microsoft.com/office/excel/formula"
}

# Create a reverse lookup as well
#   e.g. REV_ODF_NAMESPACES["urn:oasis:names:tc:opendocument:xmlns:drawing:1.0"] == "draw"
REV_ODF_NAMESPACES = {}
for key,val in list(ODF_NAMESPACES.items()):
    REV_ODF_NAMESPACES[val] = key

XMLNS_STR = ' '.join( ['xmlns:%s="%s"'%(sh,tag) for sh,tag in list(ODF_NAMESPACES.items())] )

if __name__ == "__main__":
    
    from odpslides.template_xml_file import TemplateXML_File
    import sys
    
    

    #sys.exit()
    TFile = TemplateXML_File(r'D:\temp\open_office\content.xml')
    #TFile = TemplateXML_File(r'D:\temp\open_office_v2\GN2_Press\content.xml')
    for key,val in list(TFile.rev_nsOD.items()):
        if key not in ODF_NAMESPACES:
            print( '%s not in ODF_NAMESPACES'%key )
    
    root = TFile.root
    short_pathD = TFile.short_pathD
    depthD = TFile.depthD
    print('root = %s at depth = %i'%(short_pathD[root], depthD[root]))
    for n in range(1, TFile.max_depth):
        print()
        for parent in root.iter():
            if depthD[parent] == n:
                short_path = short_pathD[parent]
                sL = short_path.split('/')
                print('parent = %s at depth = %i'%(sL[-1], depthD[parent]))
    
    