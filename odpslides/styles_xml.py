# Support Python 2 and 3




import time
import sys
from copy import deepcopy

from odpslides.color_utils import getValidHexStr


class StylesXML(object):
    """
    StylesXML wraps the styles.xml internal file of the reference odp file
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
        # Make a copy of the original styles.xml Elements
        self.styles_tmplt = deepcopy( self.odp_ref.styles_xml_obj )
        
    def set_background(self):
        
        if self.presObj.page_type == 'solidbg':
            hex_col_str = getValidHexStr(  self.presObj.background_color , "#ffffff") # default to white
            self.styles_tmplt.set_all_attr_of_tag( 'style:drawing-page-properties', 'draw:fill-color', hex_col_str)
        
        elif self.presObj.page_type == 'grad':
            hex_col_str = getValidHexStr(  self.presObj.grad_start_color , "#ffffff") # default to white
            self.styles_tmplt.set_all_attr_of_tag( 'draw:gradient', 'draw:start-color', hex_col_str)
            #print('Setting start gradient color to', hex_col_str)

            hex_col_str = getValidHexStr(  self.presObj.grad_end_color , "#ffffff") # default to white
            self.styles_tmplt.set_all_attr_of_tag( 'draw:gradient', 'draw:end-color', hex_col_str)
            #print('Setting end gradient color to', hex_col_str)
            
            self.styles_tmplt.set_all_attr_of_tag( 'draw:gradient', 'draw:style', self.presObj.grad_draw_style)
            self.styles_tmplt.set_all_attr_of_tag( 'draw:gradient', 'draw:angle', self.presObj.grad_angle)
            
        elif self.presObj.page_type == 'image':
            
            img_name = 'media/%s'%self.presObj.image_nameL[0]
            self.styles_tmplt.set_all_attr_of_tag( 'draw:fill-image', 'xlink:href', img_name)
            
        
    def set_page_number_font_color(self):
        hex_col_str = getValidHexStr(  self.presObj.page_number_font_color , "#000000") # default to black
        #print('Setting page_number_font_color to',hex_col_str)
        
        self.styles_tmplt.set_all_styles_of_tag_w_attr( 'draw:frame', 'presentation:class', "page-number",
                                         'fo:color', hex_col_str)

    def set_date_font_color(self):
        hex_col_str = getValidHexStr(  self.presObj.date_font_color , "#000000") # default to black
        #print('Setting page_number_font_color to',hex_col_str)
        
        self.styles_tmplt.set_all_styles_of_tag_w_attr( 'draw:frame', 'presentation:class', "date-time",
                                         'fo:color', hex_col_str)

    def set_footer_font_color(self):
        hex_col_str = getValidHexStr(  self.presObj.footer_font_color , "#000000") # default to black
        #print('Setting page_number_font_color to',hex_col_str)
        
        self.styles_tmplt.set_all_styles_of_tag_w_attr( 'draw:frame', 'presentation:class', "footer",
                                         'fo:color', hex_col_str)

    def set_footer_text(self):
        
        self.styles_tmplt.set_span_text_of_tag_w_attr('draw:frame', 'presentation:class', "footer",
                                         span_text=self.presObj.footer)        

