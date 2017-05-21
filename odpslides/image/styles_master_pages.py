
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


def draw_8_layer_set():
    
    """Build Element draw:layer-set """
    
    elem = build_element( """<draw:layer-set>
<draw:layer draw:name="Master1-bg" draw:protected="true" />
</draw:layer-set>
""" )
    
    return elem

def style_8_master_page_Master1_PPL1():
    
    """Build Element style:master-page for Master1-PPL1 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout1-title-Title-Slide" style:page-layout-name="pageLayout1" draw:style-name="a32">
<draw:frame draw:id="id5" presentation:style-name="a35" draw:name="Title 1" svg:x="0.75in" svg:y="2.32986in" svg:width="8.5in" svg:height="1.60764in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a34" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a33" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id6" presentation:style-name="a38" draw:name="Subtitle 2" svg:x="1.5in" svg:y="4.25in" svg:width="7in" svg:height="1.91667in" presentation:class="subtitle" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a37" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a36" text:class-names="">
Click to edit Master subtitle style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id7" presentation:style-name="a42" draw:name="Date Placeholder 3" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a41" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a39" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a40">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id8" presentation:style-name="a45" draw:name="Footer Placeholder 4" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a44" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a43" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id9" presentation:style-name="a48" draw:name="Slide Number Placeholder 5" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a47" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a46" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL2():
    
    """Build Element style:master-page for Master1-PPL2 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout2-obj-Title-and-Content" style:page-layout-name="pageLayout1" draw:style-name="a50">
<draw:frame draw:id="id10" presentation:style-name="a53" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a52" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a51" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id11" presentation:style-name="a69" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a56">
<text:list-item>
<text:p text:style-name="a55" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a54" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a59">
<text:list-item>
<text:list text:style-name="a59">
<text:list-item>
<text:p text:style-name="a58" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a57" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a62">
<text:list-item>
<text:list text:style-name="a62">
<text:list-item>
<text:list text:style-name="a62">
<text:list-item>
<text:p text:style-name="a61" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a60" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a65">
<text:list-item>
<text:list text:style-name="a65">
<text:list-item>
<text:list text:style-name="a65">
<text:list-item>
<text:list text:style-name="a65">
<text:list-item>
<text:p text:style-name="a64" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a63" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a68">
<text:list-item>
<text:list text:style-name="a68">
<text:list-item>
<text:list text:style-name="a68">
<text:list-item>
<text:list text:style-name="a68">
<text:list-item>
<text:list text:style-name="a68">
<text:list-item>
<text:p text:style-name="a67" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a66" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id12" presentation:style-name="a73" draw:name="Date Placeholder 3" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a72" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a70" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a71">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id13" presentation:style-name="a76" draw:name="Footer Placeholder 4" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a75" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a74" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id14" presentation:style-name="a79" draw:name="Slide Number Placeholder 5" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a78" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a77" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL4():
    
    """Build Element style:master-page for Master1-PPL4 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout4-twoObj-Two-Content" style:page-layout-name="pageLayout1" draw:style-name="a100">
<draw:frame draw:id="id20" presentation:style-name="a103" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a102" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a101" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id21" presentation:style-name="a119" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a106">
<text:list-item>
<text:p text:style-name="a105" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a104" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a109">
<text:list-item>
<text:list text:style-name="a109">
<text:list-item>
<text:p text:style-name="a108" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a107" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a112">
<text:list-item>
<text:list text:style-name="a112">
<text:list-item>
<text:list text:style-name="a112">
<text:list-item>
<text:p text:style-name="a111" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a110" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a115">
<text:list-item>
<text:list text:style-name="a115">
<text:list-item>
<text:list text:style-name="a115">
<text:list-item>
<text:list text:style-name="a115">
<text:list-item>
<text:p text:style-name="a114" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a113" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a118">
<text:list-item>
<text:list text:style-name="a118">
<text:list-item>
<text:list text:style-name="a118">
<text:list-item>
<text:list text:style-name="a118">
<text:list-item>
<text:list text:style-name="a118">
<text:list-item>
<text:p text:style-name="a117" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a116" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id22" presentation:style-name="a135" draw:name="Content Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a122">
<text:list-item>
<text:p text:style-name="a121" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a120" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a125">
<text:list-item>
<text:list text:style-name="a125">
<text:list-item>
<text:p text:style-name="a124" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a123" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a128">
<text:list-item>
<text:list text:style-name="a128">
<text:list-item>
<text:list text:style-name="a128">
<text:list-item>
<text:p text:style-name="a127" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a126" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a131">
<text:list-item>
<text:list text:style-name="a131">
<text:list-item>
<text:list text:style-name="a131">
<text:list-item>
<text:list text:style-name="a131">
<text:list-item>
<text:p text:style-name="a130" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a129" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a134">
<text:list-item>
<text:list text:style-name="a134">
<text:list-item>
<text:list text:style-name="a134">
<text:list-item>
<text:list text:style-name="a134">
<text:list-item>
<text:list text:style-name="a134">
<text:list-item>
<text:p text:style-name="a133" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a132" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id23" presentation:style-name="a139" draw:name="Date Placeholder 4" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a138" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a136" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a137">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id24" presentation:style-name="a142" draw:name="Footer Placeholder 5" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a141" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a140" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id25" presentation:style-name="a145" draw:name="Slide Number Placeholder 6" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a144" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a143" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL12():
    
    """Build Element style:master-page for Master1-PPL12 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout12-tx-Title-and-Text" style:page-layout-name="pageLayout1" draw:style-name="a348">
