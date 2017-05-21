
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

func_quick_lookupD = {} # index=display name, value=function name
layout_name_lookupD = {}
display_name_lookupD = {}


def style_8_presentation_page_layout_Title_Slide():
    
    """Build Element style:presentation-page-layout for Title Slide """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL1" style:display-name="Title Slide">
<presentation:placeholder presentation:object="title" svg:x="0.75in" svg:y="2.32986in" svg:width="8.5in" svg:height="1.60764in" />
<presentation:placeholder presentation:object="subtitle" svg:x="1.5in" svg:y="4.25in" svg:width="7in" svg:height="1.91667in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title_and_Content():
    
    """Build Element style:presentation-page-layout for Title and Content """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL2" style:display-name="Title and Content">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Section_Header():
    
    """Build Element style:presentation-page-layout for Section Header """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL3" style:display-name="Section Header">
<presentation:placeholder presentation:object="title" svg:x="0.78993in" svg:y="4.81944in" svg:width="8.5in" svg:height="1.48958in" />
<presentation:placeholder presentation:object="outline" svg:x="0.78993in" svg:y="3.17882in" svg:width="8.5in" svg:height="1.64062in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Two_Content():
    
    """Build Element style:presentation-page-layout for Two Content """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL4" style:display-name="Two Content">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="object" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Comparison():
    
    """Build Element style:presentation-page-layout for Comparison """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL5" style:display-name="Comparison">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="outline" svg:x="0.5in" svg:y="1.67882in" svg:width="4.4184in" svg:height="0.69965in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="2.37847in" svg:width="4.4184in" svg:height="4.32118in" />
<presentation:placeholder presentation:object="outline" svg:x="5.07986in" svg:y="1.67882in" svg:width="4.42014in" svg:height="0.69965in" />
<presentation:placeholder presentation:object="object" svg:x="5.07986in" svg:y="2.37847in" svg:width="4.42014in" svg:height="4.32118in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title_Only():
    
    """Build Element style:presentation-page-layout for Title Only """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL6" style:display-name="Title Only">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Blank():
    
    """Build Element style:presentation-page-layout for Blank """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL7" style:display-name="Blank">
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Content_with_Caption():
    
    """Build Element style:presentation-page-layout for Content with Caption """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL8" style:display-name="Content with Caption">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.29861in" svg:width="3.28993in" svg:height="1.27083in" />
<presentation:placeholder presentation:object="object" svg:x="3.90972in" svg:y="0.29861in" svg:width="5.59028in" svg:height="6.40104in" />
<presentation:placeholder presentation:object="outline" svg:x="0.5in" svg:y="1.56944in" svg:width="3.28993in" svg:height="5.13021in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Picture_with_Caption():
    
    """Build Element style:presentation-page-layout for Picture with Caption """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL9" style:display-name="Picture with Caption">
<presentation:placeholder presentation:object="title" svg:x="1.96007in" svg:y="5.25in" svg:width="6in" svg:height="0.61979in" />
<presentation:placeholder presentation:object="graphic" svg:x="1.96007in" svg:y="0.67014in" svg:width="6in" svg:height="4.5in" />
<presentation:placeholder presentation:object="outline" svg:x="1.96007in" svg:y="5.86979in" svg:width="6in" svg:height="0.88021in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title_and_Vertical_Text():
    
    """Build Element style:presentation-page-layout for Title and Vertical Text """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL10" style:display-name="Title and Vertical Text">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="outline" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Vertical_Title_and_Text():
    
    """Build Element style:presentation-page-layout for Vertical Title and Text """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL11" style:display-name="Vertical Title and Text">
<presentation:placeholder presentation:object="title" svg:x="7.25in" svg:y="0.30035in" svg:width="2.25in" svg:height="6.39931in" />
<presentation:placeholder presentation:object="outline" svg:x="0.5in" svg:y="0.30035in" svg:width="6.58333in" svg:height="6.39931in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title_and_Text():
    
    """Build Element style:presentation-page-layout for Title and Text """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL12" style:display-name="Title and Text">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="outline" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title_and_2_Column_Text():
    
    """Build Element style:presentation-page-layout for Title and 2-Column Text """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL13" style:display-name="Title and 2-Column Text">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="outline" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="outline" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title_and_Text_over_Content():
    
    """Build Element style:presentation-page-layout for Title and Text over Content """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL14" style:display-name="Title and Text over Content">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="outline" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="2.39063in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="4.30729in" svg:width="9in" svg:height="2.39236in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title__Text__and_Content():
    
    """Build Element style:presentation-page-layout for Title_ Text_ and Content """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL15" style:display-name="Title, Text, and Content">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="outline" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="object" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title__Content_and_Text():
    
    """Build Element style:presentation-page-layout for Title_ Content and Text """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL16" style:display-name="Title, Content and Text">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="outline" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title__Text__and_2_Content():
    
    """Build Element style:presentation-page-layout for Title_ Text_ and 2 Content """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL17" style:display-name="Title, Text, and 2 Content">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="outline" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="object" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" />
