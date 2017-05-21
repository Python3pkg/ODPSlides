
# Python 2 and 3



        
"""Code Generated to build style:presentation-page-layout objects for odp files"""

import sys, os
from collections import OrderedDict

from odpslides.template_xml_file import TemplateXML_File
from odpslides.namespace import XMLNS_STR

def build_element( s ):
    """Add namespace to string and use TemplateXML_File to make Element"""
    s = s.replace(' ',' %s '%XMLNS_STR, 1) # First space ONLY
    return TemplateXML_File( s ).root
                


# Use func_quick_lookupD for access to function calls

func_quick_lookupD = {} # index=suffix name, value=function name


# Use content_style_name_lookupD for access to function calls

content_style_name_lookupD = {} # index=style name (e.g. "a123"), value=function name


def style_8_style_presentation_a1004():
    
    """Build Element style:style for presentation_a1004 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1004">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1052():
    
    """Build Element style:style for text_a1052 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1052">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1005():
    
    """Build Element style:style for text_a1005 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1005">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#898989" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.44444in" style:font-size-asian="0.44444in" style:font-size-complex="0.44444in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1053():
    
    """Build Element style:style for paragraph_a1053 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1053">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.8125in" fo:margin-right="0in" fo:text-indent="-0.3125in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1006():
    
    """Build Element style:style for paragraph_a1006 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1006">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0.11111in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1007():
    
    """Build Element style:style for text_a1007 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1007">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#898989" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1055():
    
    """Build Element style:style for presentation_a1055 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1055">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1008():
    
    """Build Element style:style for paragraph_a1008 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1008">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0.5in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1056():
    
    """Build Element style:style for presentation_a1056 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1056">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1057():
    
    """Build Element style:style for drawing-page_a1057 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1057">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1058():
    
    """Build Element style:style for text_a1058 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1058">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1059():
    
    """Build Element style:style for paragraph_a1059 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1059">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1120():
    
    """Build Element style:style for text_a1120 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1120">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1121():
    
    """Build Element style:style for paragraph_a1121 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1121">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1122():
    
    """Build Element style:style for presentation_a1122 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1122">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1123():
    
    """Build Element style:style for presentation_a1123 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1123">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1124():
    
    """Build Element style:style for presentation_a1124 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1124">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1125():
    
    """Build Element style:style for presentation_a1125 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1125">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1126():
    
    """Build Element style:style for presentation_a1126 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1126">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1127():
    
    """Build Element style:style for drawing-page_a1127 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1127">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1128():
    
    """Build Element style:style for text_a1128 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1128">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1129():
    
    """Build Element style:style for paragraph_a1129 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1129">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1010():
    
    """Build Element style:style for presentation_a1010 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1010">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1011():
    
    """Build Element style:style for drawing-page_a1011 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1011">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1060():
    
    """Build Element style:style for presentation_a1060 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1060">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1012():
    
    """Build Element style:style for text_a1012 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1012">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1061():
    
    """Build Element style:style for text_a1061 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1061">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.44444in" style:font-size-asian="0.44444in" style:font-size-complex="0.44444in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1013():
    
    """Build Element style:style for paragraph_a1013 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1013">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1062():
    
    """Build Element style:style for paragraph_a1062 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1062">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.375in" fo:margin-right="0in" fo:text-indent="-0.375in" fo:margin-top="0.11111in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1014():
    
    """Build Element style:style for presentation_a1014 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1014">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1015():
    
    """Build Element style:style for text_a1015 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1015">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.44444in" style:font-size-asian="0.44444in" style:font-size-complex="0.44444in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1064():
    
    """Build Element style:style for text_a1064 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1064">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1016():
    
    """Build Element style:style for paragraph_a1016 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1016">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.375in" fo:margin-right="0in" fo:text-indent="-0.375in" fo:margin-top="0.11111in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1065():
    
    """Build Element style:style for paragraph_a1065 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1065">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.8125in" fo:margin-right="0in" fo:text-indent="-0.3125in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1018():
    
    """Build Element style:style for text_a1018 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1018">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1067():
    
    """Build Element style:style for presentation_a1067 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1067">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1019():
    
    """Build Element style:style for paragraph_a1019 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1019">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.8125in" fo:margin-right="0in" fo:text-indent="-0.3125in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1068():
    
    """Build Element style:style for presentation_a1068 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1068">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1069():
    
    """Build Element style:style for drawing-page_a1069 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1069">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1130():
    
    """Build Element style:style for presentation_a1130 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1130">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1131():
    
    """Build Element style:style for presentation_a1131 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1131">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1132():
    
    """Build Element style:style for presentation_a1132 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1132">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1133():
    
    """Build Element style:style for presentation_a1133 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1133">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1134():
    
    """Build Element style:style for drawing-page_a1134 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1134">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1135():
    
    """Build Element style:style for text_a1135 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1135">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1136():
    
    """Build Element style:style for paragraph_a1136 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1136">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1137():
    
    """Build Element style:style for presentation_a1137 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1137">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1138():
    
    """Build Element style:style for presentation_a1138 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1138">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1139():
    
    """Build Element style:style for presentation_a1139 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1139">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1021():
    
    """Build Element style:style for presentation_a1021 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1021">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1070():
    
    """Build Element style:style for text_a1070 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1070">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1022():
    
    """Build Element style:style for drawing-page_a1022 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1022">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1071():
    
    """Build Element style:style for paragraph_a1071 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1071">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1023():
    
    """Build Element style:style for text_a1023 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1023">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1072():
    
    """Build Element style:style for presentation_a1072 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1072">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1024():
    
    """Build Element style:style for paragraph_a1024 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1024">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1073():
    
    """Build Element style:style for presentation_a1073 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1073">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1025():
    
    """Build Element style:style for presentation_a1025 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1025">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1074():
    
    """Build Element style:style for presentation_a1074 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1074">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1026():
    
    """Build Element style:style for text_a1026 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1026">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1075():
    
    """Build Element style:style for drawing-page_a1075 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1075">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1027():
    
    """Build Element style:style for paragraph_a1027 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1027">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.375in" fo:margin-right="0in" fo:text-indent="-0.375in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1076():
    
    """Build Element style:style for text_a1076 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1076">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1077():
    
    """Build Element style:style for paragraph_a1077 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1077">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1029():
    
    """Build Element style:style for text_a1029 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1029">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1078():
    
    """Build Element style:style for presentation_a1078 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1078">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1079():
    
    """Build Element style:style for presentation_a1079 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1079">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1140():
    
    """Build Element style:style for text_a1140 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1140">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.44444in" style:font-size-asian="0.44444in" style:font-size-complex="0.44444in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1141():
    
    """Build Element style:style for paragraph_a1141 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1141">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.375in" fo:margin-right="0in" fo:text-indent="-0.375in" fo:margin-top="0.11111in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1143():
    
    """Build Element style:style for text_a1143 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1143">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1144():
    
    """Build Element style:style for paragraph_a1144 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1144">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.8125in" fo:margin-right="0in" fo:text-indent="-0.3125in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1146():
    
    """Build Element style:style for presentation_a1146 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1146">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1147():
    
    """Build Element style:style for drawing-page_a1147 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1147">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1148():
    
    """Build Element style:style for text_a1148 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1148">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1149():
    
    """Build Element style:style for paragraph_a1149 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1149">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1030():
    
    """Build Element style:style for paragraph_a1030 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1030">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.8125in" fo:margin-right="0in" fo:text-indent="-0.3125in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1032():
    
    """Build Element style:style for presentation_a1032 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1032">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1080():
    
    """Build Element style:style for text_a1080 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1080">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.44444in" style:font-size-asian="0.44444in" style:font-size-complex="0.44444in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1033():
    
    """Build Element style:style for text_a1033 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1033">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1081():
    
    """Build Element style:style for paragraph_a1081 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1081">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.375in" fo:margin-right="0in" fo:text-indent="-0.375in" fo:margin-top="0.11111in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1034():
    
    """Build Element style:style for paragraph_a1034 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1034">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.375in" fo:margin-right="0in" fo:text-indent="-0.375in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1083():
    
    """Build Element style:style for text_a1083 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1083">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1036():
    
    """Build Element style:style for text_a1036 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1036">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.33333in" style:font-size-asian="0.33333in" style:font-size-complex="0.33333in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1084():
    
    """Build Element style:style for paragraph_a1084 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1084">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.8125in" fo:margin-right="0in" fo:text-indent="-0.3125in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1037():
    
    """Build Element style:style for paragraph_a1037 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1037">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.8125in" fo:margin-right="0in" fo:text-indent="-0.3125in" fo:margin-top="0.08333in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1086():
    
    """Build Element style:style for presentation_a1086 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1086">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1039():
    
    """Build Element style:style for presentation_a1039 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1039">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1087():
    
    """Build Element style:style for drawing-page_a1087 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1087">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1088():
    
    """Build Element style:style for text_a1088 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1088">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1089():
    
    """Build Element style:style for paragraph_a1089 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1089">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1100():
    
    """Build Element style:style for drawing-page_a1100 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1100">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1101():
    
    """Build Element style:style for text_a1101 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1101">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1102():
    
    """Build Element style:style for paragraph_a1102 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1102">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1150():
    
    """Build Element style:style for presentation_a1150 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1150">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1103():
    
    """Build Element style:style for presentation_a1103 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1103">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1151():
    
    """Build Element style:style for presentation_a1151 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1151">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1104():
    
    """Build Element style:style for presentation_a1104 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1104">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1152():
    
    """Build Element style:style for presentation_a1152 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1152">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1105():
    
    """Build Element style:style for presentation_a1105 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1105">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1153():
    
    """Build Element style:style for text_a1153 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1153">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.44444in" style:font-size-asian="0.44444in" style:font-size-complex="0.44444in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1106():
    
    """Build Element style:style for presentation_a1106 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1106">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1154():
    
    """Build Element style:style for paragraph_a1154 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1154">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.375in" fo:margin-right="0in" fo:text-indent="-0.375in" fo:margin-top="0.11111in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1107():
    
    """Build Element style:style for drawing-page_a1107 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1107">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1108():
    
    """Build Element style:style for text_a1108 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1108">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1156():
    
    """Build Element style:style for text_a1156 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1156">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1109():
    
    """Build Element style:style for paragraph_a1109 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1109">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1157():
    
    """Build Element style:style for paragraph_a1157 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1157">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.8125in" fo:margin-right="0in" fo:text-indent="-0.3125in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1159():
    
    """Build Element style:style for presentation_a1159 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1159">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1040():
    
    """Build Element style:style for drawing-page_a1040 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1040">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1041():
    
    """Build Element style:style for text_a1041 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1041">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1042():
    
    """Build Element style:style for paragraph_a1042 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1042">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1090():
    
    """Build Element style:style for presentation_a1090 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1090">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1043():
    
    """Build Element style:style for presentation_a1043 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1043">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1091():
    
    """Build Element style:style for text_a1091 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1091">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.44444in" style:font-size-asian="0.44444in" style:font-size-complex="0.44444in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1044():
    
    """Build Element style:style for presentation_a1044 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1044">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1092():
    
    """Build Element style:style for paragraph_a1092 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1092">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.375in" fo:margin-right="0in" fo:text-indent="-0.375in" fo:margin-top="0.11111in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1045():
    
    """Build Element style:style for drawing-page_a1045 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1045">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1046():
    
    """Build Element style:style for text_a1046 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1046">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1094():
    
    """Build Element style:style for text_a1094 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1094">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1047():
    
    """Build Element style:style for paragraph_a1047 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1047">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1095():
    
    """Build Element style:style for paragraph_a1095 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1095">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.8125in" fo:margin-right="0in" fo:text-indent="-0.3125in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1048():
    
    """Build Element style:style for presentation_a1048 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1048">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1097():
    
    """Build Element style:style for presentation_a1097 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1097">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1049():
    
    """Build Element style:style for text_a1049 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1049">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.44444in" style:font-size-asian="0.44444in" style:font-size-complex="0.44444in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1098():
    
    """Build Element style:style for presentation_a1098 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1098">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1099():
    
    """Build Element style:style for presentation_a1099 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1099">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1110():
    
    """Build Element style:style for presentation_a1110 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1110">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1111():
    
    """Build Element style:style for presentation_a1111 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1111">
