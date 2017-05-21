# Python 2 and 3




import sys
from collections import OrderedDict
import io

if sys.version_info < (3,):
    import odpslides.ElementTree_27OD as ET
else:
    import odpslides.ElementTree_34OD as ET

# get StringIO for either python 2.x or 3.x
try:
    from io import StringIO
except ImportError:
    from io import StringIO

import re
from copy import deepcopy
from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag

header_re = re.compile( '\<\?.*\?\>', flags=re.MULTILINE | re.UNICODE )

class TemplateXML_File(object):

    def __init__(self, xml_file_name_or_src):
        """
        Read and parse xml file using modified version of standard python
        xml.etree.ElementTree.

        xml_file_name_or_src can be a file name like: "content.xml" OR
        can be xml source.
        """
        #xml_file_name_or_src = xml_file_name_or_src.decode('utf-8')
        
        if xml_file_name_or_src.endswith('.xml') and len(xml_file_name_or_src)<256:
            self.xml_file_name_or_src = xml_file_name_or_src

            fInp = io.open(xml_file_name_or_src, 'rt', encoding='utf-8')
            xml_src = fInp.read()
            fInp.close()
        else:
            self.xml_file_name_or_src = None
            xml_src = xml_file_name_or_src

        self.xml_header = '' # Assume no header unless found at head of file
        match = header_re.match(xml_src)
        if match:
            #print( 'Found XML Header: ' + match.group(0) )
            self.xml_header = match.group(0) # will need \n when serialized

        # ns entries like: ('urn:oasis:names:tc:opendocument:xmlns:table:1.0', u'table')
        self.nsOD = OrderedDict()

        # rev_ns entries like: (u'table', 'urn:oasis:names:tc:opendocument:xmlns:table:1.0')
        self.rev_nsOD = OrderedDict()

        # qname entries like: ('{urn:oasis:names:tc:opendocument:xmlns:office:1.0}document-content', u'office:document-content')
        self.qnameOD = OrderedDict()

        events = ("start", "end", "start-ns", "end-ns")
        context = ET.iterparse(StringIO(xml_src), events=events)

        for event, elem in context:
            if event=="start":
                #print('elem.tag =', elem.tag)
                #print('type elem.tag =', type(elem.tag))
                #print('     type("}") =',type("}"))
                sL = elem.tag.split('}')
                if len(sL) == 2:
                    name = sL[1]
                    uri = sL[0][1:]
                    self.qnameOD[elem.tag] = '%s:%s'%(self.nsOD[uri], name)

                for qname,v in list(elem.attrib.items()):
                    sL = qname.split('}')
                    if len(sL) == 2:
                        name = sL[1]
                        uri = sL[0][1:]
                        self.qnameOD[qname] = '%s:%s'%(self.nsOD[uri], name)
            if event=="start-ns":
                self.nsOD[elem[1]] = elem[0]     # like: ('urn:oasis:names:tc:opendocument:xmlns:table:1.0', u'table')
                self.rev_nsOD[elem[0]] = elem[1] # like: (u'table', 'urn:oasis:names:tc:opendocument:xmlns:table:1.0')

        self.context = context
        #self.root = ET.ElementTree( context.root )
        self.root = context.root

        self.parentD = {} # index=child Element object, value=parent Element object
        self.depthD = {}  # index=Element object, value = depth in xml tree
        self.original_posD = {}  # index=Element object, value=tuple of child position (e.g. (0,3,1))
        self.get_elem_from_orig_posD = {}  # reverse lookup of "original_posD"
        
        self.max_depth = 0
        self.short_pathD = {} # index=Element, value = short name (like: "ns0:name1/ns1:xyz/ns3:abc")
        # After building tree, create self.parentD for all Elements
        self.parentD[self.root] = None
        self.depthD[self.root] = 0
        self.short_pathD[self.root] = self.qnameOD[ self.root.tag ] # no calc req'd... just = qname
        
        self.original_posD[self.root] = (0,) # tuple of position

        temp_short_path_counterD = {} # just used here to help count occurances of short path
        self.short_path_counterD = {} # index=Element, value=short path counter value
        self.short_path_parent_counterD = {} #  index=Element, value=parent's short path counter value
        self.short_path_counterD[self.root] = 1 # 1st (and only) occurance
        self.short_path_parent_counterD[self.root] = 1 # 1st (and only) occurance

        for parent in self.root.iter():
            try:
                for ichild, child in enumerate(parent.getchildren()):
                    self.parentD[child] = parent
                    self.depthD[child] = self.depthD[parent] + 1
                    self.max_depth = max(self.max_depth, self.depthD[child])
                    
                    L = list(self.original_posD[parent])
                    L.append( ichild )
                    self.original_posD[child] = tuple( L )

                    short_path = self.get_short_path( child )
                    self.short_pathD[child] = short_path

                    temp_short_path_counterD[(parent,short_path)] = temp_short_path_counterD.get((parent,short_path), 0) + 1
                    self.short_path_counterD[child] = '%s,%s'%(self.short_path_counterD[parent],
                                                       temp_short_path_counterD[(parent,short_path)])
                    self.short_path_parent_counterD[child] = '%s'%self.short_path_counterD[parent]

            except:
                print( 'NOTICE: No children for:', parent )
                
        for key,item in list(self.original_posD.items()):
            self.get_elem_from_orig_posD[item] = key # get elem from original_posD
            
            
        # set up dictionaries to hold style:name info (if init_all_annn_style8name)
        self.annn_style8nameD = {} # index=style:name ("a123"), value=style elem
        self.style_refD = {} # index=xxxxx:style-name (e.g. "a123"), value=elem with ref (not style itself)
        self.id_draw8idD = {} # index=draw:id (e.g. "id123"), value=elem
        

    def get_short_path(self, elem):

        sL = [ self.qnameOD[ elem.tag ] ]
        while self.parentD[elem] is not None:
            elem = self.parentD[elem]
            sL.append( self.qnameOD[ elem.tag ] )
        sL.reverse()
        return "/".join(sL)

    def getroot(self):
        return self.root

    def getparent(self, child):
        return self.parentD[child]
        
    def get_elements_orig_pos(self, elem):
        return self.original_posD[ elem ]
        
    def get_elem_at_original_pos(self, pos):
        return self.get_elem_from_orig_posD[pos]
        
    def remove_original_pos(self, pos):
        elem = self.get_elem_from_orig_posD[pos]
        parent = self.getparent(elem)
        self.remove_child( elem, parent )

    def remove_child(self, child, parent):
        parent.remove( child )
        del self.parentD[child]  # child still in memory, just not  in dict

    def add_child(self, child, parent):
        self.parentD[child] = parent
        parent.append( child )

    def add_children(self, childrenL, parent):
        for child in childrenL:
            self.add_child( child, parent )

    def tostring(self):
            
        xml_dataL = []
        if self.xml_header:
            xml_dataL = [self.xml_header + '\n']

        class dummy:
            pass
            def write(self, sInp ):
                if sys.version_info < (3,):
                    sInp = sInp.decode('utf-8')
                xml_dataL.append(sInp )
        dummy_file = dummy()
        #dummy_file.write = xml_dataL.append

        # There are differences between the python2 and python3 serialize routines
        if sys.version_info < (3,):
            ET._serialize_xml(dummy_file.write, self.root, "utf-8", self.qnameOD, self.nsOD)
        else:
            short_empty_elements = True # use short format for empty elements
            ET._serialize_xml(dummy_file.write, self.root, self.qnameOD, self.nsOD, short_empty_elements)

        sOut = "".join(xml_dataL)
        return sOut.encode('utf-8')

    def elem_tostring(self, elem, include_ns=False, use_linebreaks=True, include_header=False):
            
        xml_dataL = []
        
        class dummy:
            
            def write(self, sInp ):
                
                if sys.version_info < (3,):
                    sInp = sInp.decode('utf-8')
                if sInp.strip().startswith('xmlns:') and not include_ns:
                    return
                if sInp.strip().endswith('>') and use_linebreaks:
                    sInp = sInp.replace('>','>\n')
                    
                xml_dataL.append(sInp )
                dummy_file = dummy()
                #dummy_file.write = xml_dataL.append

        dummy_file = dummy()

        # There are differences between the python2 and python3 serialize routines
        if sys.version_info < (3,):
            ET._serialize_xml(dummy_file.write, elem, "utf-8", self.qnameOD, self.nsOD)
        else:
            short_empty_elements = True # use short format for empty elements
            ET._serialize_xml(dummy_file.write, elem, self.qnameOD, self.nsOD, short_empty_elements)

        sOut = "".join(xml_dataL)
        sOut = sOut.encode('utf-8')
        if include_header and self.xml_header:
            sOut = self.xml_header + '\n' + sOut
        
        return sOut

    def write(self, out_file_name):
        #fOut = open(out_file_name, "w")
        fOut = io.open(out_file_name, 'wt', encoding='utf-8')
        fOut.write( self.tostring() )
        fOut.close()


    def find(self, path, elem_obj=None):
        """Find Element within root OR elem_obj.
           path format is: 'office:body/office:spreadsheet'
        """
        if elem_obj is not None:
            return elem_obj.find( path, self.rev_nsOD )
        else:
            return self.root.find( path, self.rev_nsOD )

    def findall(self, path, elem_obj=None):
        """Find All Element objects within root OR elem_obj.
           path format is: 'office:body/office:spreadsheet'
        """
        if elem_obj:
            return elem_obj.findall( path, self.rev_nsOD )
        else:
            return self.root.findall( path, self.rev_nsOD )


    def NS(self, path_or_tag ):
        """force into tag format like: '{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table' """
        if path_or_tag.startswith('{'):
            return path_or_tag

        sL = path_or_tag.split(':')
        if len(sL)!=2:
            return path_or_tag

        return '{%s}%s'%( self.rev_nsOD[sL[0]], sL[1] )

    def NS_attrib(self, attD ):
        D = OrderedDict()
        for key,val in list(attD.items()):
            D[ self.NS(key) ] = val
        return D

    def acclimate_new_elem(self, my_new_elem):
        """
        Make sure qnameOD is up to date for my_new_elem
        """

        sL = my_new_elem.tag.split('}')
        if len(sL) == 2:
            name = sL[1]
            uri = sL[0][1:]
            self.qnameOD[my_new_elem.tag] = '%s:%s'%(self.nsOD[uri], name)

        for qname,v in list(my_new_elem.attrib.items()):
            sL = qname.split('}')
            if len(sL) == 2:
                name = sL[1]
                uri = sL[0][1:]
                self.qnameOD[qname] = '%s:%s'%(self.nsOD[uri], name)
                
        for child in my_new_elem.getchildren():
            self.acclimate_new_elem( child )

    def new_elem(self, name, attribOD=None):
        """
        Create a new Element object.
        name format can be 'table:table' OR '{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table'
        (i.e. can be path format OR tag format)
        attribOD is an OrderedDict in order to preserve attribute order.
        """

        tag = self.NS( name )
        #print( 'tag =',tag )


        if attribOD:
            OD = self.NS_attrib( attribOD )
            my_new_elem = ET.Element(tag, attrib=OD)
        else:
            my_new_elem = ET.Element(tag)

        sL = my_new_elem.tag.split('}')
        if len(sL) == 2:
            name = sL[1]
            uri = sL[0][1:]
            self.qnameOD[my_new_elem.tag] = '%s:%s'%(self.nsOD[uri], name)

        for qname,v in list(my_new_elem.attrib.items()):
            sL = qname.split('}')
            if len(sL) == 2:
                name = sL[1]
                uri = sL[0][1:]
                self.qnameOD[qname] = '%s:%s'%(self.nsOD[uri], name)

        return my_new_elem

    def init_all_annn_style8name(self):
        
        STYLE_NAME_ATTR = force_to_tag( 'style:name' )
        DRAW_ID_ATTR = force_to_tag( 'draw:id' )
        
        # reset in case called twice
        self.annn_style8nameD = {} # index=style:name ("a123"), value=elem
        self.style_refD = {} # index=xxxxx:style-name (e.g. "a123"), value=elem
        self.id_draw8idD = {} # index=draw:id (e.g. "id123"), value=elem

        for elem in self.root.iter():
            att_val = elem.get(STYLE_NAME_ATTR, '')
            if att_val.startswith('a'):
                if att_val in self.annn_style8nameD:
                    print('...ERROR... More than one definition for:', att_val)
                    self.annn_style8nameD[ att_val ] = [ self.annn_style8nameD[ att_val ] ]
                    self.annn_style8nameD[ att_val ].append( elem )
                else:
                    self.annn_style8nameD[ att_val ] = elem

            for aname, aval in list(elem.items()):
                if aname.endswith( '}style-name' ):
                    if aval in self.style_refD:
                        self.style_refD[ aval ] = [ self.style_refD[ aval ] ]
                        self.style_refD[ aval ].append( elem )
                    else:
                        self.style_refD[ aval ] = elem
                        
            att_val = elem.get(DRAW_ID_ATTR, '')
            if att_val.startswith('id'):
                if att_val in self.id_draw8idD:
                    print('...ERROR... More than one definition for:', att_val)
                    self.id_draw8idD[ att_val ] = [ self.id_draw8idD[ att_val ] ]
                    self.id_draw8idD[ att_val ].append( elem )
                else:
                    self.id_draw8idD[ att_val ] = elem
                

        self.max_annn_def = -1
        self.min_annn_def = 9999999999
        for annn in list(self.annn_style8nameD.keys()):
            self.max_annn_def = max( self.max_annn_def, int(annn[1:]) )
            self.min_annn_def = min( self.min_annn_def, int(annn[1:]) )
        #print('min_annn_def self.annn_style8nameD = ', self.min_annn_def)
        #print('max_annn_def self.annn_style8nameD = ', self.max_annn_def)


        self.max_annn_used = -1
        self.min_annn_used = 9999999999
        for annn in list(self.style_refD.keys()):
            self.max_annn_used = max( self.max_annn_used, int(annn[1:]) )
            self.min_annn_used = min( self.min_annn_used, int(annn[1:]) )
        #print('min_annn_used self.annn_style8nameD = ', self.min_annn_used)
        #print('max_annn_used self.annn_style8nameD = ', self.max_annn_used)


        self.max_idnnn_def = -1
        self.min_idnnn_def = 9999999999
        for idnnn in list(self.id_draw8idD.keys()):
            self.max_idnnn_def = max( self.max_idnnn_def, int(idnnn[2:]) )
            self.min_idnnn_def = min( self.min_idnnn_def, int(idnnn[2:]) )
        #print('min_idnnn_def self.id_draw8idD = ', self.min_idnnn_def)
        #print('max_idnnn_def self.id_draw8idD = ', self.max_idnnn_def)


    def set_all_attr_of_tag(self, tag, attr_name, attr_val):
        
        # force tag and attr_name to long version 
        tag = force_to_tag( tag )
        attr_name = force_to_tag( attr_name )
        
        for elem in self.root.iter():
            if elem.tag == tag:
                elem.set( attr_name, attr_val )
            

    def set_all_styles_of_tag_w_attr(self, targ_tag, targ_attr_name, targ_attr_val,
                                         style_attr_name, style_attr_val):
        """
        dictionaries  hold style:name info (if init_all_annn_style8name)
        self.annn_style8nameD = {} # index=style:name ("a123"), value=elem
        self.style_refD = {} # index=xxxxx:style-name (e.g. "a123"), value=elem
        """
        targ_tag = force_to_tag( targ_tag )
        targ_attr_name = force_to_tag( targ_attr_name )
        style_attr_name = force_to_tag( style_attr_name )

        for elem in self.root.iter():
            # for example a 'draw:frame' with an attribute 'presentation:class' == "page-number",
            if (elem.tag == targ_tag) and (elem.get(targ_attr_name,'') == targ_attr_val):
                
                # looking for a style element attribute (e.g. an attrib value like "a123")
                for sub_elem in elem.iter():
                    # looking for, for example text:style-name="a28"
                    for attname, attval in list(sub_elem.items()):
                        if (attval in self.style_refD)  and (attval in self.annn_style8nameD):
                            style_elem = self.annn_style8nameD[attval]
                            
                            # now look for the desired style attribute to set (e.g. 'fo:color' = '#000000')
                            for sub_style_elem in style_elem.iter():
                                if sub_style_elem.get(style_attr_name,''):
                                    sub_style_elem.set(style_attr_name, style_attr_val)

    def set_span_text_of_tag_w_attr(self, targ_tag, targ_attr_name, targ_attr_val,
                                         span_text=''):
        """
        dictionaries  hold style:name info (if init_all_annn_style8name)
        self.annn_style8nameD = {} # index=style:name ("a123"), value=elem
        self.style_refD = {} # index=xxxxx:style-name (e.g. "a123"), value=elem
        """
        targ_tag = force_to_tag( targ_tag )
        targ_attr_name = force_to_tag( targ_attr_name )
        span_tag = force_to_tag( 'text:span' )

        for elem in self.root.iter():
            # for example a 'draw:frame' with an attribute 'presentation:class' == "footer",
            if (elem.tag == targ_tag) and (elem.get(targ_attr_name,'') == targ_attr_val):
                
                # looking for a span element
                for sub_elem in elem.iter():
                    if sub_elem.tag == span_tag:
                        sub_elem.text = span_text
                        break
                    


if __name__ == "__main__":

    TFile = TemplateXML_File(r'D:\temp\open_office\content.xml')

    #TFile.write( r'D:\temp\open_office\content_v11.xml' )

    ss = TFile.find( 'office:body/office:spreadsheet' )
    print( 'ss =', ss )
    print( 'ss.tag =', ss.tag )
    print( 'type(ss) =', type(ss) )
    print()

    ss2 = TFile.find('{urn:oasis:names:tc:opendocument:xmlns:office:1.0}spreadsheet')
    print( 'ss2 =',ss2,'  (Should be None since can NOT search on tag)' )

    #print( TFile.findall( 'table:table', elem_obj=ss ) )
    print()
    #print( TFile.qnameOD.items()[:2] )

    newtab1 = TFile.new_elem( '{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table', attribOD=None)
    newtab2 = TFile.new_elem( 'table:table', attribOD=None)

    print( 'newtab1 =',newtab1 )
    print( 'newtab2 =',newtab2 )

    newtab3 = TFile.new_elem( 'table:table', attribOD={'table:name':'Sheet1'})
    print( 'newtab3 =',newtab3 )
    print( 'newtab3 =',list(newtab3.items()) )