<draw:frame draw:id="id63" presentation:style-name="a351" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a350" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a349" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id64" presentation:style-name="a367" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a354">
<text:list-item>
<text:p text:style-name="a353" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a352" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a357">
<text:list-item>
<text:list text:style-name="a357">
<text:list-item>
<text:p text:style-name="a356" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a355" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a360">
<text:list-item>
<text:list text:style-name="a360">
<text:list-item>
<text:list text:style-name="a360">
<text:list-item>
<text:p text:style-name="a359" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a358" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a363">
<text:list-item>
<text:list text:style-name="a363">
<text:list-item>
<text:list text:style-name="a363">
<text:list-item>
<text:list text:style-name="a363">
<text:list-item>
<text:p text:style-name="a362" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a361" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a366">
<text:list-item>
<text:list text:style-name="a366">
<text:list-item>
<text:list text:style-name="a366">
<text:list-item>
<text:list text:style-name="a366">
<text:list-item>
<text:list text:style-name="a366">
<text:list-item>
<text:p text:style-name="a365" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a364" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id65" presentation:style-name="a371" draw:name="Date Placeholder 3" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a370" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a368" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a369">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id66" presentation:style-name="a374" draw:name="Footer Placeholder 4" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a373" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a372" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id67" presentation:style-name="a377" draw:name="Slide Number Placeholder 5" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a376" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a375" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL13():
    
    """Build Element style:master-page for Master1-PPL13 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout13-twoColTx-Title-and-2-Column-Text" style:page-layout-name="pageLayout1" draw:style-name="a379">
<draw:frame draw:id="id68" presentation:style-name="a382" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a381" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a380" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id69" presentation:style-name="a398" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a385">
<text:list-item>
<text:p text:style-name="a384" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a383" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a388">
<text:list-item>
<text:list text:style-name="a388">
<text:list-item>
<text:p text:style-name="a387" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a386" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a391">
<text:list-item>
<text:list text:style-name="a391">
<text:list-item>
<text:list text:style-name="a391">
<text:list-item>
<text:p text:style-name="a390" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a389" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a394">
<text:list-item>
<text:list text:style-name="a394">
<text:list-item>
<text:list text:style-name="a394">
<text:list-item>
<text:list text:style-name="a394">
<text:list-item>
<text:p text:style-name="a393" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a392" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a397">
<text:list-item>
<text:list text:style-name="a397">
<text:list-item>
<text:list text:style-name="a397">
<text:list-item>
<text:list text:style-name="a397">
<text:list-item>
<text:list text:style-name="a397">
<text:list-item>
<text:p text:style-name="a396" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a395" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id70" presentation:style-name="a414" draw:name="Text Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a401">
<text:list-item>
<text:p text:style-name="a400" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a399" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a404">
<text:list-item>
<text:list text:style-name="a404">
<text:list-item>
<text:p text:style-name="a403" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a402" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a407">
<text:list-item>
<text:list text:style-name="a407">
<text:list-item>
<text:list text:style-name="a407">
<text:list-item>
<text:p text:style-name="a406" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a405" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a410">
<text:list-item>
<text:list text:style-name="a410">
<text:list-item>
<text:list text:style-name="a410">
<text:list-item>
<text:list text:style-name="a410">
<text:list-item>
<text:p text:style-name="a409" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a408" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a413">
<text:list-item>
<text:list text:style-name="a413">
<text:list-item>
<text:list text:style-name="a413">
<text:list-item>
<text:list text:style-name="a413">
<text:list-item>
<text:list text:style-name="a413">
<text:list-item>
<text:p text:style-name="a412" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a411" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id71" presentation:style-name="a418" draw:name="Date Placeholder 4" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a417" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a415" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a416">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id72" presentation:style-name="a421" draw:name="Footer Placeholder 5" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a420" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a419" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id73" presentation:style-name="a424" draw:name="Slide Number Placeholder 6" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a423" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a422" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL14():
    
    """Build Element style:master-page for Master1-PPL14 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout14-txOverObj-Title-and-Text-over-Content" style:page-layout-name="pageLayout1" draw:style-name="a426">
