# Support Python 2 and 3




import os
import sys
import zipfile
import time
from copy import deepcopy
import datetime

from odpslides.template_xml_file import TemplateXML_File
from odpslides.find_obj import find_elem_w_attrib, NS_attrib, NS

here = os.path.abspath(os.path.dirname(__file__))


def read_source_from_odp(ods_fname, fname, subdir='' ):

    full_ods_path = os.path.join( here, 'templates', ods_fname )

    if subdir:
        inner_fname = subdir + '/' + fname
    else:
        inner_fname =  fname

    odsfile = zipfile.ZipFile( full_ods_path )
    return odsfile.read( inner_fname ).decode('utf-8')
        

def load_template_xml_from_odp(ods_fname, fname, subdir='' ):
    src = read_source_from_odp(ods_fname, fname, subdir=subdir )
    return TemplateXML_File( src )



class ODPFile( object ):
    
    def get_short_path(self, elem, omit_full_path=True):
        
        try:
            s = self.content_xml_obj.get_short_path( elem )
        except:
            s = self.styles_xml_obj.get_short_path( elem )
            
        if omit_full_path:
            sL = s.split('/')
            return sL[-1]
        else:
            return s
    
    def get_elem(self, elem_short_tag):
        
        try:
            elem_tag = self.content_xml_obj.NS( elem_short_tag )
            for elem in self.content_xml_obj.root.iter():
                if elem.tag == elem_tag:
                    return elem
        except:
            pass
            
        elem_tag = self.styles_xml_obj.NS( elem_short_tag )
        for elem in self.styles_xml_obj.root.iter():
            if elem.tag == elem_tag:
                return elem
            
        return None
    
    def get_elem_with_attr(self, elem_short_tag, attr_short_tag, attr_val):
        
        try:
            elem_tag = self.content_xml_obj.NS( elem_short_tag )
            attr_tag = self.content_xml_obj.NS( attr_short_tag )
            for elem in self.content_xml_obj.root.iter():
                if elem.tag == elem_tag:
                    if elem.get(attr_tag,'DUMMY') == attr_val:
                        return elem
        except:
            pass
            
        elem_tag = self.styles_xml_obj.NS( elem_short_tag )
        attr_tag = self.styles_xml_obj.NS( attr_short_tag )
        for elem in self.styles_xml_obj.root.iter():
            if elem.tag == elem_tag:
                if elem.get(attr_tag,'DUMMY') == attr_val:
                    return elem
            
        return None
    
    def __init__(self, filename):
        

        self.max_style_name_int = 0 # used for nameing styles (ex. draw:style-name="a123")
        self.max_draw_id_int = 0 # some internal use ???

        self.template_fname = filename
                
        self.slideL = [] # list of slide pages content
        
        # ................. Need to do some prep work with content_xml_obj ...............
        # Get ref auto_styles and presentation sections for document
        self.content_xml_obj = load_template_xml_from_odp( self.template_fname, 'content.xml' )
        
        # Need styles info as part of prep work
        self.styles_xml_obj = load_template_xml_from_odp( self.template_fname, 'styles.xml' )
        
        
        self.office_styles_elem = self.styles_xml_obj.root.find(\
                                  NS('office:styles') )
        #print('!!!!!!!!!! office_styles_elem =',self.office_styles_elem)
        
        self.office_automatic_styles_elem = self.styles_xml_obj.root.find(\
                                            NS('office:automatic-styles') )
        #print('!!!!!!!!!! office_automatic_styles_elem =',self.office_automatic_styles_elem)
        
        self.office_master_styles_elem = self.styles_xml_obj.root.find(\
                                         NS('office:master-styles') )
        #print('!!!!!!!!!! office_master_styles_elem =',self.office_master_styles_elem)
        
        
        # ===================================================================================
        
        self.init_master_styles()
        
        # ===================================================================================
        # Get ref auto_styles sections for document
        self.content_auto_styles = self.content_xml_obj.find('office:automatic-styles')
        #print('auto_styles =', self.content_auto_styles)
        self.content_body_presentation = self.content_xml_obj.find('office:body/office:presentation')
        #print('presentation =', self.content_body_presentation)
                
        self.meta_xml_obj = load_template_xml_from_odp( self.template_fname, 'meta.xml' )
        self.settings_xml_obj = load_template_xml_from_odp( self.template_fname, 'settings.xml' )
        
        self.mimetype_str = 'application/vnd.oasis.opendocument.presentation'
        
        self.metainf_manifest_xml_obj = load_template_xml_from_odp(self.template_fname, 'manifest.xml', subdir='META-INF')

        self.meta_creation_date_obj = self.meta_xml_obj.find('office:meta/meta:creation-date')
        self.meta_dc_date_obj = self.meta_xml_obj.find('office:meta/dc:date')

        self.meta_init_creator_obj = self.meta_xml_obj.find('office:meta/meta:initial-creator')
        self.meta_dc_creator_obj = self.meta_xml_obj.find('office:meta/dc:creator')


    def get_next_a_style(self):
        """Returns a string like "a123"  """
        
        self.max_style_name_int += 1
        return 'a%i'%self.max_style_name_int
        
    def get_next_draw_id(self):
        """Returns a string like "id123"  """
        
        self.max_draw_id_int += 1
        return 'id%i'%self.max_draw_id_int
        

    def init_master_styles( self ):
        """
        Use self.styles_xml_obj and self.content_xml_obj to organize page 
        layouts and master-page styles.
        
        Note:  presentation:object values == presentation:class values
        (i.e. object, subtitle, outline, footer, title, page-number, table, date-time)
        
        self.style_name_elem_from_nameD will hold style elements, index="a123" name, value=Element
        """
        
        # Make some shorter names
        tree_styles = self.styles_xml_obj
        tree_content = self.content_xml_obj
        #print(NS('draw:id'))
        
        STYLE_NAME_ATTRIB_NAME = NS('style:name')
        DRAW_ID_ATTRIB_NAME = NS('draw:id')
        #DRAW_GRADIENT_TAG = NS('draw:gradient')
        #DRAW_START_COLOR_ATTR = NS('draw:start-color')
        #DRAW_END_COLOR_ATTR = NS('draw:end-color')
        #DRAW_ANGLE_ATTR = NS('draw:angle')
        #DRAW_STYLE_ATTR = NS('draw:style')

        #DRAW_FILL_IMAGE_TAG = NS('draw:fill-image')
        #XLINK_HREF_ATTR =  NS('xlink:href')

        # Find the highest value of self.max_style_name_int
        self.style_name_elem_from_nameD = {} # index=style-name (ex. "a123"), value=elem
        
        rootL = [tree_styles.root, tree_content.root]
        for root in rootL:
            for elem in root.iter():
                aval = elem.get(STYLE_NAME_ATTRIB_NAME, '')
                if aval.startswith('a'):
                    try:
                        aint = int( aval[1:] )
                        if aint > self.max_style_name_int:
                            self.max_style_name_int = aint
                        self.style_name_elem_from_nameD[aval] = elem
                    except:
                        print('FAILED to get integer of style: "%s"'%aval)
                            
                id_val = elem.get(DRAW_ID_ATTRIB_NAME, '')
                if id_val.startswith('id'):
                    try:
                        idint = int( id_val[2:] )
                        if idint > self.max_draw_id_int:
                            self.max_draw_id_int = idint
                    except:
                        pass


        #print('Highest value of style   from styles.xml is "a%i"'%self.max_style_name_int)
        #print('Highest value of draw id from styles.xml is "id%i"'%self.max_draw_id_int)
        #print()
        
        # Build a lookup to select proper style:presentation-page-layout when 
        # the name of the master-page is given.
        # (ex. master="Master1-Layout1-title-Title-Slide",  layout="Master1-PPL1")

        # ==================== content info =======================
        page_contentL = tree_content.findall('office:body/office:presentation/draw:page') # Element objects
        #print('Number of page_contentL = %i'%len(page_contentL))


        # =================== styles info =========================
        print('='*77)

        # index=style:name of presentation-page-layout,  value=elem
        pres_page_layout_styleL = tree_styles.findall('office:styles/style:presentation-page-layout') # Element objects
        print('Number of presentation-page-layout styles = %i'%len(pres_page_layout_styleL))
        self.page_layout_elem_from_nameD = {} # index=layout name,  value=elem
        for pres_page_layout in pres_page_layout_styleL:
            self.page_layout_elem_from_nameD[ pres_page_layout.get( NS('style:name') ) ] = pres_page_layout

        master_page_styleL =  tree_styles.findall('office:master-styles/style:master-page') # Element objects
        print('Number of master-page styles = %i'%len(master_page_styleL))

        # Will need master page Element objects when generating new pages
        self.master_page_elem_from_nameD = {} # index=master name, value=elem (master-page Element)
        for master_page in master_page_styleL:
            name = master_page.get('{urn:oasis:names:tc:opendocument:xmlns:style:1.0}name')
            #print( 'Master Page Name = %s'%name )
            self.master_page_elem_from_nameD[ master_page.get( NS('style:name') ) ] = master_page
            

        # ============= check layout infor vs master info =======================
        #  from content, there are matching master and layout choices.
        #  Make sure that the number and type of child elements match
        #  Master elements have draw:frame elements with presentation:class attributes
        #  Layout elements have presentation:placeholder with presentation:object attributes
        print('='*77)

        self.matching_layout_nameD = {} # index=draw:master-page-name, value=presentation:presentation-page-layout-name
        self.draw_page_elem_from_nameD = {} # index=draw:master-page-name, value=Element obj for draw:page
        for page in page_contentL:
            master_name = page.get( NS('draw:master-page-name') )
            layout_name = page.get( NS('presentation:presentation-page-layout-name') )
            #print('used master="%60s",  layout="%s"'%(master_name, layout_name)  )
            self.matching_layout_nameD[master_name] = layout_name
            self.draw_page_elem_from_nameD[master_name] = page


if __name__=="__main__":
     
    blank = ODPFile( r'D:\py_proj_2015\odp_diff\blank.odp' )