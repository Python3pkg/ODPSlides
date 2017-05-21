# Support Python 2 and 3




import os
import sys
from copy import deepcopy
import re

from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag
from odpslides.color_utils import getValidHexStr
from odpslides.template_xml_file import TemplateXML_File


style_re = re.compile( '\"a[0-9]+\"' )

    
def build_text_list(text_or_list):
    """
    Start building textL, i.e a list of strings. Assume NO INDENTS.
    
    """
    
    # build a text list (textL)
    if (type(text_or_list) == type('text')) or (type(text_or_list) == type(b'text')): # a single string with \r and \t
        s = text_or_list.replace('\n','\r')
        textL = s.split( '\r' )
    elif type(text_or_list) == type(['s','t']): # a list of strings
        textL = []
        for s in text_or_list:
            s2 = s.replace('\n','\r')
            sL = s2.split('\r')
            textL.extend( sL )
    else:
        textL = ['No TextBox Text']
    return [s.strip() for s in textL]

def add_text_box( presObj, text_or_list='Test Message', 
                    text_font_colors='black #333333',
                    x=8.0, y=2.0):
    """
    text_font_colors can be a list of colors or a single string with space-seperated colors
    (e.g. "black #666666" or ["black", "#666666"])
    """
    if not presObj.new_content_pageL:
        print('...WARNING... No Last Page for TextBox:', text_or_list)
        return
    
    last_page = presObj.new_content_pageL[-1] # Page object 
    
    # Build a color list (colorL)
    # If not already in list form, make a list
    if type(text_font_colors) != type(['r','b']):
        # Create a list of colors
        colorL = text_font_colors.split(' ') # <- make a list
    else:
        colorL = text_font_colors # <- already a list
    # make the colors valid
    colorL = [ getValidHexStr(c,'#000000') for c in colorL ]    
    
    # if there's a problem with the list, make a default list
    if not colorL:
        colorL = ['#000000']
    
    # get new style names (e.g. "a123")
    a_frame = presObj.get_next_a_style()

    # Make new Element objects and style Element objects
    s = TBOX_DRAW_FRAME.replace('svg:x="5.75in" svg:y="3in"','svg:x="%sin" svg:y="%sin"'%(x,y))
    draw_frame = TemplateXML_File( s.replace('"a343"', '"%s"'%a_frame) ).root
    text_box = draw_frame.find( force_to_tag('draw:text-box') )
    
    draw_frame_style = TemplateXML_File( TBOX_DRAW_FRAME_STYLE.replace('"a343"', '"%s"'%a_frame) ).root
    
    # get all the lines in the TextBox
    textL = build_text_list(text_or_list)
    annn_styleElemL = [(a_frame, draw_frame_style)]
    
    for itext, text in enumerate(textL):
        
        hex_col_str = colorL[ itext % len(colorL) ]
        a_p = presObj.get_next_a_style()
        a_span = presObj.get_next_a_style()
    
        p_span_elem = TemplateXML_File( TBOX_TEXT_P_SPAN.replace('"a337"', '"%s"'%a_p).replace('"a336"', '"%s"'%a_span) ).root
        span_elem = p_span_elem.getchildren()[0]
        span_elem.text = text
        
        s = TBOX_TEXT_P_STYLE.replace( 'fo:color="#000000"', 'fo:color="%s"'%hex_col_str )
        p_style =  TemplateXML_File( s.replace('"a337"', '"%s"'%a_p) ).root
        
        s = TBOX_TEXT_SPAN_STYLE.replace( 'fo:color="#000000"', 'fo:color="%s"'%hex_col_str )
        span_style =  TemplateXML_File( s.replace('"a336"', '"%s"'%a_span) ).root
        
        annn_styleElemL.append(  (a_p, p_style) )
        annn_styleElemL.append( (a_span, span_style) )
        text_box.append( p_span_elem )
    
    # put the new style descriptions and elements into the Presentation object.
    for a_new, style_elem in annn_styleElemL:
        presObj.new_content_styleL.append( style_elem )
        presObj.new_content_styleD[ a_new ] = style_elem
                    
    
    last_page.draw_page.append( draw_frame )


TBOX_TEXT_P_SPAN = """
<text:p %s text:style-name="a337" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a336" text:class-names="">Here's the message.</text:span>
</text:p>
  """%XMLNS_STR
TBOX_TEXT_SPAN_STYLE = """
<style:style %s style:family="text" style:name="a336">
    <style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" 
    style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" 
    style:text-line-through-color="font-color" style:text-position="0%% 100%%" fo:font-family="Calibri" 
    fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" 
    fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" 
    style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" 
    style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" 
    style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true"/>
</style:style>"""%XMLNS_STR

TBOX_TEXT_P_STYLE = """
<style:style %s style:family="paragraph" style:name="a337">
    <style:paragraph-properties fo:line-height="100%%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0in" 
    fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" 
    style:vertical-align="auto" style:writing-mode="lr-tb">
        <style:tab-stops/>
    </style:paragraph-properties>
    <style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" 
    style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" 
    style:text-line-through-color="font-color" style:text-position="0%% 100%%" fo:font-size="0.25in" 
    style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" 
    style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" 
    style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" 
    fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" 
    style:letter-kerning="false"/>
</style:style>
"""%XMLNS_STR

# can fill TextBox by using:    draw:fill="solid"  draw:fill-color="#ff0000"
TBOX_DRAW_FRAME_STYLE = """
<style:style %s style:family="graphic" style:name="a343">
    <style:graphic-properties fo:wrap-option="no-wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" 
      fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" 
      draw:fill="none" draw:stroke="none" draw:auto-grow-width="true" draw:auto-grow-height="true"/>
    <style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb"/>
</style:style>
"""%XMLNS_STR

TBOX_DRAW_FRAME = """
<draw:frame %s draw:id="id63" draw:style-name="a343" draw:name="TextBox 1" svg:x="5.75in" svg:y="3in" svg:width="1.46192in" svg:height="1.00977in">
<draw:text-box>
</draw:text-box>
<svg:title/>
<svg:desc/>
</draw:frame>
"""%XMLNS_STR

if __name__ == "__main__":
    
    for s in [TBOX_TEXT_P_SPAN, TBOX_TEXT_P_STYLE, TBOX_TEXT_SPAN_STYLE, TBOX_DRAW_FRAME, TBOX_DRAW_FRAME_STYLE]:
        print( style_re.findall( s ) )
