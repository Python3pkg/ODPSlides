
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout1-title-Title-Slide" style:page-layout-name="pageLayout1" draw:style-name="a34">
<draw:frame draw:id="id5" presentation:style-name="a38" draw:name="Title 1" svg:x="0.75in" svg:y="2.32986in" svg:width="8.5in" svg:height="1.60764in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a37" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a35" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a36" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id6" presentation:style-name="a42" draw:name="Subtitle 2" svg:x="1.5in" svg:y="4.25in" svg:width="7in" svg:height="1.91667in" presentation:class="subtitle" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a41" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a39" text:class-names="">
Click to edit Master subtitle style</text:span>
<text:span text:style-name="a40" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id7" presentation:style-name="a47" draw:name="Date Placeholder 3" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a46" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a43" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a44" />
</text:span>
<text:span text:style-name="a45" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id8" presentation:style-name="a50" draw:name="Footer Placeholder 4" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a49" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a48" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id9" presentation:style-name="a54" draw:name="Slide Number Placeholder 5" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a53" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a51" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a52" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout2-obj-Title-and-Content" style:page-layout-name="pageLayout1" draw:style-name="a55">
<draw:frame draw:id="id10" presentation:style-name="a59" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a58" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a56" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a57" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id11" presentation:style-name="a76" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a62">
<text:list-item>
<text:p text:style-name="a61" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a60" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a65">
<text:list-item>
<text:list text:style-name="a65">
<text:list-item>
<text:p text:style-name="a64" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a63" text:class-names="">
Second level</text:span>
</text:p>
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
<text:p text:style-name="a67" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a66" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a71">
<text:list-item>
<text:list text:style-name="a71">
<text:list-item>
<text:list text:style-name="a71">
<text:list-item>
<text:list text:style-name="a71">
<text:list-item>
<text:p text:style-name="a70" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a69" text:class-names="">
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
<text:list text:style-name="a75">
<text:list-item>
<text:list text:style-name="a75">
<text:list-item>
<text:list text:style-name="a75">
<text:list-item>
<text:list text:style-name="a75">
<text:list-item>
<text:list text:style-name="a75">
<text:list-item>
<text:p text:style-name="a74" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a72" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a73" text:class-names="" />
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
<draw:frame draw:id="id12" presentation:style-name="a81" draw:name="Date Placeholder 3" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a80" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a77" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a78" />
</text:span>
<text:span text:style-name="a79" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id13" presentation:style-name="a84" draw:name="Footer Placeholder 4" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a83" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a82" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id14" presentation:style-name="a88" draw:name="Slide Number Placeholder 5" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a87" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a85" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a86" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout4-twoObj-Two-Content" style:page-layout-name="pageLayout1" draw:style-name="a110">
<draw:frame draw:id="id20" presentation:style-name="a114" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a113" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a111" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a112" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id21" presentation:style-name="a131" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a117">
<text:list-item>
<text:p text:style-name="a116" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a115" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a120">
<text:list-item>
<text:list text:style-name="a120">
<text:list-item>
<text:p text:style-name="a119" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a118" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a123">
<text:list-item>
<text:list text:style-name="a123">
<text:list-item>
<text:list text:style-name="a123">
<text:list-item>
<text:p text:style-name="a122" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a121" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a126">
<text:list-item>
<text:list text:style-name="a126">
<text:list-item>
<text:list text:style-name="a126">
<text:list-item>
<text:list text:style-name="a126">
<text:list-item>
<text:p text:style-name="a125" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a124" text:class-names="">
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
<text:list text:style-name="a130">
<text:list-item>
<text:list text:style-name="a130">
<text:list-item>
<text:list text:style-name="a130">
<text:list-item>
<text:list text:style-name="a130">
<text:list-item>
<text:list text:style-name="a130">
<text:list-item>
<text:p text:style-name="a129" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a127" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a128" text:class-names="" />
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
<draw:frame draw:id="id22" presentation:style-name="a148" draw:name="Content Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a134">
<text:list-item>
<text:p text:style-name="a133" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a132" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a137">
<text:list-item>
<text:list text:style-name="a137">
<text:list-item>
<text:p text:style-name="a136" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a135" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a140">
<text:list-item>
<text:list text:style-name="a140">
<text:list-item>
<text:list text:style-name="a140">
<text:list-item>
<text:p text:style-name="a139" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a138" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a143">
<text:list-item>
<text:list text:style-name="a143">
<text:list-item>
<text:list text:style-name="a143">
<text:list-item>
<text:list text:style-name="a143">
<text:list-item>
<text:p text:style-name="a142" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a141" text:class-names="">
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
<text:list text:style-name="a147">
<text:list-item>
<text:list text:style-name="a147">
<text:list-item>
<text:list text:style-name="a147">
<text:list-item>
<text:list text:style-name="a147">
<text:list-item>
<text:list text:style-name="a147">
<text:list-item>
<text:p text:style-name="a146" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a144" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a145" text:class-names="" />
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
<draw:frame draw:id="id23" presentation:style-name="a153" draw:name="Date Placeholder 4" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a152" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a149" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a150" />
</text:span>
<text:span text:style-name="a151" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id24" presentation:style-name="a156" draw:name="Footer Placeholder 5" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a155" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a154" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id25" presentation:style-name="a160" draw:name="Slide Number Placeholder 6" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a159" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a157" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a158" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout12-tx-Title-and-Text" style:page-layout-name="pageLayout1" draw:style-name="a380">
<draw:frame draw:id="id63" presentation:style-name="a384" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a383" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a381" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a382" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id64" presentation:style-name="a401" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a387">
<text:list-item>
<text:p text:style-name="a386" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a385" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a390">
<text:list-item>
<text:list text:style-name="a390">
<text:list-item>
<text:p text:style-name="a389" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a388" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a393">
<text:list-item>
<text:list text:style-name="a393">
<text:list-item>
<text:list text:style-name="a393">
<text:list-item>
<text:p text:style-name="a392" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a391" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a396">
<text:list-item>
<text:list text:style-name="a396">
<text:list-item>
<text:list text:style-name="a396">
<text:list-item>
<text:list text:style-name="a396">
<text:list-item>
<text:p text:style-name="a395" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a394" text:class-names="">
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
<text:list text:style-name="a400">
<text:list-item>
<text:list text:style-name="a400">
<text:list-item>
<text:list text:style-name="a400">
<text:list-item>
<text:list text:style-name="a400">
<text:list-item>
<text:list text:style-name="a400">
<text:list-item>
<text:p text:style-name="a399" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a397" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a398" text:class-names="" />
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
<draw:frame draw:id="id65" presentation:style-name="a406" draw:name="Date Placeholder 3" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a405" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a402" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a403" />
</text:span>
<text:span text:style-name="a404" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id66" presentation:style-name="a409" draw:name="Footer Placeholder 4" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a408" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a407" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id67" presentation:style-name="a413" draw:name="Slide Number Placeholder 5" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a412" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a410" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a411" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout13-twoColTx-Title-and-2-Column-Text" style:page-layout-name="pageLayout1" draw:style-name="a414">
<draw:frame draw:id="id68" presentation:style-name="a418" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a417" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a415" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a416" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id69" presentation:style-name="a435" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a421">
<text:list-item>
<text:p text:style-name="a420" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a419" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a424">
<text:list-item>
<text:list text:style-name="a424">
<text:list-item>
<text:p text:style-name="a423" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a422" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a427">
<text:list-item>
<text:list text:style-name="a427">
<text:list-item>
<text:list text:style-name="a427">
<text:list-item>
<text:p text:style-name="a426" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a425" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a430">
<text:list-item>
<text:list text:style-name="a430">
<text:list-item>
<text:list text:style-name="a430">
<text:list-item>
<text:list text:style-name="a430">
<text:list-item>
<text:p text:style-name="a429" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a428" text:class-names="">
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
<text:list text:style-name="a434">
<text:list-item>
<text:list text:style-name="a434">
<text:list-item>
<text:list text:style-name="a434">
<text:list-item>
<text:list text:style-name="a434">
<text:list-item>
<text:list text:style-name="a434">
<text:list-item>
<text:p text:style-name="a433" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a431" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a432" text:class-names="" />
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
<draw:frame draw:id="id70" presentation:style-name="a452" draw:name="Text Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a438">
<text:list-item>
<text:p text:style-name="a437" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a436" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a441">
<text:list-item>
<text:list text:style-name="a441">
<text:list-item>
<text:p text:style-name="a440" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a439" text:class-names="">
Second level</text:span>
</text:p>
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
<text:p text:style-name="a443" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a442" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a447">
<text:list-item>
<text:list text:style-name="a447">
<text:list-item>
<text:list text:style-name="a447">
<text:list-item>
<text:list text:style-name="a447">
<text:list-item>
<text:p text:style-name="a446" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a445" text:class-names="">
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
<text:list text:style-name="a451">
<text:list-item>
<text:list text:style-name="a451">
<text:list-item>
<text:list text:style-name="a451">
<text:list-item>
<text:list text:style-name="a451">
<text:list-item>
<text:list text:style-name="a451">
<text:list-item>
<text:p text:style-name="a450" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a448" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a449" text:class-names="" />
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
<draw:frame draw:id="id71" presentation:style-name="a457" draw:name="Date Placeholder 4" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a456" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a453" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a454" />
</text:span>
<text:span text:style-name="a455" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id72" presentation:style-name="a460" draw:name="Footer Placeholder 5" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a459" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a458" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id73" presentation:style-name="a464" draw:name="Slide Number Placeholder 6" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a463" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a461" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a462" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout14-txOverObj-Title-and-Text-over-Content" style:page-layout-name="pageLayout1" draw:style-name="a465">
<draw:frame draw:id="id74" presentation:style-name="a469" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a468" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a466" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a467" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id75" presentation:style-name="a486" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="2.39063in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a472">
<text:list-item>
<text:p text:style-name="a471" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a470" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a475">
<text:list-item>
<text:list text:style-name="a475">
<text:list-item>
<text:p text:style-name="a474" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a473" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a478">
<text:list-item>
<text:list text:style-name="a478">
<text:list-item>
<text:list text:style-name="a478">
<text:list-item>
<text:p text:style-name="a477" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a476" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a481">
<text:list-item>
<text:list text:style-name="a481">
<text:list-item>
<text:list text:style-name="a481">
<text:list-item>
<text:list text:style-name="a481">
<text:list-item>
<text:p text:style-name="a480" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a479" text:class-names="">
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
<text:list text:style-name="a485">
<text:list-item>
<text:list text:style-name="a485">
<text:list-item>
<text:list text:style-name="a485">
<text:list-item>
<text:list text:style-name="a485">
<text:list-item>
<text:list text:style-name="a485">
<text:list-item>
<text:p text:style-name="a484" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a482" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a483" text:class-names="" />
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
<draw:frame draw:id="id76" presentation:style-name="a503" draw:name="Content Placeholder 3" svg:x="0.5in" svg:y="4.30729in" svg:width="9in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a489">
<text:list-item>
<text:p text:style-name="a488" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a487" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a492">
<text:list-item>
<text:list text:style-name="a492">
<text:list-item>
<text:p text:style-name="a491" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a490" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a495">
<text:list-item>
<text:list text:style-name="a495">
<text:list-item>
<text:list text:style-name="a495">
<text:list-item>
<text:p text:style-name="a494" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a493" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a498">
<text:list-item>
<text:list text:style-name="a498">
<text:list-item>
<text:list text:style-name="a498">
<text:list-item>
<text:list text:style-name="a498">
<text:list-item>
<text:p text:style-name="a497" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a496" text:class-names="">
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
<text:list text:style-name="a502">
<text:list-item>
<text:list text:style-name="a502">
<text:list-item>
<text:list text:style-name="a502">
<text:list-item>
<text:list text:style-name="a502">
<text:list-item>
<text:list text:style-name="a502">
<text:list-item>
<text:p text:style-name="a501" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a499" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a500" text:class-names="" />
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
<draw:frame draw:id="id77" presentation:style-name="a508" draw:name="Date Placeholder 4" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a507" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a504" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a505" />
</text:span>
<text:span text:style-name="a506" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id78" presentation:style-name="a511" draw:name="Footer Placeholder 5" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a510" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a509" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id79" presentation:style-name="a515" draw:name="Slide Number Placeholder 6" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a514" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a512" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a513" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout15-txAndObj-Title,-Text,-and-Content" style:page-layout-name="pageLayout1" draw:style-name="a516">
<draw:frame draw:id="id80" presentation:style-name="a520" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a519" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a517" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a518" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id81" presentation:style-name="a537" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a523">
<text:list-item>
<text:p text:style-name="a522" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a521" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a526">
<text:list-item>
<text:list text:style-name="a526">
<text:list-item>
<text:p text:style-name="a525" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a524" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a529">
<text:list-item>
<text:list text:style-name="a529">
<text:list-item>
<text:list text:style-name="a529">
<text:list-item>
<text:p text:style-name="a528" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a527" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
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
<text:list text:style-name="a532">
<text:list-item>
<text:p text:style-name="a531" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a530" text:class-names="">
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
<text:list text:style-name="a536">
<text:list-item>
<text:list text:style-name="a536">
<text:list-item>
<text:list text:style-name="a536">
<text:list-item>
<text:list text:style-name="a536">
<text:list-item>
<text:list text:style-name="a536">
<text:list-item>
<text:p text:style-name="a535" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a533" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a534" text:class-names="" />
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
<draw:frame draw:id="id82" presentation:style-name="a554" draw:name="Content Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a540">
<text:list-item>
<text:p text:style-name="a539" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a538" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a543">
<text:list-item>
<text:list text:style-name="a543">
<text:list-item>
<text:p text:style-name="a542" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a541" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a546">
<text:list-item>
<text:list text:style-name="a546">
<text:list-item>
<text:list text:style-name="a546">
<text:list-item>
<text:p text:style-name="a545" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a544" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a549">
<text:list-item>
<text:list text:style-name="a549">
<text:list-item>
<text:list text:style-name="a549">
<text:list-item>
<text:list text:style-name="a549">
<text:list-item>
<text:p text:style-name="a548" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a547" text:class-names="">
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
<text:list text:style-name="a553">
<text:list-item>
<text:list text:style-name="a553">
<text:list-item>
<text:list text:style-name="a553">
<text:list-item>
<text:list text:style-name="a553">
<text:list-item>
<text:list text:style-name="a553">
<text:list-item>
<text:p text:style-name="a552" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a550" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a551" text:class-names="" />
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
<draw:frame draw:id="id83" presentation:style-name="a559" draw:name="Date Placeholder 4" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a558" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a555" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a556" />
</text:span>
<text:span text:style-name="a557" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id84" presentation:style-name="a562" draw:name="Footer Placeholder 5" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a561" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a560" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id85" presentation:style-name="a566" draw:name="Slide Number Placeholder 6" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a565" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a563" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a564" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout16-objAndTx-Title,-Content-and-Text" style:page-layout-name="pageLayout1" draw:style-name="a567">
<draw:frame draw:id="id86" presentation:style-name="a571" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a570" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a568" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a569" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id87" presentation:style-name="a588" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a574">
<text:list-item>
<text:p text:style-name="a573" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a572" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a577">
<text:list-item>
<text:list text:style-name="a577">
<text:list-item>
<text:p text:style-name="a576" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a575" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a580">
<text:list-item>
<text:list text:style-name="a580">
<text:list-item>
<text:list text:style-name="a580">
<text:list-item>
<text:p text:style-name="a579" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a578" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a583">
<text:list-item>
<text:list text:style-name="a583">
<text:list-item>
<text:list text:style-name="a583">
<text:list-item>
<text:list text:style-name="a583">
<text:list-item>
<text:p text:style-name="a582" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a581" text:class-names="">
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
<text:list text:style-name="a587">
<text:list-item>
<text:list text:style-name="a587">
<text:list-item>
<text:list text:style-name="a587">
<text:list-item>
<text:list text:style-name="a587">
<text:list-item>
<text:list text:style-name="a587">
<text:list-item>
<text:p text:style-name="a586" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a584" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a585" text:class-names="" />
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
<draw:frame draw:id="id88" presentation:style-name="a605" draw:name="Text Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a591">
<text:list-item>
<text:p text:style-name="a590" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a589" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a594">
<text:list-item>
<text:list text:style-name="a594">
<text:list-item>
<text:p text:style-name="a593" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a592" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a597">
<text:list-item>
<text:list text:style-name="a597">
<text:list-item>
<text:list text:style-name="a597">
<text:list-item>
<text:p text:style-name="a596" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a595" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a600">
<text:list-item>
<text:list text:style-name="a600">
<text:list-item>
<text:list text:style-name="a600">
<text:list-item>
<text:list text:style-name="a600">
<text:list-item>
<text:p text:style-name="a599" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a598" text:class-names="">
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
<text:list text:style-name="a604">
<text:list-item>
<text:list text:style-name="a604">
<text:list-item>
<text:list text:style-name="a604">
<text:list-item>
<text:list text:style-name="a604">
<text:list-item>
<text:list text:style-name="a604">
<text:list-item>
<text:p text:style-name="a603" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a601" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a602" text:class-names="" />
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
<draw:frame draw:id="id89" presentation:style-name="a610" draw:name="Date Placeholder 4" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a609" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a606" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a607" />
</text:span>
<text:span text:style-name="a608" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id90" presentation:style-name="a613" draw:name="Footer Placeholder 5" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a612" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a611" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id91" presentation:style-name="a617" draw:name="Slide Number Placeholder 6" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a616" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a614" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a615" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout17-txAndTwoObj-Title,-Text,-and-2-Content" style:page-layout-name="pageLayout1" draw:style-name="a618">
<draw:frame draw:id="id92" presentation:style-name="a622" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a621" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a619" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a620" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id93" presentation:style-name="a639" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a625">
<text:list-item>
<text:p text:style-name="a624" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a623" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a628">
<text:list-item>
<text:list text:style-name="a628">
<text:list-item>
<text:p text:style-name="a627" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a626" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a631">
<text:list-item>
<text:list text:style-name="a631">
<text:list-item>
<text:list text:style-name="a631">
<text:list-item>
<text:p text:style-name="a630" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a629" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a634">
<text:list-item>
<text:list text:style-name="a634">
<text:list-item>
<text:list text:style-name="a634">
<text:list-item>
<text:list text:style-name="a634">
<text:list-item>
<text:p text:style-name="a633" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a632" text:class-names="">
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
<text:list text:style-name="a638">
<text:list-item>
<text:list text:style-name="a638">
<text:list-item>
<text:list text:style-name="a638">
<text:list-item>
<text:list text:style-name="a638">
<text:list-item>
<text:list text:style-name="a638">
<text:list-item>
<text:p text:style-name="a637" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a635" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a636" text:class-names="" />
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
<draw:frame draw:id="id94" presentation:style-name="a656" draw:name="Content Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a642">
<text:list-item>
<text:p text:style-name="a641" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a640" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a645">
<text:list-item>
<text:list text:style-name="a645">
<text:list-item>
<text:p text:style-name="a644" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a643" text:class-names="">
Second level</text:span>
</text:p>
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
<text:p text:style-name="a647" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a646" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a651">
<text:list-item>
<text:list text:style-name="a651">
<text:list-item>
<text:list text:style-name="a651">
<text:list-item>
<text:list text:style-name="a651">
<text:list-item>
<text:p text:style-name="a650" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a649" text:class-names="">
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
<text:list text:style-name="a655">
<text:list-item>
<text:list text:style-name="a655">
<text:list-item>
<text:list text:style-name="a655">
<text:list-item>
<text:list text:style-name="a655">
<text:list-item>
<text:list text:style-name="a655">
<text:list-item>
<text:p text:style-name="a654" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a652" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a653" text:class-names="" />
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
<draw:frame draw:id="id95" presentation:style-name="a673" draw:name="Content Placeholder 4" svg:x="5.08333in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a659">
<text:list-item>
<text:p text:style-name="a658" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a657" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a662">
<text:list-item>
<text:list text:style-name="a662">
<text:list-item>
<text:p text:style-name="a661" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a660" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a665">
<text:list-item>
<text:list text:style-name="a665">
<text:list-item>
<text:list text:style-name="a665">
<text:list-item>
<text:p text:style-name="a664" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a663" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a668">
<text:list-item>
<text:list text:style-name="a668">
<text:list-item>
<text:list text:style-name="a668">
<text:list-item>
<text:list text:style-name="a668">
<text:list-item>
<text:p text:style-name="a667" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a666" text:class-names="">
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
<text:list text:style-name="a672">
<text:list-item>
<text:list text:style-name="a672">
<text:list-item>
<text:list text:style-name="a672">
<text:list-item>
<text:list text:style-name="a672">
<text:list-item>
<text:list text:style-name="a672">
<text:list-item>
<text:p text:style-name="a671" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a669" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a670" text:class-names="" />
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
<draw:frame draw:id="id96" presentation:style-name="a678" draw:name="Date Placeholder 5" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a677" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a674" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a675" />
</text:span>
<text:span text:style-name="a676" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id97" presentation:style-name="a681" draw:name="Footer Placeholder 6" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a680" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a679" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id98" presentation:style-name="a685" draw:name="Slide Number Placeholder 7" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a684" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a682" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a683" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout18-objAndTwoObj-Title,-Content,-and-2-Content" style:page-layout-name="pageLayout1" draw:style-name="a686">
<draw:frame draw:id="id99" presentation:style-name="a690" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a689" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a687" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a688" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id100" presentation:style-name="a707" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a693">
<text:list-item>
<text:p text:style-name="a692" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a691" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a696">
<text:list-item>
<text:list text:style-name="a696">
<text:list-item>
<text:p text:style-name="a695" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a694" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a699">
<text:list-item>
<text:list text:style-name="a699">
<text:list-item>
<text:list text:style-name="a699">
<text:list-item>
<text:p text:style-name="a698" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a697" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a702">
<text:list-item>
<text:list text:style-name="a702">
<text:list-item>
<text:list text:style-name="a702">
<text:list-item>
<text:list text:style-name="a702">
<text:list-item>
<text:p text:style-name="a701" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a700" text:class-names="">
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
<text:list text:style-name="a706">
<text:list-item>
<text:list text:style-name="a706">
<text:list-item>
<text:list text:style-name="a706">
<text:list-item>
<text:list text:style-name="a706">
<text:list-item>
<text:list text:style-name="a706">
<text:list-item>
<text:p text:style-name="a705" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a703" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a704" text:class-names="" />
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
<draw:frame draw:id="id101" presentation:style-name="a724" draw:name="Content Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a710">
<text:list-item>
<text:p text:style-name="a709" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a708" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a713">
<text:list-item>
<text:list text:style-name="a713">
<text:list-item>
<text:p text:style-name="a712" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a711" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a716">
<text:list-item>
<text:list text:style-name="a716">
<text:list-item>
<text:list text:style-name="a716">
<text:list-item>
<text:p text:style-name="a715" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a714" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a719">
<text:list-item>
<text:list text:style-name="a719">
<text:list-item>
<text:list text:style-name="a719">
<text:list-item>
<text:list text:style-name="a719">
<text:list-item>
<text:p text:style-name="a718" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a717" text:class-names="">
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
<text:list text:style-name="a723">
<text:list-item>
<text:list text:style-name="a723">
<text:list-item>
<text:list text:style-name="a723">
<text:list-item>
<text:list text:style-name="a723">
<text:list-item>
<text:list text:style-name="a723">
<text:list-item>
<text:p text:style-name="a722" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a720" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a721" text:class-names="" />
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
<draw:frame draw:id="id102" presentation:style-name="a741" draw:name="Content Placeholder 4" svg:x="5.08333in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a727">
<text:list-item>
<text:p text:style-name="a726" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a725" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a730">
<text:list-item>
<text:list text:style-name="a730">
<text:list-item>
<text:p text:style-name="a729" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a728" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a733">
<text:list-item>
<text:list text:style-name="a733">
<text:list-item>
<text:list text:style-name="a733">
<text:list-item>
<text:p text:style-name="a732" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a731" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a736">
<text:list-item>
<text:list text:style-name="a736">
<text:list-item>
<text:list text:style-name="a736">
<text:list-item>
<text:list text:style-name="a736">
<text:list-item>
<text:p text:style-name="a735" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a734" text:class-names="">
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
<text:list text:style-name="a740">
<text:list-item>
<text:list text:style-name="a740">
<text:list-item>
<text:list text:style-name="a740">
<text:list-item>
<text:list text:style-name="a740">
<text:list-item>
<text:list text:style-name="a740">
<text:list-item>
<text:p text:style-name="a739" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a737" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a738" text:class-names="" />
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
<draw:frame draw:id="id103" presentation:style-name="a746" draw:name="Date Placeholder 5" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a745" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a742" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a743" />
</text:span>
<text:span text:style-name="a744" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id104" presentation:style-name="a749" draw:name="Footer Placeholder 6" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a748" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a747" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id105" presentation:style-name="a753" draw:name="Slide Number Placeholder 7" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a752" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a750" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a751" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout19-objOverTx-Title-and-Content-over-Text" style:page-layout-name="pageLayout1" draw:style-name="a754">
<draw:frame draw:id="id106" presentation:style-name="a758" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a757" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a755" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a756" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id107" presentation:style-name="a775" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a761">
<text:list-item>
<text:p text:style-name="a760" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a759" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a764">
<text:list-item>
<text:list text:style-name="a764">
<text:list-item>
<text:p text:style-name="a763" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a762" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a767">
<text:list-item>
<text:list text:style-name="a767">
<text:list-item>
<text:list text:style-name="a767">
<text:list-item>
<text:p text:style-name="a766" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a765" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a770">
<text:list-item>
<text:list text:style-name="a770">
<text:list-item>
<text:list text:style-name="a770">
<text:list-item>
<text:list text:style-name="a770">
<text:list-item>
<text:p text:style-name="a769" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a768" text:class-names="">
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
<text:span text:style-name="a771" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a772" text:class-names="" />
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
<draw:frame draw:id="id108" presentation:style-name="a792" draw:name="Text Placeholder 3" svg:x="0.5in" svg:y="4.30729in" svg:width="9in" svg:height="2.39236in" presentation:class="outline" presentation:placeholder="false">
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
<text:list text:style-name="a791">
<text:list-item>
<text:list text:style-name="a791">
<text:list-item>
<text:list text:style-name="a791">
<text:list-item>
<text:list text:style-name="a791">
<text:list-item>
<text:list text:style-name="a791">
<text:list-item>
<text:p text:style-name="a790" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a788" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a789" text:class-names="" />
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
<draw:frame draw:id="id109" presentation:style-name="a797" draw:name="Date Placeholder 4" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a796" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a793" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a794" />
</text:span>
<text:span text:style-name="a795" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id110" presentation:style-name="a800" draw:name="Footer Placeholder 5" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a799" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a798" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id111" presentation:style-name="a804" draw:name="Slide Number Placeholder 6" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a803" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a801" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a802" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout20-fourObj-Title-and-4-Content" style:page-layout-name="pageLayout1" draw:style-name="a805">
<draw:frame draw:id="id112" presentation:style-name="a809" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a808" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a806" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a807" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id113" presentation:style-name="a826" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a812">
<text:list-item>
<text:p text:style-name="a811" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a810" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a815">
<text:list-item>
<text:list text:style-name="a815">
<text:list-item>
<text:p text:style-name="a814" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a813" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a818">
<text:list-item>
<text:list text:style-name="a818">
<text:list-item>
<text:list text:style-name="a818">
<text:list-item>
<text:p text:style-name="a817" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a816" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a821">
<text:list-item>
<text:list text:style-name="a821">
<text:list-item>
<text:list text:style-name="a821">
<text:list-item>
<text:list text:style-name="a821">
<text:list-item>
<text:p text:style-name="a820" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a819" text:class-names="">
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
<text:list text:style-name="a825">
<text:list-item>
<text:list text:style-name="a825">
<text:list-item>
<text:list text:style-name="a825">
<text:list-item>
<text:list text:style-name="a825">
<text:list-item>
<text:list text:style-name="a825">
<text:list-item>
<text:p text:style-name="a824" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a822" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a823" text:class-names="" />
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
<draw:frame draw:id="id114" presentation:style-name="a843" draw:name="Content Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a829">
<text:list-item>
<text:p text:style-name="a828" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a827" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a832">
<text:list-item>
<text:list text:style-name="a832">
<text:list-item>
<text:p text:style-name="a831" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a830" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a835">
<text:list-item>
<text:list text:style-name="a835">
<text:list-item>
<text:list text:style-name="a835">
<text:list-item>
<text:p text:style-name="a834" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a833" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a838">
<text:list-item>
<text:list text:style-name="a838">
<text:list-item>
<text:list text:style-name="a838">
<text:list-item>
<text:list text:style-name="a838">
<text:list-item>
<text:p text:style-name="a837" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a836" text:class-names="">
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
<text:list text:style-name="a842">
<text:list-item>
<text:list text:style-name="a842">
<text:list-item>
<text:list text:style-name="a842">
<text:list-item>
<text:list text:style-name="a842">
<text:list-item>
<text:list text:style-name="a842">
<text:list-item>
<text:p text:style-name="a841" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a839" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a840" text:class-names="" />
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
<draw:frame draw:id="id115" presentation:style-name="a860" draw:name="Content Placeholder 4" svg:x="0.5in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a846">
<text:list-item>
<text:p text:style-name="a845" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a844" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a849">
<text:list-item>
<text:list text:style-name="a849">
<text:list-item>
<text:p text:style-name="a848" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a847" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a852">
<text:list-item>
<text:list text:style-name="a852">
<text:list-item>
<text:list text:style-name="a852">
<text:list-item>
<text:p text:style-name="a851" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a850" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a855">
<text:list-item>
<text:list text:style-name="a855">
<text:list-item>
<text:list text:style-name="a855">
<text:list-item>
<text:list text:style-name="a855">
<text:list-item>
<text:p text:style-name="a854" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a853" text:class-names="">
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
<text:list text:style-name="a859">
<text:list-item>
<text:list text:style-name="a859">
<text:list-item>
<text:list text:style-name="a859">
<text:list-item>
<text:list text:style-name="a859">
<text:list-item>
<text:list text:style-name="a859">
<text:list-item>
<text:p text:style-name="a858" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a856" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a857" text:class-names="" />
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
<draw:frame draw:id="id116" presentation:style-name="a877" draw:name="Content Placeholder 5" svg:x="5.08333in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a863">
<text:list-item>
<text:p text:style-name="a862" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a861" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a866">
<text:list-item>
<text:list text:style-name="a866">
<text:list-item>
<text:p text:style-name="a865" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a864" text:class-names="">
Second level</text:span>
</text:p>
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
<text:p text:style-name="a868" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a867" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a872">
<text:list-item>
<text:list text:style-name="a872">
<text:list-item>
<text:list text:style-name="a872">
<text:list-item>
<text:list text:style-name="a872">
<text:list-item>
<text:p text:style-name="a871" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a870" text:class-names="">
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
<text:list text:style-name="a876">
<text:list-item>
<text:list text:style-name="a876">
<text:list-item>
<text:list text:style-name="a876">
<text:list-item>
<text:list text:style-name="a876">
<text:list-item>
<text:list text:style-name="a876">
<text:list-item>
<text:p text:style-name="a875" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a873" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a874" text:class-names="" />
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
<draw:frame draw:id="id117" presentation:style-name="a882" draw:name="Date Placeholder 6" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a881" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a878" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a879" />
</text:span>
<text:span text:style-name="a880" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id118" presentation:style-name="a885" draw:name="Footer Placeholder 7" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a884" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a883" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id119" presentation:style-name="a889" draw:name="Slide Number Placeholder 8" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a888" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a886" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a887" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout21-twoObjAndObj-Title,-2-Content-and-Content" style:page-layout-name="pageLayout1" draw:style-name="a890">
<draw:frame draw:id="id120" presentation:style-name="a894" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a893" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a891" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a892" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id121" presentation:style-name="a911" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a897">
<text:list-item>
<text:p text:style-name="a896" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a895" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a900">
<text:list-item>
<text:list text:style-name="a900">
<text:list-item>
<text:p text:style-name="a899" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a898" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a903">
<text:list-item>
<text:list text:style-name="a903">
<text:list-item>
<text:list text:style-name="a903">
<text:list-item>
<text:p text:style-name="a902" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a901" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a906">
<text:list-item>
<text:list text:style-name="a906">
<text:list-item>
<text:list text:style-name="a906">
<text:list-item>
<text:list text:style-name="a906">
<text:list-item>
<text:p text:style-name="a905" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a904" text:class-names="">
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
<text:list text:style-name="a910">
<text:list-item>
<text:list text:style-name="a910">
<text:list-item>
<text:list text:style-name="a910">
<text:list-item>
<text:list text:style-name="a910">
<text:list-item>
<text:list text:style-name="a910">
<text:list-item>
<text:p text:style-name="a909" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a907" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a908" text:class-names="" />
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
<draw:frame draw:id="id122" presentation:style-name="a928" draw:name="Content Placeholder 3" svg:x="0.5in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a914">
<text:list-item>
<text:p text:style-name="a913" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a912" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a917">
<text:list-item>
<text:list text:style-name="a917">
<text:list-item>
<text:p text:style-name="a916" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a915" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a920">
<text:list-item>
<text:list text:style-name="a920">
<text:list-item>
<text:list text:style-name="a920">
<text:list-item>
<text:p text:style-name="a919" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a918" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a923">
<text:list-item>
<text:list text:style-name="a923">
<text:list-item>
<text:list text:style-name="a923">
<text:list-item>
<text:list text:style-name="a923">
<text:list-item>
<text:p text:style-name="a922" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a921" text:class-names="">
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
<text:list text:style-name="a927">
<text:list-item>
<text:list text:style-name="a927">
<text:list-item>
<text:list text:style-name="a927">
<text:list-item>
<text:list text:style-name="a927">
<text:list-item>
<text:list text:style-name="a927">
<text:list-item>
<text:p text:style-name="a926" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a924" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a925" text:class-names="" />
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
<draw:frame draw:id="id123" presentation:style-name="a945" draw:name="Content Placeholder 4" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a931">
<text:list-item>
<text:p text:style-name="a930" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a929" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a934">
<text:list-item>
<text:list text:style-name="a934">
<text:list-item>
<text:p text:style-name="a933" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a932" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a937">
<text:list-item>
<text:list text:style-name="a937">
<text:list-item>
<text:list text:style-name="a937">
<text:list-item>
<text:p text:style-name="a936" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a935" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a940">
<text:list-item>
<text:list text:style-name="a940">
<text:list-item>
<text:list text:style-name="a940">
<text:list-item>
<text:list text:style-name="a940">
<text:list-item>
<text:p text:style-name="a939" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a938" text:class-names="">
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
<text:list text:style-name="a944">
<text:list-item>
<text:list text:style-name="a944">
<text:list-item>
<text:list text:style-name="a944">
<text:list-item>
<text:list text:style-name="a944">
<text:list-item>
<text:list text:style-name="a944">
<text:list-item>
<text:p text:style-name="a943" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a941" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a942" text:class-names="" />
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
<draw:frame draw:id="id124" presentation:style-name="a950" draw:name="Date Placeholder 5" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a949" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a946" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a947" />
</text:span>
<text:span text:style-name="a948" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id125" presentation:style-name="a953" draw:name="Footer Placeholder 6" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a952" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a951" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id126" presentation:style-name="a957" draw:name="Slide Number Placeholder 7" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a956" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a954" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a955" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout22-twoObjAndTx-Title,-2-Content-and-Text" style:page-layout-name="pageLayout1" draw:style-name="a958">
<draw:frame draw:id="id127" presentation:style-name="a962" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a961" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a959" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a960" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id128" presentation:style-name="a979" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a965">
<text:list-item>
<text:p text:style-name="a964" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a963" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a968">
<text:list-item>
<text:list text:style-name="a968">
<text:list-item>
<text:p text:style-name="a967" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a966" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a971">
<text:list-item>
<text:list text:style-name="a971">
<text:list-item>
<text:list text:style-name="a971">
<text:list-item>
<text:p text:style-name="a970" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a969" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a974">
<text:list-item>
<text:list text:style-name="a974">
<text:list-item>
<text:list text:style-name="a974">
<text:list-item>
<text:list text:style-name="a974">
<text:list-item>
<text:p text:style-name="a973" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a972" text:class-names="">
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
<text:list text:style-name="a978">
<text:list-item>
<text:list text:style-name="a978">
<text:list-item>
<text:list text:style-name="a978">
<text:list-item>
<text:list text:style-name="a978">
<text:list-item>
<text:list text:style-name="a978">
<text:list-item>
<text:p text:style-name="a977" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a975" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a976" text:class-names="" />
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
<draw:frame draw:id="id129" presentation:style-name="a996" draw:name="Content Placeholder 3" svg:x="0.5in" svg:y="4.30729in" svg:width="4.41667in" svg:height="2.39236in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a982">
<text:list-item>
<text:p text:style-name="a981" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a980" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a985">
<text:list-item>
<text:list text:style-name="a985">
<text:list-item>
<text:p text:style-name="a984" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a983" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a988">
<text:list-item>
<text:list text:style-name="a988">
<text:list-item>
<text:list text:style-name="a988">
<text:list-item>
<text:p text:style-name="a987" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a986" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a991">
<text:list-item>
<text:list text:style-name="a991">
<text:list-item>
<text:list text:style-name="a991">
<text:list-item>
<text:list text:style-name="a991">
<text:list-item>
<text:p text:style-name="a990" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a989" text:class-names="">
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
<text:span text:style-name="a992" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a993" text:class-names="" />
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
<draw:frame draw:id="id130" presentation:style-name="a1013" draw:name="Text Placeholder 4" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a999">
<text:list-item>
<text:p text:style-name="a998" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a997" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1002">
<text:list-item>
<text:list text:style-name="a1002">
<text:list-item>
<text:p text:style-name="a1001" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1000" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a1005">
<text:list-item>
<text:list text:style-name="a1005">
<text:list-item>
<text:list text:style-name="a1005">
<text:list-item>
<text:p text:style-name="a1004" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1003" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a1008">
<text:list-item>
<text:list text:style-name="a1008">
<text:list-item>
<text:list text:style-name="a1008">
<text:list-item>
<text:list text:style-name="a1008">
<text:list-item>
<text:p text:style-name="a1007" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1006" text:class-names="">
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
<text:list text:style-name="a1012">
<text:list-item>
<text:list text:style-name="a1012">
<text:list-item>
<text:list text:style-name="a1012">
<text:list-item>
<text:list text:style-name="a1012">
<text:list-item>
<text:list text:style-name="a1012">
<text:list-item>
<text:p text:style-name="a1011" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1009" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a1010" text:class-names="" />
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
<draw:frame draw:id="id131" presentation:style-name="a1018" draw:name="Date Placeholder 5" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1017" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1014" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a1015" />
</text:span>
<text:span text:style-name="a1016" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id132" presentation:style-name="a1021" draw:name="Footer Placeholder 6" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1020" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1019" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id133" presentation:style-name="a1025" draw:name="Slide Number Placeholder 7" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1024" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1022" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a1023" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout23-twoObjOverTx-Title-and-2-Content-over-Text" style:page-layout-name="pageLayout1" draw:style-name="a1026">
<draw:frame draw:id="id134" presentation:style-name="a1030" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1029" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1027" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a1028" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id135" presentation:style-name="a1047" draw:name="Content Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1033">
<text:list-item>
<text:p text:style-name="a1032" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1031" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1036">
<text:list-item>
<text:list text:style-name="a1036">
<text:list-item>
<text:p text:style-name="a1035" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1034" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a1039">
<text:list-item>
<text:list text:style-name="a1039">
<text:list-item>
<text:list text:style-name="a1039">
<text:list-item>
<text:p text:style-name="a1038" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1037" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a1042">
<text:list-item>
<text:list text:style-name="a1042">
<text:list-item>
<text:list text:style-name="a1042">
<text:list-item>
<text:list text:style-name="a1042">
<text:list-item>
<text:p text:style-name="a1041" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1040" text:class-names="">
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
<text:list text:style-name="a1046">
<text:list-item>
<text:list text:style-name="a1046">
<text:list-item>
<text:list text:style-name="a1046">
<text:list-item>
<text:list text:style-name="a1046">
<text:list-item>
<text:list text:style-name="a1046">
<text:list-item>
<text:p text:style-name="a1045" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1043" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a1044" text:class-names="" />
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
<draw:frame draw:id="id136" presentation:style-name="a1064" draw:name="Content Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="2.39063in" presentation:class="object" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1050">
<text:list-item>
<text:p text:style-name="a1049" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1048" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1053">
<text:list-item>
<text:list text:style-name="a1053">
<text:list-item>
<text:p text:style-name="a1052" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1051" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a1056">
<text:list-item>
<text:list text:style-name="a1056">
<text:list-item>
<text:list text:style-name="a1056">
<text:list-item>
<text:p text:style-name="a1055" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1054" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a1059">
<text:list-item>
<text:list text:style-name="a1059">
<text:list-item>
<text:list text:style-name="a1059">
<text:list-item>
<text:list text:style-name="a1059">
<text:list-item>
<text:p text:style-name="a1058" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1057" text:class-names="">
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
<text:list text:style-name="a1063">
<text:list-item>
<text:list text:style-name="a1063">
<text:list-item>
<text:list text:style-name="a1063">
<text:list-item>
<text:list text:style-name="a1063">
<text:list-item>
<text:list text:style-name="a1063">
<text:list-item>
<text:p text:style-name="a1062" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1060" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a1061" text:class-names="" />
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
<draw:frame draw:id="id137" presentation:style-name="a1081" draw:name="Text Placeholder 4" svg:x="0.5in" svg:y="4.30729in" svg:width="9in" svg:height="2.39236in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1067">
<text:list-item>
<text:p text:style-name="a1066" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1065" text:class-names="">
Click to edit Master text styles</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1070">
<text:list-item>
<text:list text:style-name="a1070">
<text:list-item>
<text:p text:style-name="a1069" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1068" text:class-names="">
Second level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a1073">
<text:list-item>
<text:list text:style-name="a1073">
<text:list-item>
<text:list text:style-name="a1073">
<text:list-item>
<text:p text:style-name="a1072" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1071" text:class-names="">
Third level</text:span>
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
<text:list text:style-name="a1076">
<text:list-item>
<text:list text:style-name="a1076">
<text:list-item>
<text:list text:style-name="a1076">
<text:list-item>
<text:list text:style-name="a1076">
<text:list-item>
<text:p text:style-name="a1075" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1074" text:class-names="">
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
<text:list text:style-name="a1080">
<text:list-item>
<text:list text:style-name="a1080">
<text:list-item>
<text:list text:style-name="a1080">
<text:list-item>
<text:list text:style-name="a1080">
<text:list-item>
<text:list text:style-name="a1080">
<text:list-item>
<text:p text:style-name="a1079" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1077" text:class-names="">
Fifth level</text:span>
<text:span text:style-name="a1078" text:class-names="" />
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
<draw:frame draw:id="id138" presentation:style-name="a1086" draw:name="Date Placeholder 5" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1085" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1082" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a1083" />
</text:span>
<text:span text:style-name="a1084" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id139" presentation:style-name="a1089" draw:name="Footer Placeholder 6" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1088" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1087" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id140" presentation:style-name="a1093" draw:name="Slide Number Placeholder 7" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1092" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1090" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a1091" text:class-names="" />
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
    
    elem = build_element( """<style:master-page style:name="Master1-Layout24-tbl-Title-and-Table" style:page-layout-name="pageLayout1" draw:style-name="a1094">
<draw:frame draw:id="id141" presentation:style-name="a1098" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1097" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1095" text:class-names="">
Click to edit Master title style</text:span>
<text:span text:style-name="a1096" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id142" presentation:style-name="a1102" draw:name="Table Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="4.94965in" presentation:class="table" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1101">
<text:list-item>
<text:p text:style-name="a1100" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1099" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id143" presentation:style-name="a1107" draw:name="Date Placeholder 3" svg:x="0.5in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="date-time" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1106" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1103" text:class-names="">
<text:date text:fixed="false" style:data-style-name="a1104" />
</text:span>
<text:span text:style-name="a1105" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id144" presentation:style-name="a1110" draw:name="Footer Placeholder 4" svg:x="3.41667in" svg:y="6.95139in" svg:width="3.16667in" svg:height="0.39931in" presentation:class="footer" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1109" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1108" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id145" presentation:style-name="a1114" draw:name="Slide Number Placeholder 5" svg:x="7.16667in" svg:y="6.95139in" svg:width="2.33333in" svg:height="0.39931in" presentation:class="page-number" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1113" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1111" text:class-names="">
<text:page-number style:num-format="1" text:fixed="false" />
</text:span>
<text:span text:style-name="a1112" text:class-names="" />
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
