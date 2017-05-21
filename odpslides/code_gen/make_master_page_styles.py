# Support Python 2 and 3




import sys, os
from collections import OrderedDict

if sys.version_info < (3,):
    import odpslides.ElementTree_27OD as ET
else:
    import odpslides.ElementTree_34OD as ET
from odpslides.find_obj import find_elem_w_attrib, NS_attrib, NS

from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag
from odpslides.namespace import python_param_from_tag, python_def_from_tag

func_quick_lookupD = {} # index=suffix name, value=function name

# index=layout name (e.g. "Master1-PPL24"), value=master name (e.g. "Master1-Layout24-tbl-Title-and-Table")
master_page_name_lookupD = {} 
layout_page_name_lookupD = {}


# Set values in master_page_name_lookupD
master_page_name_lookupD["Master1-PPL1"] = "Master1-Layout1-title-Title-Slide"
master_page_name_lookupD["Master1-PPL12"] = "Master1-Layout12-tx-Title-and-Text"
master_page_name_lookupD["Master1-PPL13"] = "Master1-Layout13-twoColTx-Title-and-2-Column-Text"
master_page_name_lookupD["Master1-PPL14"] = "Master1-Layout14-txOverObj-Title-and-Text-over-Content"
master_page_name_lookupD["Master1-PPL15"] = "Master1-Layout15-txAndObj-Title,-Text,-and-Content"
master_page_name_lookupD["Master1-PPL16"] = "Master1-Layout16-objAndTx-Title,-Content-and-Text"
master_page_name_lookupD["Master1-PPL17"] = "Master1-Layout17-txAndTwoObj-Title,-Text,-and-2-Content"
master_page_name_lookupD["Master1-PPL18"] = "Master1-Layout18-objAndTwoObj-Title,-Content,-and-2-Content"
master_page_name_lookupD["Master1-PPL19"] = "Master1-Layout19-objOverTx-Title-and-Content-over-Text"
master_page_name_lookupD["Master1-PPL2"] = "Master1-Layout2-obj-Title-and-Content"
master_page_name_lookupD["Master1-PPL20"] = "Master1-Layout20-fourObj-Title-and-4-Content"
master_page_name_lookupD["Master1-PPL21"] = "Master1-Layout21-twoObjAndObj-Title,-2-Content-and-Content"
master_page_name_lookupD["Master1-PPL22"] = "Master1-Layout22-twoObjAndTx-Title,-2-Content-and-Text"
master_page_name_lookupD["Master1-PPL23"] = "Master1-Layout23-twoObjOverTx-Title-and-2-Content-over-Text"
master_page_name_lookupD["Master1-PPL24"] = "Master1-Layout24-tbl-Title-and-Table"
master_page_name_lookupD["Master1-PPL4"] = "Master1-Layout4-twoObj-Two-Content"


# Set values in layout_page_name_lookupD
layout_page_name_lookupD["Master1-Layout1-title-Title-Slide"] = "Master1-PPL1"
layout_page_name_lookupD["Master1-Layout12-tx-Title-and-Text"] = "Master1-PPL12"
layout_page_name_lookupD["Master1-Layout13-twoColTx-Title-and-2-Column-Text"] = "Master1-PPL13"
layout_page_name_lookupD["Master1-Layout14-txOverObj-Title-and-Text-over-Content"] = "Master1-PPL14"
layout_page_name_lookupD["Master1-Layout15-txAndObj-Title,-Text,-and-Content"] = "Master1-PPL15"
layout_page_name_lookupD["Master1-Layout16-objAndTx-Title,-Content-and-Text"] = "Master1-PPL16"
layout_page_name_lookupD["Master1-Layout17-txAndTwoObj-Title,-Text,-and-2-Content"] = "Master1-PPL17"
layout_page_name_lookupD["Master1-Layout18-objAndTwoObj-Title,-Content,-and-2-Content"] = "Master1-PPL18"
layout_page_name_lookupD["Master1-Layout19-objOverTx-Title-and-Content-over-Text"] = "Master1-PPL19"
layout_page_name_lookupD["Master1-Layout2-obj-Title-and-Content"] = "Master1-PPL2"
layout_page_name_lookupD["Master1-Layout20-fourObj-Title-and-4-Content"] = "Master1-PPL20"
layout_page_name_lookupD["Master1-Layout21-twoObjAndObj-Title,-2-Content-and-Content"] = "Master1-PPL21"
layout_page_name_lookupD["Master1-Layout22-twoObjAndTx-Title,-2-Content-and-Text"] = "Master1-PPL22"
layout_page_name_lookupD["Master1-Layout23-twoObjOverTx-Title-and-2-Content-over-Text"] = "Master1-PPL23"
layout_page_name_lookupD["Master1-Layout24-tbl-Title-and-Table"] = "Master1-PPL24"
layout_page_name_lookupD["Master1-Layout4-twoObj-Two-Content"] = "Master1-PPL4"

