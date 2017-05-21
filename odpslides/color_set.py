# Support Python 2 and 3




from odpslides.color_utils import getValidHexStr
from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag

DRAW_FRAME_TAG = force_to_tag( 'draw:frame' )
TEXT_SPAN_TAG =  force_to_tag( 'text:span' )
TEXT_STYLE_NAME_ATTR = force_to_tag( 'text:style-name' )
FONT_COLOR_ATTR = force_to_tag( 'fo:color' )
PRESENTATION_CLASS_ATTR = force_to_tag( 'presentation:class' )

def set_drawframe_font_color( presObj, draw_page, frame_class='title', font_color='black' ):
    """
    Set the fo:color in all the style elements of the frame
    
    """

    hex_col_str = getValidHexStr( font_color, "#000000") # default to black
    
    for elem in draw_page.iter():
        if elem.tag == DRAW_FRAME_TAG:
            if elem.get( PRESENTATION_CLASS_ATTR, '' ) == frame_class:
                # Now we are in proper "title", "subtitle", etc.
                for subelem in elem.iter():
                    if subelem.tag == TEXT_SPAN_TAG:
                        aNNN = subelem.get( TEXT_STYLE_NAME_ATTR, '' )
                        a_int = int( aNNN[1:] )
                        if a_int >= len(presObj.new_content_styleL):
                            print( 'Bad style index = %i, when len new_content_styleL = %i'%\
                                  (a_int, len(presObj.new_content_styleL)) )
                        else:
                            span_elem = presObj.new_content_styleL[ a_int ]
                            for sub_span_elem in span_elem.iter():
                                if sub_span_elem.get(FONT_COLOR_ATTR, ''):
                                    sub_span_elem.set( FONT_COLOR_ATTR, hex_col_str )