<style:graphic-properties draw:fill="none" draw:stroke="none" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1112():
    
    """Build Element style:style for text_a1112 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1112">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.44444in" style:font-size-asian="0.44444in" style:font-size-complex="0.44444in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1160():
    
    """Build Element style:style for drawing-page_a1160 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1160">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1113():
    
    """Build Element style:style for paragraph_a1113 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1113">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.375in" fo:margin-right="0in" fo:text-indent="-0.375in" fo:margin-top="0.11111in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1161():
    
    """Build Element style:style for text_a1161 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1161">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1162():
    
    """Build Element style:style for paragraph_a1162 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1162">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1115():
    
    """Build Element style:style for text_a1115 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1115">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.38889in" style:font-size-asian="0.38889in" style:font-size-complex="0.38889in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1163():
    
    """Build Element style:style for presentation_a1163 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1163">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="middle" draw:textarea-horizontal-align="center" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1116():
    
    """Build Element style:style for paragraph_a1116 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1116">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.8125in" fo:margin-right="0in" fo:text-indent="-0.3125in" fo:margin-top="0.09722in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1164():
    
    """Build Element style:style for presentation_a1164 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1164">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_presentation_a1118():
    
    """Build Element style:style for presentation_a1118 """
    
    elem = build_element( """<style:style style:family="presentation" style:name="a1118">