<draw:frame draw:id="id74" presentation:style-name="a429" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a428" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a427" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id75" presentation:style-name="a445" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="2.39063in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a432">
<text:list-item>
<text:p text:style-name="a431" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a430" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a435">
<text:list-item>
<text:list text:style-name="a435">
<text:list-item>
<text:p text:style-name="a434" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a433" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a438">
<text:list-item>
<text:list text:style-name="a438">
<text:list-item>
<text:list text:style-name="a438">
<text:list-item>
<text:p text:style-name="a437" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a436" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a441">
<text:list-item>
<text:list text:style-name="a441">
<text:list-item>
<text:list text:style-name="a441">
<text:list-item>
<text:list text:style-name="a441">
<text:list-item>
<text:p text:style-name="a440" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a439" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a444">
<text:list-item>
<text:list text:style-name="a444">
<text:list-item>
<text:list text:style-name="a444">
<text:list-item>
<text:list text:style-name="a444">
<text:list-item>
<text:list text:style-name="a444">
<text:list-item>
<text:p text:style-name="a443" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a442" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id76" presentation:style-name="a461" draw:name="Content Placeholder 3" svg:x="0.5in" svg:y="4.30729in" svg:width="9in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a448">
<text:list-item>
<text:p text:style-name="a447" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a446" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a451">
<text:list-item>
<text:list text:style-name="a451">
<text:list-item>
<text:p text:style-name="a450" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a449" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a454">
<text:list-item>
<text:list text:style-name="a454">
<text:list-item>
<text:list text:style-name="a454">
<text:list-item>
<text:p text:style-name="a453" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a452" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a457">
<text:list-item>
<text:list text:style-name="a457">
<text:list-item>
<text:list text:style-name="a457">
<text:list-item>
<text:list text:style-name="a457">
<text:list-item>
<text:p text:style-name="a456" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a455" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a460">
<text:list-item>
<text:list text:style-name="a460">
<text:list-item>
<text:list text:style-name="a460">
<text:list-item>
<text:list text:style-name="a460">
<text:list-item>
<text:list text:style-name="a460">
<text:list-item>
<text:p text:style-name="a459" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a458" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id77" presentation:style-name="a465" draw:name="Date Placeholder 4" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a464" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a462" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a463">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id78" presentation:style-name="a468" draw:name="Footer Placeholder 5" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a467" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a466" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id79" presentation:style-name="a471" draw:name="Slide Number Placeholder 6" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a470" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a469" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL15():
    
    """Build Element style:master-page for Master1-PPL15 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout15-txAndObj-Title,-Text,-and-Content" style:page-layout-name="pageLayout1" draw:style-name="a473">
<draw:frame draw:id="id80" presentation:style-name="a476" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a475" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a474" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id81" presentation:style-name="a492" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a479">
<text:list-item>
<text:p text:style-name="a478" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a477" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a482">
<text:list-item>
<text:list text:style-name="a482">
<text:list-item>
<text:p text:style-name="a481" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a480" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a485">
<text:list-item>
<text:list text:style-name="a485">
<text:list-item>
<text:list text:style-name="a485">
<text:list-item>
<text:p text:style-name="a484" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a483" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a488">
<text:list-item>
<text:list text:style-name="a488">
<text:list-item>
<text:list text:style-name="a488">
<text:list-item>
<text:list text:style-name="a488">
<text:list-item>
<text:p text:style-name="a487" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a486" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a491">
<text:list-item>
<text:list text:style-name="a491">
<text:list-item>
<text:list text:style-name="a491">
<text:list-item>
<text:list text:style-name="a491">
<text:list-item>
<text:list text:style-name="a491">
<text:list-item>
<text:p text:style-name="a490" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a489" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id82" presentation:style-name="a508" draw:name="Content Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a495">
<text:list-item>
<text:p text:style-name="a494" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a493" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a498">
<text:list-item>
<text:list text:style-name="a498">
<text:list-item>
<text:p text:style-name="a497" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a496" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a501">
<text:list-item>
<text:list text:style-name="a501">
<text:list-item>
<text:list text:style-name="a501">
<text:list-item>
<text:p text:style-name="a500" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a499" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a504">
<text:list-item>
<text:list text:style-name="a504">
<text:list-item>
<text:list text:style-name="a504">
<text:list-item>
<text:list text:style-name="a504">
<text:list-item>
<text:p text:style-name="a503" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a502" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a507">
<text:list-item>
<text:list text:style-name="a507">
<text:list-item>
<text:list text:style-name="a507">
<text:list-item>
<text:list text:style-name="a507">
<text:list-item>
<text:list text:style-name="a507">
<text:list-item>
<text:p text:style-name="a506" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a505" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id83" presentation:style-name="a512" draw:name="Date Placeholder 4" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a511" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a509" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a510">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id84" presentation:style-name="a515" draw:name="Footer Placeholder 5" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a514" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a513" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id85" presentation:style-name="a518" draw:name="Slide Number Placeholder 6" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a517" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a516" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL16():
    
    """Build Element style:master-page for Master1-PPL16 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout16-objAndTx-Title,-Content-and-Text" style:page-layout-name="pageLayout1" draw:style-name="a520">