def fix_utf8( s ):
    cL = []
    #s = s.encode('utf-8')
    for c in s:
        if ord(c) >= 128:
            cL.append( '\\x%X'%ord(c) )
        else:
            cL.append( c )
    return ''.join(cL)

def make_function_from_root( root, tmplt_obj, suffix='' ):
    """build python source to make the Elements from scratch"""
    
    suffix = suffix.replace(',','_')
    if suffix in func_quick_lookupD:
        n = 2
        while '%s_%i'%(suffix, n) in func_quick_lookupD:
            n += 1
        suffix = '%s_%i'%(suffix, n)
    
    func_name = python_def_from_tag(root.tag)
    if suffix:
        func_name = func_name + '_%s'%python_def_from_tag(suffix)
        
        # Used after code is generated
        func_quick_lookupD[suffix] = func_name
    else:
        # Used after code is generated
        func_quick_lookupD[func_name] = func_name
    
    
    keyL = sorted( root.keys() )
    
    sL = ['def %s():'%(func_name, )]
    sL.append( '    ' )
    doc_str = 'Build Element %s'%force_to_short(root.tag)
    if suffix:
        doc_str = doc_str + ' for %s'%suffix
    sL.append( '''    """%s """'''%doc_str )
    sL.append( '    ' )
    
    sOut = tmplt_obj.elem_tostring(root, include_ns=False, use_linebreaks=True )
    sOut = fix_utf8( sOut )
    sL.append( '''    elem = build_element( """%s""" )'''%sOut )
    
    
    sL.append( '    ' )
    sL.append( '    return elem\n\n' )
    
    return '\n'.join(sL)

if __name__ == "__main__":

    from odpslides.odp_file import ODPFile
    
    here = os.path.abspath(os.path.dirname(__file__))
    
    for suffix in ['image', 'grad', 'plain', 'solidbg']:
    #for suffix in ['plain']:
        func_quick_lookupD.clear() # need to empty dict
    
        fname = r'D:\py_proj_2015\ODPSlides\odpslides\templates\ppt_all_layouts_%s.odp'%suffix
        odp = ODPFile( fname )
        
        py_file = os.path.join(here, suffix, 'styles_master_pages.py')
        print('Opening:',py_file)
        fOut = open( py_file, 'w' )
        
        fOut.write( '''
# Python 2 and 3
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
        
"""Code Generated to build style:presentation-page-layout objects for odp files"""

import sys, os
from collections import OrderedDict

from odpslides.template_xml_file import TemplateXML_File
from odpslides.namespace import XMLNS_STR

def build_element( s ):
    """Add namespace to string and use TemplateXML_File to make Element"""
    s = s.replace(' ',' %s '%XMLNS_STR, 1) # First space ONLY
    return TemplateXML_File( s ).root
                
''' )
        fOut.write('\n\n# Use func_quick_lookupD for access to function calls')
        fOut.write( '\n\nfunc_quick_lookupD = {} # index=suffix name, value=function name\n' )
        
        
        fOut.write('\n\n')
        
        # do style:presentation-page-layout
        
        for style in odp.office_master_styles_elem.getchildren():
            draw_name = style.get( force_to_tag('draw:style-name'), 'nodraw' ) # e.g. "a0"
            style_name = style.get( force_to_tag('style:name'), '' ) # e.g. "Master1-Layout1-title-Title-Slide"
            
            if style_name in layout_page_name_lookupD:
                suffix = layout_page_name_lookupD[style_name]
                fOut.write( make_function_from_root( style, odp.styles_xml_obj, suffix=suffix ).encode('utf-8') )
            else:
                if draw_name == 'nodraw':
                    suffix = style_name
                    fOut.write( make_function_from_root( style, odp.styles_xml_obj, suffix=suffix ).encode('utf-8') )


        fOut.write('\n\n# Set values in func_quick_lookupD\n')
        keyL = sorted( func_quick_lookupD.keys() )
        for key in keyL:
            fOut.write( 'func_quick_lookupD["%s"] = %s\n'%(key, func_quick_lookupD[key]) )

        fOut.write('\n\n')
        
        
        fOut.write('''
if __name__ == "__main__":
    print( func_quick_lookupD["Master1-PPL24"]() )
''')
        