<style:graphic-properties fo:wrap-option="wrap" fo:padding-top="0.05in" fo:padding-bottom="0.05in" fo:padding-left="0.1in" fo:padding-right="0.1in" draw:textarea-vertical-align="top" draw:textarea-horizontal-align="left" draw:fill="none" draw:stroke="none" draw:auto-grow-width="false" draw:auto-grow-height="false" />
<style:paragraph-properties style:font-independent-line-spacing="true" style:writing-mode="lr-tb" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1119():
    
    """Build Element style:style for drawing-page_a1119 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1119">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_drawing_page_a1001():
    
    """Build Element style:style for drawing-page_a1001 """
    
    elem = build_element( """<style:style style:family="drawing-page" style:name="a1001">
<style:drawing-page-properties draw:fill="solid" draw:fill-color="#ccffcc" draw:opacity="100%" presentation:transition-type="manual" presentation:transition-speed="slow" presentation:visibility="visible" draw:background-size="border" presentation:background-objects-visible="true" presentation:background-visible="true" presentation:display-header="false" presentation:display-footer="false" presentation:display-page-number="false" presentation:display-date-time="false" />
</style:style>
""" )
    
    return elem

def style_8_style_text_a1002():
    
    """Build Element style:style for text_a1002 """
    
    elem = build_element( """<style:style style:family="text" style:name="a1002">
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-family="Calibri" fo:font-size="0.61111in" style:font-size-asian="0.61111in" style:font-size-complex="0.61111in" fo:letter-spacing="0in" fo:language="en" fo:country="US" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="true" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1050():
    
    """Build Element style:style for paragraph_a1050 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1050">
<style:paragraph-properties fo:line-height="100%" fo:text-align="left" style:tab-stop-distance="1in" fo:margin-left="0.375in" fo:margin-right="0in" fo:text-indent="-0.375in" fo:margin-top="0.11111in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def style_8_style_paragraph_a1003():
    
    """Build Element style:style for paragraph_a1003 """
    
    elem = build_element( """<style:style style:family="paragraph" style:name="a1003">