<draw:frame draw:id="id86" presentation:style-name="a523" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a522" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a521" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id87" presentation:style-name="a539" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a526">
<text:list-item>
<text:p text:style-name="a525" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a524" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a529">
<text:list-item>
<text:list text:style-name="a529">
<text:list-item>
<text:p text:style-name="a528" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a527" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a532">
<text:list-item>
<text:list text:style-name="a532">
<text:list-item>
<text:list text:style-name="a532">
<text:list-item>
<text:p text:style-name="a531" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a530" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a535">
<text:list-item>
<text:list text:style-name="a535">
<text:list-item>
<text:list text:style-name="a535">
<text:list-item>
<text:list text:style-name="a535">
<text:list-item>
<text:p text:style-name="a534" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a533" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a538">
<text:list-item>
<text:list text:style-name="a538">
<text:list-item>
<text:list text:style-name="a538">
<text:list-item>
<text:list text:style-name="a538">
<text:list-item>
<text:list text:style-name="a538">
<text:list-item>
<text:p text:style-name="a537" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a536" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id88" presentation:style-name="a555" draw:name="Text Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a542">
<text:list-item>
<text:p text:style-name="a541" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a540" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a545">
<text:list-item>
<text:list text:style-name="a545">
<text:list-item>
<text:p text:style-name="a544" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a543" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a548">
<text:list-item>
<text:list text:style-name="a548">
<text:list-item>
<text:list text:style-name="a548">
<text:list-item>
<text:p text:style-name="a547" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a546" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a551">
<text:list-item>
<text:list text:style-name="a551">
<text:list-item>
<text:list text:style-name="a551">
<text:list-item>
<text:list text:style-name="a551">
<text:list-item>
<text:p text:style-name="a550" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a549" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a554">
<text:list-item>
<text:list text:style-name="a554">
<text:list-item>
<text:list text:style-name="a554">
<text:list-item>
<text:list text:style-name="a554">
<text:list-item>
<text:list text:style-name="a554">
<text:list-item>
<text:p text:style-name="a553" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a552" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id89" presentation:style-name="a559" draw:name="Date Placeholder 4" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a558" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a556" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a557">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id90" presentation:style-name="a562" draw:name="Footer Placeholder 5" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a561" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a560" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id91" presentation:style-name="a565" draw:name="Slide Number Placeholder 6" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a564" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a563" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL17():
    
    """Build Element style:master-page for Master1-PPL17 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout17-txAndTwoObj-Title,-Text,-and-2-Content" style:page-layout-name="pageLayout1" draw:style-name="a567">
<draw:frame draw:id="id92" presentation:style-name="a570" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a569" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a568" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id93" presentation:style-name="a586" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a573">
<text:list-item>
<text:p text:style-name="a572" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a571" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a576">
<text:list-item>
<text:list text:style-name="a576">
<text:list-item>
<text:p text:style-name="a575" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a574" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a579">
<text:list-item>
<text:list text:style-name="a579">
<text:list-item>
<text:list text:style-name="a579">
<text:list-item>
<text:p text:style-name="a578" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a577" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a582">
<text:list-item>
<text:list text:style-name="a582">
<text:list-item>
<text:list text:style-name="a582">
<text:list-item>
<text:list text:style-name="a582">
<text:list-item>
<text:p text:style-name="a581" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a580" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a585">
<text:list-item>
<text:list text:style-name="a585">
<text:list-item>
<text:list text:style-name="a585">
<text:list-item>
<text:list text:style-name="a585">
<text:list-item>
<text:list text:style-name="a585">
<text:list-item>
<text:p text:style-name="a584" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a583" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id94" presentation:style-name="a602" draw:name="Content Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a589">
<text:list-item>
<text:p text:style-name="a588" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a587" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a592">
<text:list-item>
<text:list text:style-name="a592">
<text:list-item>
<text:p text:style-name="a591" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a590" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a595">
<text:list-item>
<text:list text:style-name="a595">
<text:list-item>
<text:list text:style-name="a595">
<text:list-item>
<text:p text:style-name="a594" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a593" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a598">
<text:list-item>
<text:list text:style-name="a598">
<text:list-item>
<text:list text:style-name="a598">
<text:list-item>
<text:list text:style-name="a598">
<text:list-item>
<text:p text:style-name="a597" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a596" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a601">
<text:list-item>
<text:list text:style-name="a601">
<text:list-item>
<text:list text:style-name="a601">
<text:list-item>
<text:list text:style-name="a601">
<text:list-item>
<text:list text:style-name="a601">
<text:list-item>
<text:p text:style-name="a600" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a599" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id95" presentation:style-name="a618" draw:name="Content Placeholder 4" svg:x="5.08333in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a605">
<text:list-item>
<text:p text:style-name="a604" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a603" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a608">
<text:list-item>
<text:list text:style-name="a608">
<text:list-item>
<text:p text:style-name="a607" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a606" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a611">
<text:list-item>
<text:list text:style-name="a611">
<text:list-item>
<text:list text:style-name="a611">
<text:list-item>
<text:p text:style-name="a610" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a609" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a614">
<text:list-item>
<text:list text:style-name="a614">
<text:list-item>
<text:list text:style-name="a614">
<text:list-item>
<text:list text:style-name="a614">
<text:list-item>
<text:p text:style-name="a613" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a612" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a617">
<text:list-item>
<text:list text:style-name="a617">
<text:list-item>
<text:list text:style-name="a617">
<text:list-item>
<text:list text:style-name="a617">
<text:list-item>
<text:list text:style-name="a617">
<text:list-item>
<text:p text:style-name="a616" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a615" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id96" presentation:style-name="a622" draw:name="Date Placeholder 5" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a621" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a619" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a620">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id97" presentation:style-name="a625" draw:name="Footer Placeholder 6" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a624" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a623" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id98" presentation:style-name="a628" draw:name="Slide Number Placeholder 7" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a627" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a626" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL18():
    
    """Build Element style:master-page for Master1-PPL18 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout18-objAndTwoObj-Title,-Content,-and-2-Content" style:page-layout-name="pageLayout1" draw:style-name="a630">