<presentation:placeholder presentation:object="object" svg:x="5.08333in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title__Content__and_2_Content():
    
    """Build Element style:presentation-page-layout for Title_ Content_ and 2 Content """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL18" style:display-name="Title, Content, and 2 Content">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="object" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" />
<presentation:placeholder presentation:object="object" svg:x="5.08333in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title_and_Content_over_Text():
    
    """Build Element style:presentation-page-layout for Title and Content over Text """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL19" style:display-name="Title and Content over Text">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="2.39063in" />
<presentation:placeholder presentation:object="outline" svg:x="0.5in" svg:y="4.30729in" svg:width="9in" svg:height="2.39236in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title_and_4_Content():
    
    """Build Element style:presentation-page-layout for Title and 4 Content """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL20" style:display-name="Title and 4 Content">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" />
<presentation:placeholder presentation:object="object" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" />
<presentation:placeholder presentation:object="object" svg:x="5.08333in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title__2_Content_and_Content():
    
    """Build Element style:presentation-page-layout for Title_ 2 Content and Content """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL21" style:display-name="Title, 2 Content and Content">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" />
<presentation:placeholder presentation:object="object" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title__2_Content_and_Text():
    
    """Build Element style:presentation-page-layout for Title_ 2 Content and Text """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL22" style:display-name="Title, 2 Content and Text">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" />
<presentation:placeholder presentation:object="outline" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title_and_2_Content_over_Text():
    
    """Build Element style:presentation-page-layout for Title and 2 Content over Text """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL23" style:display-name="Title and 2 Content over Text">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="object" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" />
<presentation:placeholder presentation:object="object" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" />
<presentation:placeholder presentation:object="outline" svg:x="0.5in" svg:y="4.30729in" svg:width="9in" svg:height="2.39236in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_presentation_page_layout_Title_and_Table():
    
    """Build Element style:presentation-page-layout for Title and Table """
    
    elem = build_element( """<style:presentation-page-layout style:name="Master1-PPL24" style:display-name="Title and Table">
<presentation:placeholder presentation:object="title" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" />
<presentation:placeholder presentation:object="table" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="4.94965in" />
<presentation:placeholder presentation:object="date-time" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="footer" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" />
<presentation:placeholder presentation:object="page-number" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" />
</style:presentation-page-layout>
""" )
    
    return elem

def style_8_default_style_graphic():
    
    """Build Element style:default-style for graphic """
    
    elem = build_element( """<style:default-style style:family="graphic">
<style:graphic-properties draw:fill="solid" draw:fill-color="#4f81bd" draw:opacity="100%" draw:stroke="solid" svg:stroke-width="0.02778in" svg:stroke-color="#385d8a" svg:stroke-opacity="100%" />
</style:default-style>
""" )
    
    return elem

def draw_8_gradient():
    
    """Build Element draw:gradient """
    
    elem = build_element( """<draw:gradient draw:name="a825" draw:style="linear" draw:angle="0" draw:start-color="#5e9eff" draw:end-color="#85c2ff" draw:start-intensity="100%" draw:end-intensity="100%" />
""" )
    
    return elem



# Set values in func_quick_lookupD
func_quick_lookupD[""] = draw_8_gradient
func_quick_lookupD["Blank"] = style_8_presentation_page_layout_Blank
func_quick_lookupD["Comparison"] = style_8_presentation_page_layout_Comparison
func_quick_lookupD["Content with Caption"] = style_8_presentation_page_layout_Content_with_Caption
func_quick_lookupD["Picture with Caption"] = style_8_presentation_page_layout_Picture_with_Caption
func_quick_lookupD["Section Header"] = style_8_presentation_page_layout_Section_Header
func_quick_lookupD["Title Only"] = style_8_presentation_page_layout_Title_Only
func_quick_lookupD["Title Slide"] = style_8_presentation_page_layout_Title_Slide
func_quick_lookupD["Title and 2 Content over Text"] = style_8_presentation_page_layout_Title_and_2_Content_over_Text
func_quick_lookupD["Title and 2-Column Text"] = style_8_presentation_page_layout_Title_and_2_Column_Text
func_quick_lookupD["Title and 4 Content"] = style_8_presentation_page_layout_Title_and_4_Content
func_quick_lookupD["Title and Content"] = style_8_presentation_page_layout_Title_and_Content
func_quick_lookupD["Title and Content over Text"] = style_8_presentation_page_layout_Title_and_Content_over_Text
func_quick_lookupD["Title and Table"] = style_8_presentation_page_layout_Title_and_Table
func_quick_lookupD["Title and Text"] = style_8_presentation_page_layout_Title_and_Text
func_quick_lookupD["Title and Text over Content"] = style_8_presentation_page_layout_Title_and_Text_over_Content
func_quick_lookupD["Title and Vertical Text"] = style_8_presentation_page_layout_Title_and_Vertical_Text
func_quick_lookupD["Title_ 2 Content and Content"] = style_8_presentation_page_layout_Title__2_Content_and_Content
func_quick_lookupD["Title_ 2 Content and Text"] = style_8_presentation_page_layout_Title__2_Content_and_Text
func_quick_lookupD["Title_ Content and Text"] = style_8_presentation_page_layout_Title__Content_and_Text
func_quick_lookupD["Title_ Content_ and 2 Content"] = style_8_presentation_page_layout_Title__Content__and_2_Content
func_quick_lookupD["Title_ Text_ and 2 Content"] = style_8_presentation_page_layout_Title__Text__and_2_Content
func_quick_lookupD["Title_ Text_ and Content"] = style_8_presentation_page_layout_Title__Text__and_Content
func_quick_lookupD["Two Content"] = style_8_presentation_page_layout_Two_Content
func_quick_lookupD["Vertical Title and Text"] = style_8_presentation_page_layout_Vertical_Title_and_Text
func_quick_lookupD["graphic"] = style_8_default_style_graphic




