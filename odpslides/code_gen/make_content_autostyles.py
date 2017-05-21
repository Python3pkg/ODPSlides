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
content_style_name_lookupD = {} # index=style:name (e.g. "a123"), value=function name

def maybe_add_func_name_to_a_dict( elem, func_name ):
    target = force_to_tag( 'style:name' )
    value = elem.get(target, None)
    if value is not None:
        content_style_name_lookupD[value] = func_name

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
    maybe_add_func_name_to_a_dict( root, func_name )

    
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
        content_style_name_lookupD.clear()
    
        fname = r'D:\py_proj_2015\ODPSlides\odpslides\templates\ppt_all_layouts_%s.odp'%suffix
        odp = ODPFile( fname )
        
        py_file = os.path.join(here, suffix, 'content_auto_styles.py')
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
        
        fOut.write('\n\n# Use content_style_name_lookupD for access to function calls')
        fOut.write( '\n\ncontent_style_name_lookupD = {} # index=style name (e.g. "a123"), value=function name\n' )
        
        fOut.write('\n\n')
        
        # do style:presentation-page-layout
        
        for style in odp.content_auto_styles.getchildren():
            suffix = style.get( force_to_tag('style:family'), 'nofam' ) 
            if suffix == 'nofam':
                suffix = style.get( force_to_tag('style:name'), 'noname' )
            else:
                suffix = suffix + '_' + style.get( force_to_tag('style:name'), 'noname' )
                
            fOut.write( make_function_from_root( style, odp.content_xml_obj, suffix=suffix ).encode('utf-8') )
            
            print( odp.content_xml_obj.elem_tostring(style) )
            print('\n')


        fOut.write('\n\n# Set values in func_quick_lookupD\n')
        keyL = sorted( func_quick_lookupD.keys() )
        for key in keyL:
            fOut.write( 'func_quick_lookupD["%s"] = %s\n'%(key, func_quick_lookupD[key]) )

        fOut.write('\n\n')
        
        fOut.write('\n\n# Set values in content_style_name_lookupD\n')
        def int_part( s ):
            try:
                val = int(s[1:])
            except:
                val = 0
            return val
        keyL = sorted( list(content_style_name_lookupD.keys()), key=int_part )
        for key in keyL:
            fOut.write( 'content_style_name_lookupD["%s"] = %s\n'%(key, content_style_name_lookupD[key]) )
        
        
        fOut.write('''
if __name__ == "__main__":
    print( content_style_name_lookupD["a1160"]() )
''')
        