<draw:frame draw:id="id99" presentation:style-name="a633" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a632" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a631" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id100" presentation:style-name="a649" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a636">
<text:list-item>
<text:p text:style-name="a635" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a634" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a639">
<text:list-item>
<text:list text:style-name="a639">
<text:list-item>
<text:p text:style-name="a638" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a637" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a642">
<text:list-item>
<text:list text:style-name="a642">
<text:list-item>
<text:list text:style-name="a642">
<text:list-item>
<text:p text:style-name="a641" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a640" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a645">
<text:list-item>
<text:list text:style-name="a645">
<text:list-item>
<text:list text:style-name="a645">
<text:list-item>
<text:list text:style-name="a645">
<text:list-item>
<text:p text:style-name="a644" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a643" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a648">
<text:list-item>
<text:list text:style-name="a648">
<text:list-item>
<text:list text:style-name="a648">
<text:list-item>
<text:list text:style-name="a648">
<text:list-item>
<text:list text:style-name="a648">
<text:list-item>
<text:p text:style-name="a647" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a646" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id101" presentation:style-name="a665" draw:name="Content Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a652">
<text:list-item>
<text:p text:style-name="a651" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a650" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a655">
<text:list-item>
<text:list text:style-name="a655">
<text:list-item>
<text:p text:style-name="a654" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a653" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a658">
<text:list-item>
<text:list text:style-name="a658">
<text:list-item>
<text:list text:style-name="a658">
<text:list-item>
<text:p text:style-name="a657" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a656" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a661">
<text:list-item>
<text:list text:style-name="a661">
<text:list-item>
<text:list text:style-name="a661">
<text:list-item>
<text:list text:style-name="a661">
<text:list-item>
<text:p text:style-name="a660" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a659" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a664">
<text:list-item>
<text:list text:style-name="a664">
<text:list-item>
<text:list text:style-name="a664">
<text:list-item>
<text:list text:style-name="a664">
<text:list-item>
<text:list text:style-name="a664">
<text:list-item>
<text:p text:style-name="a663" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a662" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id102" presentation:style-name="a681" draw:name="Content Placeholder 4" svg:x="5.08333in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a668">
<text:list-item>
<text:p text:style-name="a667" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a666" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a671">
<text:list-item>
<text:list text:style-name="a671">
<text:list-item>
<text:p text:style-name="a670" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a669" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a674">
<text:list-item>
<text:list text:style-name="a674">
<text:list-item>
<text:list text:style-name="a674">
<text:list-item>
<text:p text:style-name="a673" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a672" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a677">
<text:list-item>
<text:list text:style-name="a677">
<text:list-item>
<text:list text:style-name="a677">
<text:list-item>
<text:list text:style-name="a677">
<text:list-item>
<text:p text:style-name="a676" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a675" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a680">
<text:list-item>
<text:list text:style-name="a680">
<text:list-item>
<text:list text:style-name="a680">
<text:list-item>
<text:list text:style-name="a680">
<text:list-item>
<text:list text:style-name="a680">
<text:list-item>
<text:p text:style-name="a679" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a678" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id103" presentation:style-name="a685" draw:name="Date Placeholder 5" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a684" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a682" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a683">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id104" presentation:style-name="a688" draw:name="Footer Placeholder 6" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a687" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a686" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id105" presentation:style-name="a691" draw:name="Slide Number Placeholder 7" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a690" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a689" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL19():
    
    """Build Element style:master-page for Master1-PPL19 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout19-objOverTx-Title-and-Content-over-Text" style:page-layout-name="pageLayout1" draw:style-name="a693">
<draw:frame draw:id="id106" presentation:style-name="a696" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a695" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a694" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id107" presentation:style-name="a712" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a699">
<text:list-item>
<text:p text:style-name="a698" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a697" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a702">
<text:list-item>
<text:list text:style-name="a702">
<text:list-item>
<text:p text:style-name="a701" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a700" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a705">
<text:list-item>
<text:list text:style-name="a705">
<text:list-item>
<text:list text:style-name="a705">
<text:list-item>
<text:p text:style-name="a704" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a703" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a708">
<text:list-item>
<text:list text:style-name="a708">
<text:list-item>
<text:list text:style-name="a708">
<text:list-item>
<text:list text:style-name="a708">
<text:list-item>
<text:p text:style-name="a707" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a706" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a711">
<text:list-item>
<text:list text:style-name="a711">
<text:list-item>
<text:list text:style-name="a711">
<text:list-item>
<text:list text:style-name="a711">
<text:list-item>
<text:list text:style-name="a711">
<text:list-item>
<text:p text:style-name="a710" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a709" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id108" presentation:style-name="a728" draw:name="Text Placeholder 3" svg:x="0.5in" svg:y="4.30729in" svg:width="9in" svg:height="2.39236in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a715">
<text:list-item>
<text:p text:style-name="a714" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a713" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a718">
<text:list-item>
<text:list text:style-name="a718">
<text:list-item>
<text:p text:style-name="a717" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a716" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a721">
<text:list-item>
<text:list text:style-name="a721">
<text:list-item>
<text:list text:style-name="a721">
<text:list-item>
<text:p text:style-name="a720" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a719" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a724">
<text:list-item>
<text:list text:style-name="a724">
<text:list-item>
<text:list text:style-name="a724">
<text:list-item>
<text:list text:style-name="a724">
<text:list-item>
<text:p text:style-name="a723" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a722" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a727">
<text:list-item>
<text:list text:style-name="a727">
<text:list-item>
<text:list text:style-name="a727">
<text:list-item>
<text:list text:style-name="a727">
<text:list-item>
<text:list text:style-name="a727">
<text:list-item>
<text:p text:style-name="a726" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a725" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id109" presentation:style-name="a732" draw:name="Date Placeholder 4" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a731" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a729" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a730">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id110" presentation:style-name="a735" draw:name="Footer Placeholder 5" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a734" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a733" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id111" presentation:style-name="a738" draw:name="Slide Number Placeholder 6" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a737" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a736" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL20():
    
    """Build Element style:master-page for Master1-PPL20 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout20-fourObj-Title-and-4-Content" style:page-layout-name="pageLayout1" draw:style-name="a740">