<style:paragraph-properties fo:line-height="100%" fo:text-align="center" style:tab-stop-distance="1in" fo:margin-left="0in" fo:margin-right="0in" fo:text-indent="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:punctuation-wrap="hanging" style:vertical-align="auto" style:writing-mode="lr-tb">
<style:tab-stops />
</style:paragraph-properties>
<style:text-properties fo:font-variant="normal" fo:text-transform="none" fo:color="#000000" style:text-line-through-type="none" style:text-line-through-style="none" style:text-line-through-width="auto" style:text-line-through-color="font-color" style:text-position="0% 100%" fo:font-size="0.25in" style:font-size-asian="0.25in" style:font-size-complex="0.25in" fo:letter-spacing="0in" fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal" style:text-underline-type="none" style:text-underline-style="none" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal" style:text-underline-mode="continuous" style:letter-kerning="false" />
</style:style>
""" )
    
    return elem

def text_8_list_style_a1051():
    
    """Build Element text:list-style for a1051 """
    
    elem = build_element( """<text:list-style style:name="a1051">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.4375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1054():
    
    """Build Element text:list-style for a1054 """
    
    elem = build_element( """<text:list-style style:name="a1054">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.0625in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.4375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1017():
    
    """Build Element text:list-style for a1017 """
    
    elem = build_element( """<text:list-style style:name="a1017">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.4375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1093():
    
    """Build Element text:list-style for a1093 """
    
    elem = build_element( """<text:list-style style:name="a1093">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.4375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1096():
    
    """Build Element text:list-style for a1096 """
    
    elem = build_element( """<text:list-style style:name="a1096">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.0625in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.4375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1114():
    
    """Build Element text:list-style for a1114 """
    
    elem = build_element( """<text:list-style style:name="a1114">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.4375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1082():
    
    """Build Element text:list-style for a1082 """
    
    elem = build_element( """<text:list-style style:name="a1082">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.4375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1009():
    
    """Build Element text:list-style for a1009 """
    
    elem = build_element( """<text:list-style style:name="a1009">
<text:list-level-style-number text:level="1" style:num-format="">
<style:list-level-properties text:space-before="0in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="2" style:num-format="">
<style:list-level-properties text:space-before="0.5in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="3" style:num-format="">
<style:list-level-properties text:space-before="0.9375in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="4" style:num-format="">
<style:list-level-properties text:space-before="1.4375in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="5" style:num-format="">
<style:list-level-properties text:space-before="1.9375in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="6" style:num-format="">
<style:list-level-properties text:space-before="2.1875in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="7" style:num-format="">
<style:list-level-properties text:space-before="2.6875in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="8" style:num-format="">
<style:list-level-properties text:space-before="3.1875in" />
</text:list-level-style-number>
<text:list-level-style-number text:level="9" style:num-format="">
<style:list-level-properties text:space-before="3.6875in" />
</text:list-level-style-number>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1085():
    
    """Build Element text:list-style for a1085 """
    
    elem = build_element( """<text:list-style style:name="a1085">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.0625in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.4375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1117():
    
    """Build Element text:list-style for a1117 """
    
    elem = build_element( """<text:list-style style:name="a1117">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.0625in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.4375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1155():
    
    """Build Element text:list-style for a1155 """
    
    elem = build_element( """<text:list-style style:name="a1155">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.4375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1031():
    
    """Build Element text:list-style for a1031 """
    
    elem = build_element( """<text:list-style style:name="a1031">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.0625in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.4375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1158():
    
    """Build Element text:list-style for a1158 """
    
    elem = build_element( """<text:list-style style:name="a1158">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.0625in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.4375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1035():
    
    """Build Element text:list-style for a1035 """
    
    elem = build_element( """<text:list-style style:name="a1035">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.4375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1142():
    
    """Build Element text:list-style for a1142 """
    
    elem = build_element( """<text:list-style style:name="a1142">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.4375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1038():
    
    """Build Element text:list-style for a1038 """
    
    elem = build_element( """<text:list-style style:name="a1038">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.0625in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.4375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1145():
    
    """Build Element text:list-style for a1145 """
    
    elem = build_element( """<text:list-style style:name="a1145">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.0625in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.4375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1020():
    
    """Build Element text:list-style for a1020 """
    
    elem = build_element( """<text:list-style style:name="a1020">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.0625in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.4375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1063():
    
    """Build Element text:list-style for a1063 """
    
    elem = build_element( """<text:list-style style:name="a1063">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.4375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1028():
    
    """Build Element text:list-style for a1028 """
    
    elem = build_element( """<text:list-style style:name="a1028">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.4375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="0.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.375in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="1.875in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="2.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.125in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\xA2">
<style:list-level-properties text:space-before="3.625in" text:min-label-width="0.375in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem

def text_8_list_style_a1066():
    
    """Build Element text:list-style for a1066 """
    
    elem = build_element( """<text:list-style style:name="a1066">
<text:list-level-style-bullet text:level="1" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.0625in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="2" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.5in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="3" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="0.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="4" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.4375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="5" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="1.9375in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="6" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="7" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="2.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="8" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.1875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
<text:list-level-style-bullet text:level="9" text:bullet-char="\xE2\x80\x93">
<style:list-level-properties text:space-before="3.6875in" text:min-label-width="0.3125in" />
<style:text-properties fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="100%" />
</text:list-level-style-bullet>
</text:list-style>
""" )
    
    return elem



# Set values in func_quick_lookupD
func_quick_lookupD["a1009"] = text_8_list_style_a1009
func_quick_lookupD["a1017"] = text_8_list_style_a1017
func_quick_lookupD["a1020"] = text_8_list_style_a1020
func_quick_lookupD["a1028"] = text_8_list_style_a1028
func_quick_lookupD["a1031"] = text_8_list_style_a1031
func_quick_lookupD["a1035"] = text_8_list_style_a1035
func_quick_lookupD["a1038"] = text_8_list_style_a1038
func_quick_lookupD["a1051"] = text_8_list_style_a1051
func_quick_lookupD["a1054"] = text_8_list_style_a1054
func_quick_lookupD["a1063"] = text_8_list_style_a1063
func_quick_lookupD["a1066"] = text_8_list_style_a1066
func_quick_lookupD["a1082"] = text_8_list_style_a1082
func_quick_lookupD["a1085"] = text_8_list_style_a1085
func_quick_lookupD["a1093"] = text_8_list_style_a1093
func_quick_lookupD["a1096"] = text_8_list_style_a1096
func_quick_lookupD["a1114"] = text_8_list_style_a1114
func_quick_lookupD["a1117"] = text_8_list_style_a1117
func_quick_lookupD["a1142"] = text_8_list_style_a1142
func_quick_lookupD["a1145"] = text_8_list_style_a1145
func_quick_lookupD["a1155"] = text_8_list_style_a1155
func_quick_lookupD["a1158"] = text_8_list_style_a1158
func_quick_lookupD["drawing-page_a1001"] = style_8_style_drawing_page_a1001
func_quick_lookupD["drawing-page_a1011"] = style_8_style_drawing_page_a1011
func_quick_lookupD["drawing-page_a1022"] = style_8_style_drawing_page_a1022
func_quick_lookupD["drawing-page_a1040"] = style_8_style_drawing_page_a1040
func_quick_lookupD["drawing-page_a1045"] = style_8_style_drawing_page_a1045
func_quick_lookupD["drawing-page_a1057"] = style_8_style_drawing_page_a1057
func_quick_lookupD["drawing-page_a1069"] = style_8_style_drawing_page_a1069
func_quick_lookupD["drawing-page_a1075"] = style_8_style_drawing_page_a1075
func_quick_lookupD["drawing-page_a1087"] = style_8_style_drawing_page_a1087
func_quick_lookupD["drawing-page_a1100"] = style_8_style_drawing_page_a1100
func_quick_lookupD["drawing-page_a1107"] = style_8_style_drawing_page_a1107
func_quick_lookupD["drawing-page_a1119"] = style_8_style_drawing_page_a1119
func_quick_lookupD["drawing-page_a1127"] = style_8_style_drawing_page_a1127
func_quick_lookupD["drawing-page_a1134"] = style_8_style_drawing_page_a1134
func_quick_lookupD["drawing-page_a1147"] = style_8_style_drawing_page_a1147
func_quick_lookupD["drawing-page_a1160"] = style_8_style_drawing_page_a1160
func_quick_lookupD["paragraph_a1003"] = style_8_style_paragraph_a1003
func_quick_lookupD["paragraph_a1006"] = style_8_style_paragraph_a1006
func_quick_lookupD["paragraph_a1008"] = style_8_style_paragraph_a1008
func_quick_lookupD["paragraph_a1013"] = style_8_style_paragraph_a1013
func_quick_lookupD["paragraph_a1016"] = style_8_style_paragraph_a1016
func_quick_lookupD["paragraph_a1019"] = style_8_style_paragraph_a1019
func_quick_lookupD["paragraph_a1024"] = style_8_style_paragraph_a1024
func_quick_lookupD["paragraph_a1027"] = style_8_style_paragraph_a1027
func_quick_lookupD["paragraph_a1030"] = style_8_style_paragraph_a1030
func_quick_lookupD["paragraph_a1034"] = style_8_style_paragraph_a1034
func_quick_lookupD["paragraph_a1037"] = style_8_style_paragraph_a1037
func_quick_lookupD["paragraph_a1042"] = style_8_style_paragraph_a1042
func_quick_lookupD["paragraph_a1047"] = style_8_style_paragraph_a1047
func_quick_lookupD["paragraph_a1050"] = style_8_style_paragraph_a1050
func_quick_lookupD["paragraph_a1053"] = style_8_style_paragraph_a1053
func_quick_lookupD["paragraph_a1059"] = style_8_style_paragraph_a1059
func_quick_lookupD["paragraph_a1062"] = style_8_style_paragraph_a1062
func_quick_lookupD["paragraph_a1065"] = style_8_style_paragraph_a1065
func_quick_lookupD["paragraph_a1071"] = style_8_style_paragraph_a1071
func_quick_lookupD["paragraph_a1077"] = style_8_style_paragraph_a1077
func_quick_lookupD["paragraph_a1081"] = style_8_style_paragraph_a1081
func_quick_lookupD["paragraph_a1084"] = style_8_style_paragraph_a1084
func_quick_lookupD["paragraph_a1089"] = style_8_style_paragraph_a1089
func_quick_lookupD["paragraph_a1092"] = style_8_style_paragraph_a1092
func_quick_lookupD["paragraph_a1095"] = style_8_style_paragraph_a1095
func_quick_lookupD["paragraph_a1102"] = style_8_style_paragraph_a1102
func_quick_lookupD["paragraph_a1109"] = style_8_style_paragraph_a1109
func_quick_lookupD["paragraph_a1113"] = style_8_style_paragraph_a1113
func_quick_lookupD["paragraph_a1116"] = style_8_style_paragraph_a1116
func_quick_lookupD["paragraph_a1121"] = style_8_style_paragraph_a1121
func_quick_lookupD["paragraph_a1129"] = style_8_style_paragraph_a1129
func_quick_lookupD["paragraph_a1136"] = style_8_style_paragraph_a1136
func_quick_lookupD["paragraph_a1141"] = style_8_style_paragraph_a1141
func_quick_lookupD["paragraph_a1144"] = style_8_style_paragraph_a1144
func_quick_lookupD["paragraph_a1149"] = style_8_style_paragraph_a1149
func_quick_lookupD["paragraph_a1154"] = style_8_style_paragraph_a1154
func_quick_lookupD["paragraph_a1157"] = style_8_style_paragraph_a1157
func_quick_lookupD["paragraph_a1162"] = style_8_style_paragraph_a1162
func_quick_lookupD["presentation_a1004"] = style_8_style_presentation_a1004
func_quick_lookupD["presentation_a1010"] = style_8_style_presentation_a1010
func_quick_lookupD["presentation_a1014"] = style_8_style_presentation_a1014
func_quick_lookupD["presentation_a1021"] = style_8_style_presentation_a1021
func_quick_lookupD["presentation_a1025"] = style_8_style_presentation_a1025
func_quick_lookupD["presentation_a1032"] = style_8_style_presentation_a1032
func_quick_lookupD["presentation_a1039"] = style_8_style_presentation_a1039
func_quick_lookupD["presentation_a1043"] = style_8_style_presentation_a1043
func_quick_lookupD["presentation_a1044"] = style_8_style_presentation_a1044
func_quick_lookupD["presentation_a1048"] = style_8_style_presentation_a1048
func_quick_lookupD["presentation_a1055"] = style_8_style_presentation_a1055
func_quick_lookupD["presentation_a1056"] = style_8_style_presentation_a1056
func_quick_lookupD["presentation_a1060"] = style_8_style_presentation_a1060
func_quick_lookupD["presentation_a1067"] = style_8_style_presentation_a1067
func_quick_lookupD["presentation_a1068"] = style_8_style_presentation_a1068
func_quick_lookupD["presentation_a1072"] = style_8_style_presentation_a1072
func_quick_lookupD["presentation_a1073"] = style_8_style_presentation_a1073
func_quick_lookupD["presentation_a1074"] = style_8_style_presentation_a1074
func_quick_lookupD["presentation_a1078"] = style_8_style_presentation_a1078
func_quick_lookupD["presentation_a1079"] = style_8_style_presentation_a1079
func_quick_lookupD["presentation_a1086"] = style_8_style_presentation_a1086
func_quick_lookupD["presentation_a1090"] = style_8_style_presentation_a1090
func_quick_lookupD["presentation_a1097"] = style_8_style_presentation_a1097
func_quick_lookupD["presentation_a1098"] = style_8_style_presentation_a1098
func_quick_lookupD["presentation_a1099"] = style_8_style_presentation_a1099
func_quick_lookupD["presentation_a1103"] = style_8_style_presentation_a1103
func_quick_lookupD["presentation_a1104"] = style_8_style_presentation_a1104
func_quick_lookupD["presentation_a1105"] = style_8_style_presentation_a1105
func_quick_lookupD["presentation_a1106"] = style_8_style_presentation_a1106
func_quick_lookupD["presentation_a1110"] = style_8_style_presentation_a1110
func_quick_lookupD["presentation_a1111"] = style_8_style_presentation_a1111
func_quick_lookupD["presentation_a1118"] = style_8_style_presentation_a1118
func_quick_lookupD["presentation_a1122"] = style_8_style_presentation_a1122
func_quick_lookupD["presentation_a1123"] = style_8_style_presentation_a1123
func_quick_lookupD["presentation_a1124"] = style_8_style_presentation_a1124
func_quick_lookupD["presentation_a1125"] = style_8_style_presentation_a1125
func_quick_lookupD["presentation_a1126"] = style_8_style_presentation_a1126
func_quick_lookupD["presentation_a1130"] = style_8_style_presentation_a1130
func_quick_lookupD["presentation_a1131"] = style_8_style_presentation_a1131
func_quick_lookupD["presentation_a1132"] = style_8_style_presentation_a1132
func_quick_lookupD["presentation_a1133"] = style_8_style_presentation_a1133
func_quick_lookupD["presentation_a1137"] = style_8_style_presentation_a1137
func_quick_lookupD["presentation_a1138"] = style_8_style_presentation_a1138
func_quick_lookupD["presentation_a1139"] = style_8_style_presentation_a1139
func_quick_lookupD["presentation_a1146"] = style_8_style_presentation_a1146
func_quick_lookupD["presentation_a1150"] = style_8_style_presentation_a1150
func_quick_lookupD["presentation_a1151"] = style_8_style_presentation_a1151
func_quick_lookupD["presentation_a1152"] = style_8_style_presentation_a1152
func_quick_lookupD["presentation_a1159"] = style_8_style_presentation_a1159
func_quick_lookupD["presentation_a1163"] = style_8_style_presentation_a1163
func_quick_lookupD["presentation_a1164"] = style_8_style_presentation_a1164
func_quick_lookupD["text_a1002"] = style_8_style_text_a1002
func_quick_lookupD["text_a1005"] = style_8_style_text_a1005
func_quick_lookupD["text_a1007"] = style_8_style_text_a1007
func_quick_lookupD["text_a1012"] = style_8_style_text_a1012
func_quick_lookupD["text_a1015"] = style_8_style_text_a1015
func_quick_lookupD["text_a1018"] = style_8_style_text_a1018
func_quick_lookupD["text_a1023"] = style_8_style_text_a1023
func_quick_lookupD["text_a1026"] = style_8_style_text_a1026
func_quick_lookupD["text_a1029"] = style_8_style_text_a1029
func_quick_lookupD["text_a1033"] = style_8_style_text_a1033
func_quick_lookupD["text_a1036"] = style_8_style_text_a1036
func_quick_lookupD["text_a1041"] = style_8_style_text_a1041
func_quick_lookupD["text_a1046"] = style_8_style_text_a1046
func_quick_lookupD["text_a1049"] = style_8_style_text_a1049
func_quick_lookupD["text_a1052"] = style_8_style_text_a1052
func_quick_lookupD["text_a1058"] = style_8_style_text_a1058
func_quick_lookupD["text_a1061"] = style_8_style_text_a1061
func_quick_lookupD["text_a1064"] = style_8_style_text_a1064
func_quick_lookupD["text_a1070"] = style_8_style_text_a1070
func_quick_lookupD["text_a1076"] = style_8_style_text_a1076
func_quick_lookupD["text_a1080"] = style_8_style_text_a1080
func_quick_lookupD["text_a1083"] = style_8_style_text_a1083
func_quick_lookupD["text_a1088"] = style_8_style_text_a1088
func_quick_lookupD["text_a1091"] = style_8_style_text_a1091
func_quick_lookupD["text_a1094"] = style_8_style_text_a1094
func_quick_lookupD["text_a1101"] = style_8_style_text_a1101
func_quick_lookupD["text_a1108"] = style_8_style_text_a1108
func_quick_lookupD["text_a1112"] = style_8_style_text_a1112
func_quick_lookupD["text_a1115"] = style_8_style_text_a1115
func_quick_lookupD["text_a1120"] = style_8_style_text_a1120
func_quick_lookupD["text_a1128"] = style_8_style_text_a1128
func_quick_lookupD["text_a1135"] = style_8_style_text_a1135
func_quick_lookupD["text_a1140"] = style_8_style_text_a1140
func_quick_lookupD["text_a1143"] = style_8_style_text_a1143
func_quick_lookupD["text_a1148"] = style_8_style_text_a1148
func_quick_lookupD["text_a1153"] = style_8_style_text_a1153
func_quick_lookupD["text_a1156"] = style_8_style_text_a1156
func_quick_lookupD["text_a1161"] = style_8_style_text_a1161




# Set values in content_style_name_lookupD
content_style_name_lookupD["a1001"] = style_8_style_drawing_page_a1001
content_style_name_lookupD["a1002"] = style_8_style_text_a1002
content_style_name_lookupD["a1003"] = style_8_style_paragraph_a1003
content_style_name_lookupD["a1004"] = style_8_style_presentation_a1004
content_style_name_lookupD["a1005"] = style_8_style_text_a1005
content_style_name_lookupD["a1006"] = style_8_style_paragraph_a1006
content_style_name_lookupD["a1007"] = style_8_style_text_a1007
content_style_name_lookupD["a1008"] = style_8_style_paragraph_a1008
content_style_name_lookupD["a1009"] = text_8_list_style_a1009
content_style_name_lookupD["a1010"] = style_8_style_presentation_a1010
content_style_name_lookupD["a1011"] = style_8_style_drawing_page_a1011
content_style_name_lookupD["a1012"] = style_8_style_text_a1012
content_style_name_lookupD["a1013"] = style_8_style_paragraph_a1013
content_style_name_lookupD["a1014"] = style_8_style_presentation_a1014
content_style_name_lookupD["a1015"] = style_8_style_text_a1015
content_style_name_lookupD["a1016"] = style_8_style_paragraph_a1016
content_style_name_lookupD["a1017"] = text_8_list_style_a1017
content_style_name_lookupD["a1018"] = style_8_style_text_a1018
content_style_name_lookupD["a1019"] = style_8_style_paragraph_a1019
content_style_name_lookupD["a1020"] = text_8_list_style_a1020
content_style_name_lookupD["a1021"] = style_8_style_presentation_a1021
content_style_name_lookupD["a1022"] = style_8_style_drawing_page_a1022
content_style_name_lookupD["a1023"] = style_8_style_text_a1023
content_style_name_lookupD["a1024"] = style_8_style_paragraph_a1024
content_style_name_lookupD["a1025"] = style_8_style_presentation_a1025
content_style_name_lookupD["a1026"] = style_8_style_text_a1026
content_style_name_lookupD["a1027"] = style_8_style_paragraph_a1027
content_style_name_lookupD["a1028"] = text_8_list_style_a1028
content_style_name_lookupD["a1029"] = style_8_style_text_a1029
content_style_name_lookupD["a1030"] = style_8_style_paragraph_a1030
content_style_name_lookupD["a1031"] = text_8_list_style_a1031
content_style_name_lookupD["a1032"] = style_8_style_presentation_a1032
content_style_name_lookupD["a1033"] = style_8_style_text_a1033
content_style_name_lookupD["a1034"] = style_8_style_paragraph_a1034
content_style_name_lookupD["a1035"] = text_8_list_style_a1035
content_style_name_lookupD["a1036"] = style_8_style_text_a1036
content_style_name_lookupD["a1037"] = style_8_style_paragraph_a1037
content_style_name_lookupD["a1038"] = text_8_list_style_a1038
content_style_name_lookupD["a1039"] = style_8_style_presentation_a1039
content_style_name_lookupD["a1040"] = style_8_style_drawing_page_a1040
content_style_name_lookupD["a1041"] = style_8_style_text_a1041
content_style_name_lookupD["a1042"] = style_8_style_paragraph_a1042
content_style_name_lookupD["a1043"] = style_8_style_presentation_a1043
content_style_name_lookupD["a1044"] = style_8_style_presentation_a1044
content_style_name_lookupD["a1045"] = style_8_style_drawing_page_a1045
content_style_name_lookupD["a1046"] = style_8_style_text_a1046
content_style_name_lookupD["a1047"] = style_8_style_paragraph_a1047
content_style_name_lookupD["a1048"] = style_8_style_presentation_a1048
content_style_name_lookupD["a1049"] = style_8_style_text_a1049
content_style_name_lookupD["a1050"] = style_8_style_paragraph_a1050
content_style_name_lookupD["a1051"] = text_8_list_style_a1051
content_style_name_lookupD["a1052"] = style_8_style_text_a1052
content_style_name_lookupD["a1053"] = style_8_style_paragraph_a1053
content_style_name_lookupD["a1054"] = text_8_list_style_a1054
content_style_name_lookupD["a1055"] = style_8_style_presentation_a1055
content_style_name_lookupD["a1056"] = style_8_style_presentation_a1056
content_style_name_lookupD["a1057"] = style_8_style_drawing_page_a1057
content_style_name_lookupD["a1058"] = style_8_style_text_a1058
content_style_name_lookupD["a1059"] = style_8_style_paragraph_a1059
content_style_name_lookupD["a1060"] = style_8_style_presentation_a1060
content_style_name_lookupD["a1061"] = style_8_style_text_a1061
content_style_name_lookupD["a1062"] = style_8_style_paragraph_a1062
content_style_name_lookupD["a1063"] = text_8_list_style_a1063
content_style_name_lookupD["a1064"] = style_8_style_text_a1064
content_style_name_lookupD["a1065"] = style_8_style_paragraph_a1065
content_style_name_lookupD["a1066"] = text_8_list_style_a1066
content_style_name_lookupD["a1067"] = style_8_style_presentation_a1067
content_style_name_lookupD["a1068"] = style_8_style_presentation_a1068
content_style_name_lookupD["a1069"] = style_8_style_drawing_page_a1069
content_style_name_lookupD["a1070"] = style_8_style_text_a1070
content_style_name_lookupD["a1071"] = style_8_style_paragraph_a1071
content_style_name_lookupD["a1072"] = style_8_style_presentation_a1072
content_style_name_lookupD["a1073"] = style_8_style_presentation_a1073
content_style_name_lookupD["a1074"] = style_8_style_presentation_a1074
content_style_name_lookupD["a1075"] = style_8_style_drawing_page_a1075
content_style_name_lookupD["a1076"] = style_8_style_text_a1076
content_style_name_lookupD["a1077"] = style_8_style_paragraph_a1077
content_style_name_lookupD["a1078"] = style_8_style_presentation_a1078
content_style_name_lookupD["a1079"] = style_8_style_presentation_a1079
content_style_name_lookupD["a1080"] = style_8_style_text_a1080
content_style_name_lookupD["a1081"] = style_8_style_paragraph_a1081
content_style_name_lookupD["a1082"] = text_8_list_style_a1082
content_style_name_lookupD["a1083"] = style_8_style_text_a1083
content_style_name_lookupD["a1084"] = style_8_style_paragraph_a1084
content_style_name_lookupD["a1085"] = text_8_list_style_a1085
content_style_name_lookupD["a1086"] = style_8_style_presentation_a1086
content_style_name_lookupD["a1087"] = style_8_style_drawing_page_a1087
content_style_name_lookupD["a1088"] = style_8_style_text_a1088
content_style_name_lookupD["a1089"] = style_8_style_paragraph_a1089
content_style_name_lookupD["a1090"] = style_8_style_presentation_a1090
content_style_name_lookupD["a1091"] = style_8_style_text_a1091
content_style_name_lookupD["a1092"] = style_8_style_paragraph_a1092
content_style_name_lookupD["a1093"] = text_8_list_style_a1093
content_style_name_lookupD["a1094"] = style_8_style_text_a1094
content_style_name_lookupD["a1095"] = style_8_style_paragraph_a1095
content_style_name_lookupD["a1096"] = text_8_list_style_a1096
content_style_name_lookupD["a1097"] = style_8_style_presentation_a1097
content_style_name_lookupD["a1098"] = style_8_style_presentation_a1098
content_style_name_lookupD["a1099"] = style_8_style_presentation_a1099
content_style_name_lookupD["a1100"] = style_8_style_drawing_page_a1100
content_style_name_lookupD["a1101"] = style_8_style_text_a1101
content_style_name_lookupD["a1102"] = style_8_style_paragraph_a1102
content_style_name_lookupD["a1103"] = style_8_style_presentation_a1103
content_style_name_lookupD["a1104"] = style_8_style_presentation_a1104
content_style_name_lookupD["a1105"] = style_8_style_presentation_a1105
content_style_name_lookupD["a1106"] = style_8_style_presentation_a1106
content_style_name_lookupD["a1107"] = style_8_style_drawing_page_a1107
content_style_name_lookupD["a1108"] = style_8_style_text_a1108
content_style_name_lookupD["a1109"] = style_8_style_paragraph_a1109
content_style_name_lookupD["a1110"] = style_8_style_presentation_a1110
content_style_name_lookupD["a1111"] = style_8_style_presentation_a1111
content_style_name_lookupD["a1112"] = style_8_style_text_a1112
content_style_name_lookupD["a1113"] = style_8_style_paragraph_a1113
content_style_name_lookupD["a1114"] = text_8_list_style_a1114
content_style_name_lookupD["a1115"] = style_8_style_text_a1115
content_style_name_lookupD["a1116"] = style_8_style_paragraph_a1116
content_style_name_lookupD["a1117"] = text_8_list_style_a1117
content_style_name_lookupD["a1118"] = style_8_style_presentation_a1118
content_style_name_lookupD["a1119"] = style_8_style_drawing_page_a1119
content_style_name_lookupD["a1120"] = style_8_style_text_a1120
content_style_name_lookupD["a1121"] = style_8_style_paragraph_a1121
content_style_name_lookupD["a1122"] = style_8_style_presentation_a1122
content_style_name_lookupD["a1123"] = style_8_style_presentation_a1123
content_style_name_lookupD["a1124"] = style_8_style_presentation_a1124
content_style_name_lookupD["a1125"] = style_8_style_presentation_a1125
content_style_name_lookupD["a1126"] = style_8_style_presentation_a1126
content_style_name_lookupD["a1127"] = style_8_style_drawing_page_a1127
content_style_name_lookupD["a1128"] = style_8_style_text_a1128
content_style_name_lookupD["a1129"] = style_8_style_paragraph_a1129
content_style_name_lookupD["a1130"] = style_8_style_presentation_a1130
content_style_name_lookupD["a1131"] = style_8_style_presentation_a1131
content_style_name_lookupD["a1132"] = style_8_style_presentation_a1132
content_style_name_lookupD["a1133"] = style_8_style_presentation_a1133
content_style_name_lookupD["a1134"] = style_8_style_drawing_page_a1134
content_style_name_lookupD["a1135"] = style_8_style_text_a1135
content_style_name_lookupD["a1136"] = style_8_style_paragraph_a1136
content_style_name_lookupD["a1137"] = style_8_style_presentation_a1137
content_style_name_lookupD["a1138"] = style_8_style_presentation_a1138
content_style_name_lookupD["a1139"] = style_8_style_presentation_a1139
content_style_name_lookupD["a1140"] = style_8_style_text_a1140
content_style_name_lookupD["a1141"] = style_8_style_paragraph_a1141
content_style_name_lookupD["a1142"] = text_8_list_style_a1142
content_style_name_lookupD["a1143"] = style_8_style_text_a1143
content_style_name_lookupD["a1144"] = style_8_style_paragraph_a1144
content_style_name_lookupD["a1145"] = text_8_list_style_a1145
content_style_name_lookupD["a1146"] = style_8_style_presentation_a1146
content_style_name_lookupD["a1147"] = style_8_style_drawing_page_a1147
content_style_name_lookupD["a1148"] = style_8_style_text_a1148
content_style_name_lookupD["a1149"] = style_8_style_paragraph_a1149
content_style_name_lookupD["a1150"] = style_8_style_presentation_a1150
content_style_name_lookupD["a1151"] = style_8_style_presentation_a1151
content_style_name_lookupD["a1152"] = style_8_style_presentation_a1152
content_style_name_lookupD["a1153"] = style_8_style_text_a1153
content_style_name_lookupD["a1154"] = style_8_style_paragraph_a1154
content_style_name_lookupD["a1155"] = text_8_list_style_a1155
content_style_name_lookupD["a1156"] = style_8_style_text_a1156
content_style_name_lookupD["a1157"] = style_8_style_paragraph_a1157
content_style_name_lookupD["a1158"] = text_8_list_style_a1158
content_style_name_lookupD["a1159"] = style_8_style_presentation_a1159
content_style_name_lookupD["a1160"] = style_8_style_drawing_page_a1160
content_style_name_lookupD["a1161"] = style_8_style_text_a1161
content_style_name_lookupD["a1162"] = style_8_style_paragraph_a1162
content_style_name_lookupD["a1163"] = style_8_style_presentation_a1163
content_style_name_lookupD["a1164"] = style_8_style_presentation_a1164

if __name__ == "__main__":
    print( content_style_name_lookupD["a1160"]() )