# Set values in layout_name_lookupD
layout_name_lookupD["Blank"] = "Master1-PPL7"
layout_name_lookupD["Comparison"] = "Master1-PPL5"
layout_name_lookupD["Content with Caption"] = "Master1-PPL8"
layout_name_lookupD["Picture with Caption"] = "Master1-PPL9"
layout_name_lookupD["Section Header"] = "Master1-PPL3"
layout_name_lookupD["Title Only"] = "Master1-PPL6"
layout_name_lookupD["Title Slide"] = "Master1-PPL1"
layout_name_lookupD["Title and 2 Content over Text"] = "Master1-PPL23"
layout_name_lookupD["Title and 2-Column Text"] = "Master1-PPL13"
layout_name_lookupD["Title and 4 Content"] = "Master1-PPL20"
layout_name_lookupD["Title and Content"] = "Master1-PPL2"
layout_name_lookupD["Title and Content over Text"] = "Master1-PPL19"
layout_name_lookupD["Title and Table"] = "Master1-PPL24"
layout_name_lookupD["Title and Text"] = "Master1-PPL12"
layout_name_lookupD["Title and Text over Content"] = "Master1-PPL14"
layout_name_lookupD["Title and Vertical Text"] = "Master1-PPL10"
layout_name_lookupD["Title, 2 Content and Content"] = "Master1-PPL21"
layout_name_lookupD["Title, 2 Content and Text"] = "Master1-PPL22"
layout_name_lookupD["Title, Content and Text"] = "Master1-PPL16"
layout_name_lookupD["Title, Content, and 2 Content"] = "Master1-PPL18"
layout_name_lookupD["Title, Text, and 2 Content"] = "Master1-PPL17"
layout_name_lookupD["Title, Text, and Content"] = "Master1-PPL15"
layout_name_lookupD["Two Content"] = "Master1-PPL4"
layout_name_lookupD["Vertical Title and Text"] = "Master1-PPL11"




# Set values in display_name_lookupD
display_name_lookupD["Master1-PPL1"] = "Title Slide"
display_name_lookupD["Master1-PPL10"] = "Title and Vertical Text"
display_name_lookupD["Master1-PPL11"] = "Vertical Title and Text"
display_name_lookupD["Master1-PPL12"] = "Title and Text"
display_name_lookupD["Master1-PPL13"] = "Title and 2-Column Text"
display_name_lookupD["Master1-PPL14"] = "Title and Text over Content"
display_name_lookupD["Master1-PPL15"] = "Title, Text, and Content"
display_name_lookupD["Master1-PPL16"] = "Title, Content and Text"
display_name_lookupD["Master1-PPL17"] = "Title, Text, and 2 Content"
display_name_lookupD["Master1-PPL18"] = "Title, Content, and 2 Content"
display_name_lookupD["Master1-PPL19"] = "Title and Content over Text"
display_name_lookupD["Master1-PPL2"] = "Title and Content"
display_name_lookupD["Master1-PPL20"] = "Title and 4 Content"
display_name_lookupD["Master1-PPL21"] = "Title, 2 Content and Content"
display_name_lookupD["Master1-PPL22"] = "Title, 2 Content and Text"
display_name_lookupD["Master1-PPL23"] = "Title and 2 Content over Text"
display_name_lookupD["Master1-PPL24"] = "Title and Table"
display_name_lookupD["Master1-PPL3"] = "Section Header"
display_name_lookupD["Master1-PPL4"] = "Two Content"
display_name_lookupD["Master1-PPL5"] = "Comparison"
display_name_lookupD["Master1-PPL6"] = "Title Only"
display_name_lookupD["Master1-PPL7"] = "Blank"
display_name_lookupD["Master1-PPL8"] = "Content with Caption"
display_name_lookupD["Master1-PPL9"] = "Picture with Caption"



if __name__ == "__main__":
    print( func_quick_lookupD["Title Only"]() )
