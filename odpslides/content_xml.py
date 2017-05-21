# Support Python 2 and 3




import time
import sys
from copy import deepcopy

from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag
from odpslides.color_utils import getValidHexStr

DRAW_PAGE_TAG = force_to_tag( 'draw:page' )

class ContentXML(object):
    """
    ContentXML wraps the content.xml internal file of the reference odp file
    """
    
    def __init__(self, presObj, odp_ref):
        """
        presObj is the Presentation object
        
        odp_ref is the odp file opened by the Presentation object
        """
        
        self.presObj = presObj
        self.odp_ref = odp_ref
        
        self.make_clean_copy()
        
        
    def make_clean_copy(self):
        # Make a copy of the original content.xml Elements
        self.content_tmplt = deepcopy( self.odp_ref.content_xml_obj )
        
        body_pres_elem = self.content_tmplt.find('office:body/office:presentation')
        #for child in body_pres_elem.getchildren():
        #    print('Removing:',force_to_short(child.tag),'  from:', force_to_short(body_pres_elem.tag) )
            
        body_pres_elem.clear_children()
        
        
    def set_background(self):
        if self.presObj.page_type == 'solidbg':
            hex_col_str = getValidHexStr(  self.presObj.background_color , "#ffffff") # default to white
            self.content_tmplt.set_all_attr_of_tag( 'style:drawing-page-properties', 'draw:fill-color', hex_col_str)
               
    def set_show_page_number(self):
        self.content_tmplt.set_all_attr_of_tag( 'style:drawing-page-properties', 'presentation:display-page-number', 'true')
    
    def set_show_date(self):
        self.content_tmplt.set_all_attr_of_tag( 'style:drawing-page-properties', 'presentation:display-date-time', 'true')

    def set_show_footer(self):
        self.content_tmplt.set_all_attr_of_tag( 'style:drawing-page-properties', 'presentation:display-footer', 'true')