<draw:frame draw:id="id112" presentation:style-name="a743" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a742" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a741" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id113" presentation:style-name="a759" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a746">
<text:list-item>
<text:p text:style-name="a745" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a744" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a749">
<text:list-item>
<text:list text:style-name="a749">
<text:list-item>
<text:p text:style-name="a748" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a747" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a752">
<text:list-item>
<text:list text:style-name="a752">
<text:list-item>
<text:list text:style-name="a752">
<text:list-item>
<text:p text:style-name="a751" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a750" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a755">
<text:list-item>
<text:list text:style-name="a755">
<text:list-item>
<text:list text:style-name="a755">
<text:list-item>
<text:list text:style-name="a755">
<text:list-item>
<text:p text:style-name="a754" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a753" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a758">
<text:list-item>
<text:list text:style-name="a758">
<text:list-item>
<text:list text:style-name="a758">
<text:list-item>
<text:list text:style-name="a758">
<text:list-item>
<text:list text:style-name="a758">
<text:list-item>
<text:p text:style-name="a757" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a756" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id114" presentation:style-name="a775" draw:name="Content Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a762">
<text:list-item>
<text:p text:style-name="a761" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a760" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a765">
<text:list-item>
<text:list text:style-name="a765">
<text:list-item>
<text:p text:style-name="a764" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a763" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a768">
<text:list-item>
<text:list text:style-name="a768">
<text:list-item>
<text:list text:style-name="a768">
<text:list-item>
<text:p text:style-name="a767" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a766" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a771">
<text:list-item>
<text:list text:style-name="a771">
<text:list-item>
<text:list text:style-name="a771">
<text:list-item>
<text:list text:style-name="a771">
<text:list-item>
<text:p text:style-name="a770" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a769" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a774">
<text:list-item>
<text:list text:style-name="a774">
<text:list-item>
<text:list text:style-name="a774">
<text:list-item>
<text:list text:style-name="a774">
<text:list-item>
<text:list text:style-name="a774">
<text:list-item>
<text:p text:style-name="a773" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a772" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id115" presentation:style-name="a791" draw:name="Content Placeholder 4" svg:x="0.5in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a778">
<text:list-item>
<text:p text:style-name="a777" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a776" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a781">
<text:list-item>
<text:list text:style-name="a781">
<text:list-item>
<text:p text:style-name="a780" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a779" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a784">
<text:list-item>
<text:list text:style-name="a784">
<text:list-item>
<text:list text:style-name="a784">
<text:list-item>
<text:p text:style-name="a783" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a782" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a787">
<text:list-item>
<text:list text:style-name="a787">
<text:list-item>
<text:list text:style-name="a787">
<text:list-item>
<text:list text:style-name="a787">
<text:list-item>
<text:p text:style-name="a786" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a785" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a790">
<text:list-item>
<text:list text:style-name="a790">
<text:list-item>
<text:list text:style-name="a790">
<text:list-item>
<text:list text:style-name="a790">
<text:list-item>
<text:list text:style-name="a790">
<text:list-item>
<text:p text:style-name="a789" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a788" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id116" presentation:style-name="a807" draw:name="Content Placeholder 5" svg:x="5.08333in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a794">
<text:list-item>
<text:p text:style-name="a793" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a792" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a797">
<text:list-item>
<text:list text:style-name="a797">
<text:list-item>
<text:p text:style-name="a796" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a795" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a800">
<text:list-item>
<text:list text:style-name="a800">
<text:list-item>
<text:list text:style-name="a800">
<text:list-item>
<text:p text:style-name="a799" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a798" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a803">
<text:list-item>
<text:list text:style-name="a803">
<text:list-item>
<text:list text:style-name="a803">
<text:list-item>
<text:list text:style-name="a803">
<text:list-item>
<text:p text:style-name="a802" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a801" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a806">
<text:list-item>
<text:list text:style-name="a806">
<text:list-item>
<text:list text:style-name="a806">
<text:list-item>
<text:list text:style-name="a806">
<text:list-item>
<text:list text:style-name="a806">
<text:list-item>
<text:p text:style-name="a805" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a804" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id117" presentation:style-name="a811" draw:name="Date Placeholder 6" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a810" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a808" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a809">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id118" presentation:style-name="a814" draw:name="Footer Placeholder 7" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a813" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a812" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id119" presentation:style-name="a817" draw:name="Slide Number Placeholder 8" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a816" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a815" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL21():
    
    """Build Element style:master-page for Master1-PPL21 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout21-twoObjAndObj-Title,-2-Content-and-Content" style:page-layout-name="pageLayout1" draw:style-name="a819">
<draw:frame draw:id="id120" presentation:style-name="a822" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a821" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a820" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id121" presentation:style-name="a838" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a825">
<text:list-item>
<text:p text:style-name="a824" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a823" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a828">
<text:list-item>
<text:list text:style-name="a828">
<text:list-item>
<text:p text:style-name="a827" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a826" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a831">
<text:list-item>
<text:list text:style-name="a831">
<text:list-item>
<text:list text:style-name="a831">
<text:list-item>
<text:p text:style-name="a830" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a829" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a834">
<text:list-item>
<text:list text:style-name="a834">
<text:list-item>
<text:list text:style-name="a834">
<text:list-item>
<text:list text:style-name="a834">
<text:list-item>
<text:p text:style-name="a833" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a832" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a837">
<text:list-item>
<text:list text:style-name="a837">
<text:list-item>
<text:list text:style-name="a837">
<text:list-item>
<text:list text:style-name="a837">
<text:list-item>
<text:list text:style-name="a837">
<text:list-item>
<text:p text:style-name="a836" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a835" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id122" presentation:style-name="a854" draw:name="Content Placeholder 3" svg:x="0.5in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a841">
<text:list-item>
<text:p text:style-name="a840" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a839" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a844">
<text:list-item>
<text:list text:style-name="a844">
<text:list-item>
<text:p text:style-name="a843" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a842" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a847">
<text:list-item>
<text:list text:style-name="a847">
<text:list-item>
<text:list text:style-name="a847">
<text:list-item>
<text:p text:style-name="a846" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a845" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a850">
<text:list-item>
<text:list text:style-name="a850">
<text:list-item>
<text:list text:style-name="a850">
<text:list-item>
<text:list text:style-name="a850">
<text:list-item>
<text:p text:style-name="a849" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a848" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a853">
<text:list-item>
<text:list text:style-name="a853">
<text:list-item>
<text:list text:style-name="a853">
<text:list-item>
<text:list text:style-name="a853">
<text:list-item>
<text:list text:style-name="a853">
<text:list-item>
<text:p text:style-name="a852" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a851" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id123" presentation:style-name="a870" draw:name="Content Placeholder 4" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a857">
<text:list-item>
<text:p text:style-name="a856" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a855" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a860">
<text:list-item>
<text:list text:style-name="a860">
<text:list-item>
<text:p text:style-name="a859" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a858" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a863">
<text:list-item>
<text:list text:style-name="a863">
<text:list-item>
<text:list text:style-name="a863">
<text:list-item>
<text:p text:style-name="a862" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a861" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a866">
<text:list-item>
<text:list text:style-name="a866">
<text:list-item>
<text:list text:style-name="a866">
<text:list-item>
<text:list text:style-name="a866">
<text:list-item>
<text:p text:style-name="a865" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a864" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a869">
<text:list-item>
<text:list text:style-name="a869">
<text:list-item>
<text:list text:style-name="a869">
<text:list-item>
<text:list text:style-name="a869">
<text:list-item>
<text:list text:style-name="a869">
<text:list-item>
<text:p text:style-name="a868" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a867" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id124" presentation:style-name="a874" draw:name="Date Placeholder 5" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a873" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a871" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a872">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id125" presentation:style-name="a877" draw:name="Footer Placeholder 6" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a876" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a875" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id126" presentation:style-name="a880" draw:name="Slide Number Placeholder 7" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a879" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a878" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL22():
    
    """Build Element style:master-page for Master1-PPL22 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout22-twoObjAndTx-Title,-2-Content-and-Text" style:page-layout-name="pageLayout1" draw:style-name="a882">
