
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


# Use master_page_name_lookupD for access to master page names
# index=layout name (e.g. "Master1-PPL24"), value=master name (e.g. "Master1-Layout24-tbl-Title-and-Table")

master_page_name_lookupD = {}

# Use layout_page_name_lookupD for access layout page names
# index=layout name (e.g. "Master1-Layout24-tbl-Title-and-Table"), value=master name (e.g. "Master1-PPL24")

layout_page_name_lookupD = {}

def draw_8_page_Master1_PPL1():
    
    """Build Element draw:page for Master1-PPL1 """
    
    elem = build_element( """<draw:page draw:name="Slide1" draw:style-name="a1141" draw:master-page-name="Master1-Layout1-title-Title-Slide" presentation:presentation-page-layout-name="Master1-PPL1" draw:id="Slide-256">
<draw:frame draw:id="id146" presentation:style-name="a1145" draw:name="Title 1" svg:x="0.75in" svg:y="2.32986in" svg:width="8.5in" svg:height="1.60764in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1144" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1142" text:class-names="">
ppLayoutTitle</text:span>
<text:span text:style-name="a1143" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id147" presentation:style-name="a1152" draw:name="Subtitle 2" svg:x="1.5in" svg:y="4.25in" svg:width="7in" svg:height="1.91667in" presentation:class="subtitle" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1147" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1146" text:class-names="">
Text(2)</text:span>
</text:p>
<text:list text:style-name="a1151">
<text:list-item>
<text:list text:style-name="a1151">
<text:list-item>
<text:p text:style-name="a1150" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1148" text:class-names="">
For ppLayoutTitle</text:span>
<text:span text:style-name="a1149" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL12():
    
    """Build Element draw:page for Master1-PPL12 """
    
    elem = build_element( """<draw:page draw:name="Slide2" draw:style-name="a1154" draw:master-page-name="Master1-Layout12-tx-Title-and-Text" presentation:presentation-page-layout-name="Master1-PPL12" draw:id="Slide-257">
<draw:frame draw:id="id148" presentation:style-name="a1158" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1157" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1155" text:class-names="">
ppLayoutText</text:span>
<text:span text:style-name="a1156" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id149" presentation:style-name="a1166" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1161">
<text:list-item>
<text:p text:style-name="a1160" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1159" text:class-names="">
Text(2)</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1165">
<text:list-item>
<text:list text:style-name="a1165">
<text:list-item>
<text:p text:style-name="a1164" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1162" text:class-names="">
For ppLayoutText</text:span>
<text:span text:style-name="a1163" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL13():
    
    """Build Element draw:page for Master1-PPL13 """
    
    elem = build_element( """<draw:page draw:name="Slide3" draw:style-name="a1168" draw:master-page-name="Master1-Layout13-twoColTx-Title-and-2-Column-Text" presentation:presentation-page-layout-name="Master1-PPL13" draw:id="Slide-258">
<draw:frame draw:id="id150" presentation:style-name="a1172" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1171" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1169" text:class-names="">
ppLayoutTwoColumnText</text:span>
<text:span text:style-name="a1170" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id151" presentation:style-name="a1180" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1175">
<text:list-item>
<text:p text:style-name="a1174" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1173" text:class-names="">
Text(2)</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1179">
<text:list-item>
<text:list text:style-name="a1179">
<text:list-item>
<text:p text:style-name="a1178" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1176" text:class-names="">
For ppLayoutTwoColumnText</text:span>
<text:span text:style-name="a1177" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id152" presentation:style-name="a1188" draw:name="Text Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1183">
<text:list-item>
<text:p text:style-name="a1182" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1181" text:class-names="">
Text(3)</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1187">
<text:list-item>
<text:list text:style-name="a1187">
<text:list-item>
<text:p text:style-name="a1186" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1184" text:class-names="">
For ppLayoutTwoColumnText</text:span>
<text:span text:style-name="a1185" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL2():
    
    """Build Element draw:page for Master1-PPL2 """
    
    elem = build_element( """<draw:page draw:name="Slide4" draw:style-name="a1190" draw:master-page-name="Master1-Layout2-obj-Title-and-Content" presentation:presentation-page-layout-name="Master1-PPL2" draw:id="Slide-259">
<draw:frame draw:id="id153" presentation:style-name="a1194" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1193" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1191" text:class-names="">
ppLayoutObject</text:span>
<text:span text:style-name="a1192" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id154" presentation:style-name="a1195" draw:name="Content Placeholder 3" svg:x="2.91667in" svg:y="2.66233in" svg:width="4.16667in" svg:height="3.125in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image1.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL14():
    
    """Build Element draw:page for Master1-PPL14 """
    
    elem = build_element( """<draw:page draw:name="Slide5" draw:style-name="a1197" draw:master-page-name="Master1-Layout14-txOverObj-Title-and-Text-over-Content" presentation:presentation-page-layout-name="Master1-PPL14" draw:id="Slide-260">
<draw:frame draw:id="id155" presentation:style-name="a1201" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1200" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1198" text:class-names="">
ppLayoutTextOverObject</text:span>
<text:span text:style-name="a1199" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id156" presentation:style-name="a1209" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="2.39063in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1204">
<text:list-item>
<text:p text:style-name="a1203" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1202" text:class-names="">
Text(2)</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1208">
<text:list-item>
<text:list text:style-name="a1208">
<text:list-item>
<text:p text:style-name="a1207" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1205" text:class-names="">
For ppLayoutTextOverObject</text:span>
<text:span text:style-name="a1206" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id157" presentation:style-name="a1210" draw:name="Content Placeholder 4" svg:x="3.40509in" svg:y="4.30729in" svg:width="3.18981in" svg:height="2.39236in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image2.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL15():
    
    """Build Element draw:page for Master1-PPL15 """
    
    elem = build_element( """<draw:page draw:name="Slide6" draw:style-name="a1212" draw:master-page-name="Master1-Layout15-txAndObj-Title,-Text,-and-Content" presentation:presentation-page-layout-name="Master1-PPL15" draw:id="Slide-261">
<draw:frame draw:id="id158" presentation:style-name="a1216" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1215" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1213" text:class-names="">
ppLayoutTextAndObject</text:span>
<text:span text:style-name="a1214" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id159" presentation:style-name="a1224" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1219">
<text:list-item>
<text:p text:style-name="a1218" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1217" text:class-names="">
Text(2)</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1223">
<text:list-item>
<text:list text:style-name="a1223">
<text:list-item>
<text:p text:style-name="a1222" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1220" text:class-names="">
For ppLayoutTextAndObject</text:span>
<text:span text:style-name="a1221" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id160" presentation:style-name="a1225" draw:name="Content Placeholder 4" svg:x="5.20833in" svg:y="2.66233in" svg:width="4.16667in" svg:height="3.125in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image3.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL4():
    
    """Build Element draw:page for Master1-PPL4 """
    
    elem = build_element( """<draw:page draw:name="Slide7" draw:style-name="a1227" draw:master-page-name="Master1-Layout4-twoObj-Two-Content" presentation:presentation-page-layout-name="Master1-PPL4" draw:id="Slide-262">
<draw:frame draw:id="id161" presentation:style-name="a1231" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1230" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1228" text:class-names="">
ppLayoutTwoObjects</text:span>
<text:span text:style-name="a1229" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id162" presentation:style-name="a1232" draw:name="Content Placeholder 4" svg:x="0.625in" svg:y="2.66233in" svg:width="4.16667in" svg:height="3.125in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image4.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id163" presentation:style-name="a1233" draw:name="Content Placeholder 5" svg:x="5.20833in" svg:y="2.66233in" svg:width="4.16667in" svg:height="3.125in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image5.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL16():
    
    """Build Element draw:page for Master1-PPL16 """
    
    elem = build_element( """<draw:page draw:name="Slide8" draw:style-name="a1235" draw:master-page-name="Master1-Layout16-objAndTx-Title,-Content-and-Text" presentation:presentation-page-layout-name="Master1-PPL16" draw:id="Slide-263">
<draw:frame draw:id="id164" presentation:style-name="a1239" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1238" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1236" text:class-names="">
ppLayoutObjectAndText</text:span>
<text:span text:style-name="a1237" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id165" presentation:style-name="a1240" draw:name="Content Placeholder 4" svg:x="0.625in" svg:y="2.66233in" svg:width="4.16667in" svg:height="3.125in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image6.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id166" presentation:style-name="a1248" draw:name="Text Placeholder 3" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1243">
<text:list-item>
<text:p text:style-name="a1242" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1241" text:class-names="">
Text(3)</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1247">
<text:list-item>
<text:list text:style-name="a1247">
<text:list-item>
<text:p text:style-name="a1246" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1244" text:class-names="">
For ppLayoutObjectAndText</text:span>
<text:span text:style-name="a1245" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL17():
    
    """Build Element draw:page for Master1-PPL17 """
    
    elem = build_element( """<draw:page draw:name="Slide9" draw:style-name="a1250" draw:master-page-name="Master1-Layout17-txAndTwoObj-Title,-Text,-and-2-Content" presentation:presentation-page-layout-name="Master1-PPL17" draw:id="Slide-264">
<draw:frame draw:id="id167" presentation:style-name="a1254" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1253" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1251" text:class-names="">
ppLayoutTextAndTwoObjects</text:span>
<text:span text:style-name="a1252" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id168" presentation:style-name="a1262" draw:name="Text Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1257">
<text:list-item>
<text:p text:style-name="a1256" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1255" text:class-names="">
Text(2)</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1261">
<text:list-item>
<text:list text:style-name="a1261">
<text:list-item>
<text:p text:style-name="a1260" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1258" text:class-names="">
For ppLayoutTextAndTwoObjects</text:span>
<text:span text:style-name="a1259" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id169" presentation:style-name="a1263" draw:name="Content Placeholder 5" svg:x="5.69792in" svg:y="1.75in" svg:width="3.1875in" svg:height="2.39063in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image7.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id170" presentation:style-name="a1264" draw:name="Content Placeholder 6" svg:x="5.69676in" svg:y="4.30729in" svg:width="3.18981in" svg:height="2.39236in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image8.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL18():
    
    """Build Element draw:page for Master1-PPL18 """
    
    elem = build_element( """<draw:page draw:name="Slide10" draw:style-name="a1266" draw:master-page-name="Master1-Layout18-objAndTwoObj-Title,-Content,-and-2-Content" presentation:presentation-page-layout-name="Master1-PPL18" draw:id="Slide-265">
<draw:frame draw:id="id171" presentation:style-name="a1270" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1269" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1267" text:class-names="">
ppLayoutObjectAndTwoObjects</text:span>
<text:span text:style-name="a1268" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id172" presentation:style-name="a1271" draw:name="Content Placeholder 5" svg:x="0.625in" svg:y="2.66233in" svg:width="4.16667in" svg:height="3.125in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image9.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id173" presentation:style-name="a1272" draw:name="Content Placeholder 6" svg:x="5.69792in" svg:y="1.75in" svg:width="3.1875in" svg:height="2.39063in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image10.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id174" presentation:style-name="a1273" draw:name="Content Placeholder 7" svg:x="5.69676in" svg:y="4.30729in" svg:width="3.18981in" svg:height="2.39236in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image11.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL19():
    
    """Build Element draw:page for Master1-PPL19 """
    
    elem = build_element( """<draw:page draw:name="Slide11" draw:style-name="a1275" draw:master-page-name="Master1-Layout19-objOverTx-Title-and-Content-over-Text" presentation:presentation-page-layout-name="Master1-PPL19" draw:id="Slide-266">
<draw:frame draw:id="id175" presentation:style-name="a1279" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1278" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1276" text:class-names="">
ppLayoutObjectOverText</text:span>
<text:span text:style-name="a1277" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id176" presentation:style-name="a1280" draw:name="Content Placeholder 4" svg:x="3.40625in" svg:y="1.75in" svg:width="3.1875in" svg:height="2.39063in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image12.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id177" presentation:style-name="a1288" draw:name="Text Placeholder 3" svg:x="0.5in" svg:y="4.30729in" svg:width="9in" svg:height="2.39236in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1283">
<text:list-item>
<text:p text:style-name="a1282" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1281" text:class-names="">
Text(3)</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1287">
<text:list-item>
<text:list text:style-name="a1287">
<text:list-item>
<text:p text:style-name="a1286" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1284" text:class-names="">
For ppLayoutObjectOverText</text:span>
<text:span text:style-name="a1285" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL20():
    
    """Build Element draw:page for Master1-PPL20 """
    
    elem = build_element( """<draw:page draw:name="Slide12" draw:style-name="a1290" draw:master-page-name="Master1-Layout20-fourObj-Title-and-4-Content" presentation:presentation-page-layout-name="Master1-PPL20" draw:id="Slide-267">
<draw:frame draw:id="id178" presentation:style-name="a1294" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1293" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1291" text:class-names="">
ppLayoutFourObjects</text:span>
<text:span text:style-name="a1292" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id179" presentation:style-name="a1295" draw:name="Content Placeholder 6" svg:x="1.11458in" svg:y="1.75in" svg:width="3.1875in" svg:height="2.39063in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image13.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id180" presentation:style-name="a1296" draw:name="Content Placeholder 7" svg:x="5.69792in" svg:y="1.75in" svg:width="3.1875in" svg:height="2.39063in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image14.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id181" presentation:style-name="a1297" draw:name="Content Placeholder 8" svg:x="1.11343in" svg:y="4.30729in" svg:width="3.18981in" svg:height="2.39236in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image15.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id182" presentation:style-name="a1298" draw:name="Content Placeholder 9" svg:x="5.69676in" svg:y="4.30729in" svg:width="3.18981in" svg:height="2.39236in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image16.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL21():
    
    """Build Element draw:page for Master1-PPL21 """
    
    elem = build_element( """<draw:page draw:name="Slide13" draw:style-name="a1300" draw:master-page-name="Master1-Layout21-twoObjAndObj-Title,-2-Content-and-Content" presentation:presentation-page-layout-name="Master1-PPL21" draw:id="Slide-268">
<draw:frame draw:id="id183" presentation:style-name="a1304" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1303" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1301" text:class-names="">
ppLayoutTwoObjectsAndObject</text:span>
<text:span text:style-name="a1302" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id184" presentation:style-name="a1305" draw:name="Content Placeholder 5" svg:x="1.11458in" svg:y="1.75in" svg:width="3.1875in" svg:height="2.39063in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image17.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id185" presentation:style-name="a1306" draw:name="Content Placeholder 6" svg:x="1.11343in" svg:y="4.30729in" svg:width="3.18981in" svg:height="2.39236in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image18.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id186" presentation:style-name="a1307" draw:name="Content Placeholder 7" svg:x="5.20833in" svg:y="2.66233in" svg:width="4.16667in" svg:height="3.125in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image19.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL22():
    
    """Build Element draw:page for Master1-PPL22 """
    
    elem = build_element( """<draw:page draw:name="Slide14" draw:style-name="a1309" draw:master-page-name="Master1-Layout22-twoObjAndTx-Title,-2-Content-and-Text" presentation:presentation-page-layout-name="Master1-PPL22" draw:id="Slide-269">
<draw:frame draw:id="id187" presentation:style-name="a1313" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1312" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1310" text:class-names="">
ppLayoutTwoObjectsAndText</text:span>
<text:span text:style-name="a1311" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id188" presentation:style-name="a1314" draw:name="Content Placeholder 5" svg:x="1.11458in" svg:y="1.75in" svg:width="3.1875in" svg:height="2.39063in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image20.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id189" presentation:style-name="a1315" draw:name="Content Placeholder 6" svg:x="1.11343in" svg:y="4.30729in" svg:width="3.18981in" svg:height="2.39236in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image21.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id190" presentation:style-name="a1323" draw:name="Text Placeholder 4" svg:x="5.08333in" svg:y="1.75in" svg:width="4.41667in" svg:height="4.94965in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1318">
<text:list-item>
<text:p text:style-name="a1317" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1316" text:class-names="">
Text(4)</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1322">
<text:list-item>
<text:list text:style-name="a1322">
<text:list-item>
<text:p text:style-name="a1321" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1319" text:class-names="">
For ppLayoutTwoObjectsAndText</text:span>
<text:span text:style-name="a1320" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL23():
    
    """Build Element draw:page for Master1-PPL23 """
    
    elem = build_element( """<draw:page draw:name="Slide15" draw:style-name="a1325" draw:master-page-name="Master1-Layout23-twoObjOverTx-Title-and-2-Content-over-Text" presentation:presentation-page-layout-name="Master1-PPL23" draw:id="Slide-270">
<draw:frame draw:id="id191" presentation:style-name="a1329" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1328" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1326" text:class-names="">
ppLayoutTwoObjectsOverText</text:span>
<text:span text:style-name="a1327" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id192" presentation:style-name="a1330" draw:name="Content Placeholder 5" svg:x="1.11458in" svg:y="1.75in" svg:width="3.1875in" svg:height="2.39063in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image22.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id193" presentation:style-name="a1331" draw:name="Content Placeholder 6" svg:x="5.69792in" svg:y="1.75in" svg:width="3.1875in" svg:height="2.39063in" style:rel-width="scale" style:rel-height="scale" presentation:class="graphic" presentation:placeholder="false">
<draw:image xlink:href="media/image23.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id194" presentation:style-name="a1339" draw:name="Text Placeholder 4" svg:x="0.5in" svg:y="4.30729in" svg:width="9in" svg:height="2.39236in" presentation:class="outline" presentation:placeholder="false">
<draw:text-box>
<text:list text:style-name="a1334">
<text:list-item>
<text:p text:style-name="a1333" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1332" text:class-names="">
Text(4)</text:span>
</text:p>
</text:list-item>
</text:list>
<text:list text:style-name="a1338">
<text:list-item>
<text:list text:style-name="a1338">
<text:list-item>
<text:p text:style-name="a1337" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1335" text:class-names="">
For ppLayoutTwoObjectsOverText</text:span>
<text:span text:style-name="a1336" text:class-names="" />
</text:p>
</text:list-item>
</text:list>
</text:list-item>
</text:list>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def draw_8_page_Master1_PPL24():
    
    """Build Element draw:page for Master1-PPL24 """
    
    elem = build_element( """<draw:page draw:name="Slide16" draw:style-name="a1341" draw:master-page-name="Master1-Layout24-tbl-Title-and-Table" presentation:presentation-page-layout-name="Master1-PPL24" draw:id="Slide-271">
<draw:frame draw:id="id195" presentation:style-name="a1345" draw:name="Title 1" svg:x="0.5in" svg:y="0.30035in" svg:width="9in" svg:height="1.25in" presentation:class="title" presentation:placeholder="false">
<draw:text-box>
<text:p text:style-name="a1344" text:class-names="" text:cond-style-name="">
<text:span text:style-name="a1342" text:class-names="">
ppLayoutTable</text:span>
<text:span text:style-name="a1343" text:class-names="" />
</text:p>
</draw:text-box>
<svg:title />
<svg:desc />
</draw:frame>
<draw:frame draw:id="id196" presentation:style-name="a1346" draw:name="Table Placeholder 2" svg:x="0.5in" svg:y="1.75in" svg:width="9in" svg:height="4.94965in" presentation:class="table" presentation:placeholder="true">
<svg:title />
<svg:desc />
</draw:frame>
</draw:page>
""" )
    
    return elem

def presentation_8_settings_presentation_8_settings():
    
    """Build Element presentation:settings for presentation:settings """
    
    elem = build_element( """<presentation:settings />
""" )
    
    return elem



# Set values in func_quick_lookupD
func_quick_lookupD["Master1-PPL1"] = draw_8_page_Master1_PPL1
func_quick_lookupD["Master1-PPL12"] = draw_8_page_Master1_PPL12
func_quick_lookupD["Master1-PPL13"] = draw_8_page_Master1_PPL13
func_quick_lookupD["Master1-PPL14"] = draw_8_page_Master1_PPL14
func_quick_lookupD["Master1-PPL15"] = draw_8_page_Master1_PPL15
func_quick_lookupD["Master1-PPL16"] = draw_8_page_Master1_PPL16
func_quick_lookupD["Master1-PPL17"] = draw_8_page_Master1_PPL17
func_quick_lookupD["Master1-PPL18"] = draw_8_page_Master1_PPL18
func_quick_lookupD["Master1-PPL19"] = draw_8_page_Master1_PPL19
func_quick_lookupD["Master1-PPL2"] = draw_8_page_Master1_PPL2
func_quick_lookupD["Master1-PPL20"] = draw_8_page_Master1_PPL20
func_quick_lookupD["Master1-PPL21"] = draw_8_page_Master1_PPL21
func_quick_lookupD["Master1-PPL22"] = draw_8_page_Master1_PPL22
func_quick_lookupD["Master1-PPL23"] = draw_8_page_Master1_PPL23
func_quick_lookupD["Master1-PPL24"] = draw_8_page_Master1_PPL24
func_quick_lookupD["Master1-PPL4"] = draw_8_page_Master1_PPL4
func_quick_lookupD["presentation:settings"] = presentation_8_settings_presentation_8_settings




# Set values in master_page_name_lookupD
master_page_name_lookupD["Master1-PPL1"] = "Master1-Layout1-title-Title-Slide"
master_page_name_lookupD["Master1-PPL12"] = "Master1-Layout12-tx-Title-and-Text"
master_page_name_lookupD["Master1-PPL13"] = "Master1-Layout13-twoColTx-Title-and-2-Column-Text"
master_page_name_lookupD["Master1-PPL14"] = "Master1-Layout14-txOverObj-Title-and-Text-over-Content"
master_page_name_lookupD["Master1-PPL15"] = "Master1-Layout15-txAndObj-Title,-Text,-and-Content"
master_page_name_lookupD["Master1-PPL16"] = "Master1-Layout16-objAndTx-Title,-Content-and-Text"
master_page_name_lookupD["Master1-PPL17"] = "Master1-Layout17-txAndTwoObj-Title,-Text,-and-2-Content"
master_page_name_lookupD["Master1-PPL18"] = "Master1-Layout18-objAndTwoObj-Title,-Content,-and-2-Content"
master_page_name_lookupD["Master1-PPL19"] = "Master1-Layout19-objOverTx-Title-and-Content-over-Text"
master_page_name_lookupD["Master1-PPL2"] = "Master1-Layout2-obj-Title-and-Content"
master_page_name_lookupD["Master1-PPL20"] = "Master1-Layout20-fourObj-Title-and-4-Content"
master_page_name_lookupD["Master1-PPL21"] = "Master1-Layout21-twoObjAndObj-Title,-2-Content-and-Content"
master_page_name_lookupD["Master1-PPL22"] = "Master1-Layout22-twoObjAndTx-Title,-2-Content-and-Text"
master_page_name_lookupD["Master1-PPL23"] = "Master1-Layout23-twoObjOverTx-Title-and-2-Content-over-Text"
master_page_name_lookupD["Master1-PPL24"] = "Master1-Layout24-tbl-Title-and-Table"
master_page_name_lookupD["Master1-PPL4"] = "Master1-Layout4-twoObj-Two-Content"


# Set values in layout_page_name_lookupD
layout_page_name_lookupD["Master1-Layout1-title-Title-Slide"] = "Master1-PPL1"
layout_page_name_lookupD["Master1-Layout12-tx-Title-and-Text"] = "Master1-PPL12"
layout_page_name_lookupD["Master1-Layout13-twoColTx-Title-and-2-Column-Text"] = "Master1-PPL13"
layout_page_name_lookupD["Master1-Layout14-txOverObj-Title-and-Text-over-Content"] = "Master1-PPL14"
layout_page_name_lookupD["Master1-Layout15-txAndObj-Title,-Text,-and-Content"] = "Master1-PPL15"
layout_page_name_lookupD["Master1-Layout16-objAndTx-Title,-Content-and-Text"] = "Master1-PPL16"
layout_page_name_lookupD["Master1-Layout17-txAndTwoObj-Title,-Text,-and-2-Content"] = "Master1-PPL17"
layout_page_name_lookupD["Master1-Layout18-objAndTwoObj-Title,-Content,-and-2-Content"] = "Master1-PPL18"
layout_page_name_lookupD["Master1-Layout19-objOverTx-Title-and-Content-over-Text"] = "Master1-PPL19"
layout_page_name_lookupD["Master1-Layout2-obj-Title-and-Content"] = "Master1-PPL2"
layout_page_name_lookupD["Master1-Layout20-fourObj-Title-and-4-Content"] = "Master1-PPL20"
layout_page_name_lookupD["Master1-Layout21-twoObjAndObj-Title,-2-Content-and-Content"] = "Master1-PPL21"
layout_page_name_lookupD["Master1-Layout22-twoObjAndTx-Title,-2-Content-and-Text"] = "Master1-PPL22"
layout_page_name_lookupD["Master1-Layout23-twoObjOverTx-Title-and-2-Content-over-Text"] = "Master1-PPL23"
layout_page_name_lookupD["Master1-Layout24-tbl-Title-and-Table"] = "Master1-PPL24"
layout_page_name_lookupD["Master1-Layout4-twoObj-Two-Content"] = "Master1-PPL4"

if __name__ == "__main__":
    print( master_page_name_lookupD["Master1-PPL24"] )