<draw:frame draw:id="id127" presentation:style-name="a885" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a884" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a883" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id128" presentation:style-name="a901" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a888">
<text:list-item>
<text:p text:style-name="a887" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a886" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a891">
<text:list-item>
<text:list text:style-name="a891">
<text:list-item>
<text:p text:style-name="a890" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a889" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a894">
<text:list-item>
<text:list text:style-name="a894">
<text:list-item>
<text:list text:style-name="a894">
<text:list-item>
<text:p text:style-name="a893" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a892" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a897">
<text:list-item>
<text:list text:style-name="a897">
<text:list-item>
<text:list text:style-name="a897">
<text:list-item>
<text:list text:style-name="a897">
<text:list-item>
<text:p text:style-name="a896" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a895" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a900">
<text:list-item>
<text:list text:style-name="a900">
<text:list-item>
<text:list text:style-name="a900">
<text:list-item>
<text:list text:style-name="a900">
<text:list-item>
<text:list text:style-name="a900">
<text:list-item>
<text:p text:style-name="a899" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a898" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id129" presentation:style-name="a917" draw:name="Content Placeholder 3" svg:x="0.5in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a904">
<text:list-item>
<text:p text:style-name="a903" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a902" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a907">
<text:list-item>
<text:list text:style-name="a907">
<text:list-item>
<text:p text:style-name="a906" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a905" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a910">
<text:list-item>
<text:list text:style-name="a910">
<text:list-item>
<text:list text:style-name="a910">
<text:list-item>
<text:p text:style-name="a909" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a908" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a913">
<text:list-item>
<text:list text:style-name="a913">
<text:list-item>
<text:list text:style-name="a913">
<text:list-item>
<text:list text:style-name="a913">
<text:list-item>
<text:p text:style-name="a912" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a911" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a916">
<text:list-item>
<text:list text:style-name="a916">
<text:list-item>
<text:list text:style-name="a916">
<text:list-item>
<text:list text:style-name="a916">
<text:list-item>
<text:list text:style-name="a916">
<text:list-item>
<text:p text:style-name="a915" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a914" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id130" presentation:style-name="a933" draw:name="Text Placeholder 4" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a920">
<text:list-item>
<text:p text:style-name="a919" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a918" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a923">
<text:list-item>
<text:list text:style-name="a923">
<text:list-item>
<text:p text:style-name="a922" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a921" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a926">
<text:list-item>
<text:list text:style-name="a926">
<text:list-item>
<text:list text:style-name="a926">
<text:list-item>
<text:p text:style-name="a925" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a924" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a929">
<text:list-item>
<text:list text:style-name="a929">
<text:list-item>
<text:list text:style-name="a929">
<text:list-item>
<text:list text:style-name="a929">
<text:list-item>
<text:p text:style-name="a928" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a927" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a932">
<text:list-item>
<text:list text:style-name="a932">
<text:list-item>
<text:list text:style-name="a932">
<text:list-item>
<text:list text:style-name="a932">
<text:list-item>
<text:list text:style-name="a932">
<text:list-item>
<text:p text:style-name="a931" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a930" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id131" presentation:style-name="a937" draw:name="Date Placeholder 5" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a936" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a934" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a935">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id132" presentation:style-name="a940" draw:name="Footer Placeholder 6" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a939" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a938" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id133" presentation:style-name="a943" draw:name="Slide Number Placeholder 7" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a942" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a941" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL23():
    
    """Build Element style:master-page for Master1-PPL23 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout23-twoObjOverTx-Title-and-2-Content-over-Text" style:page-layout-name="pageLayout1" draw:style-name="a945">
<draw:frame draw:id="id134" presentation:style-name="a948" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a947" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a946" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id135" presentation:style-name="a964" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a951">
<text:list-item>
<text:p text:style-name="a950" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a949" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a954">
<text:list-item>
<text:list text:style-name="a954">
<text:list-item>
<text:p text:style-name="a953" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a952" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a957">
<text:list-item>
<text:list text:style-name="a957">
<text:list-item>
<text:list text:style-name="a957">
<text:list-item>
<text:p text:style-name="a956" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a955" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a960">
<text:list-item>
<text:list text:style-name="a960">
<text:list-item>
<text:list text:style-name="a960">
<text:list-item>
<text:list text:style-name="a960">
<text:list-item>
<text:p text:style-name="a959" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a958" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a963">
<text:list-item>
<text:list text:style-name="a963">
<text:list-item>
<text:list text:style-name="a963">
<text:list-item>
<text:list text:style-name="a963">
<text:list-item>
<text:list text:style-name="a963">
<text:list-item>
<text:p text:style-name="a962" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a961" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id136" presentation:style-name="a980" draw:name="Content Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a967">
<text:list-item>
<text:p text:style-name="a966" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a965" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a970">
<text:list-item>
<text:list text:style-name="a970">
<text:list-item>
<text:p text:style-name="a969" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a968" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a973">
<text:list-item>
<text:list text:style-name="a973">
<text:list-item>
<text:list text:style-name="a973">
<text:list-item>
<text:p text:style-name="a972" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a971" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a976">
<text:list-item>
<text:list text:style-name="a976">
<text:list-item>
<text:list text:style-name="a976">
<text:list-item>
<text:list text:style-name="a976">
<text:list-item>
<text:p text:style-name="a975" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a974" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a979">
<text:list-item>
<text:list text:style-name="a979">
<text:list-item>
<text:list text:style-name="a979">
<text:list-item>
<text:list text:style-name="a979">
<text:list-item>
<text:list text:style-name="a979">
<text:list-item>
<text:p text:style-name="a978" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a977" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id137" presentation:style-name="a996" draw:name="Text Placeholder 4" svg:x="0.5in" svg:y="4.30729in" svg:width="9in" svg:height="2.39236in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a983">
<text:list-item>
<text:p text:style-name="a982" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a981" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a986">
<text:list-item>
<text:list text:style-name="a986">
<text:list-item>
<text:p text:style-name="a985" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a984" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a989">
<text:list-item>
<text:list text:style-name="a989">
<text:list-item>
<text:list text:style-name="a989">
<text:list-item>
<text:p text:style-name="a988" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a987" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a992">
<text:list-item>
<text:list text:style-name="a992">
<text:list-item>
<text:list text:style-name="a992">
<text:list-item>
<text:list text:style-name="a992">
<text:list-item>
<text:p text:style-name="a991" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a990" text:class-names="">
Fourth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a995">
<text:list-item>
<text:list text:style-name="a995">
<text:list-item>
<text:list text:style-name="a995">
<text:list-item>
<text:list text:style-name="a995">
<text:list-item>
<text:list text:style-name="a995">
<text:list-item>
<text:p text:style-name="a994" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a993" text:class-names="">
Fifth level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id138" presentation:style-name="a1000" draw:name="Date Placeholder 5" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a999" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a997" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a998">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id139" presentation:style-name="a1003" draw:name="Footer Placeholder 6" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1002" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1001" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id140" presentation:style-name="a1006" draw:name="Slide Number Placeholder 7" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1005" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1004" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem

def style_8_master_page_Master1_PPL24():
    
    """Build Element style:master-page for Master1-PPL24 """
    
    elem = build_element( """<style:master-page style:name="Master1-Layout24-tbl-Title-and-Table" style:page-layout-name="pageLayout1" draw:style-name="a1008">
<draw:frame draw:id="id141" presentation:style-name="a1011" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1010" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1009" text:class-names="">
Click to edit Master title style</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id142" presentation:style-name="a1015" draw:name="Table Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="4.94965in" presentation:class="table" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1014">
<text:list-item>
<text:p text:style-name="a1013" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1012" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id143" presentation:style-name="a1019" draw:name="Date Placeholder 3" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1018" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1016" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a1017">
10/30/2015</text:date>
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id144" presentation:style-name="a1022" draw:name="Footer Placeholder 4" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1021" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1020" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id145" presentation:style-name="a1025" draw:name="Slide Number Placeholder 5" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1024" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1023" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</style:master-page>
""" )
    
    return elem



# Set values in func_quick_lookupD
func_quick_lookupD["Master1-PPL1"] = style_8_master_page_Master1_PPL1
func_quick_lookupD["Master1-PPL12"] = style_8_master_page_Master1_PPL12
func_quick_lookupD["Master1-PPL13"] = style_8_master_page_Master1_PPL13
func_quick_lookupD["Master1-PPL14"] = style_8_master_page_Master1_PPL14
func_quick_lookupD["Master1-PPL15"] = style_8_master_page_Master1_PPL15
func_quick_lookupD["Master1-PPL16"] = style_8_master_page_Master1_PPL16
func_quick_lookupD["Master1-PPL17"] = style_8_master_page_Master1_PPL17
func_quick_lookupD["Master1-PPL18"] = style_8_master_page_Master1_PPL18
func_quick_lookupD["Master1-PPL19"] = style_8_master_page_Master1_PPL19
func_quick_lookupD["Master1-PPL2"] = style_8_master_page_Master1_PPL2
func_quick_lookupD["Master1-PPL20"] = style_8_master_page_Master1_PPL20
func_quick_lookupD["Master1-PPL21"] = style_8_master_page_Master1_PPL21
func_quick_lookupD["Master1-PPL22"] = style_8_master_page_Master1_PPL22
func_quick_lookupD["Master1-PPL23"] = style_8_master_page_Master1_PPL23
func_quick_lookupD["Master1-PPL24"] = style_8_master_page_Master1_PPL24
func_quick_lookupD["Master1-PPL4"] = style_8_master_page_Master1_PPL4
func_quick_lookupD["draw_8_layer_set"] = draw_8_layer_set



if __name__ == "__main__":
    print( func_quick_lookupD["Master1-PPL24"]() )
