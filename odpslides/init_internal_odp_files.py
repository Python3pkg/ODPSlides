# Support Python 2 and 3




import time
import sys

if sys.version_info < (3,):
    import odpslides.ElementTree_27OD as ET
else:
    import odpslides.ElementTree_34OD as ET
from odpslides.template_xml_file import TemplateXML_File
from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag

def meta_time():
    "Return time string in meta data format"
    t = time.localtime()
    stamp = "%04d-%02d-%02dT%02d:%02d:%02d" % (t[0], t[1], t[2], t[3], t[4], t[5])
    return stamp

def get_manifest_elem():
    return TemplateXML_File( manifest_str )

def get_meta_xml_str():
    mtime = meta_time()
    return meta_str%(mtime, mtime)

def get_empty_content_elem():
    return TemplateXML_File( content_str )
    
def get_final_presentation_elem():

    return ET.Element( force_to_tag('presentation:settings') )

def get_empty_styles_elem():
    return TemplateXML_File( styles_str )

def get_mimetype_str():
    return """application/vnd.oasis.opendocument.presentation"""

def get_settings_xml_str():
    return settings_str

manifest_str = """<manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0">
<manifest:file-entry manifest:full-path="/" manifest:media-type="application/vnd.oasis.opendocument.presentation"/>
<manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/>
<manifest:file-entry manifest:full-path="settings.xml" manifest:media-type="text/xml"/>
<manifest:file-entry manifest:full-path="styles.xml" manifest:media-type="text/xml"/>
<manifest:file-entry manifest:full-path="Thumbnails/thumbnail.png" manifest:media-type="image/png"/>
<manifest:file-entry manifest:full-path="meta.xml" manifest:media-type="text/xml"/>
<manifest:file-entry manifest:full-path="mimetype" manifest:media-type="text/plain"/>
<manifest:file-entry manifest:full-path="META-INF/manifest.xml" manifest:media-type="text/xml"/>
</manifest:manifest>"""

meta_str = """<office:document-meta xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:xlink="http://www.w3.org/1999/xlink" office:version="1.1">
<office:meta>
<meta:generator>MicrosoftOffice/14.0 MicrosoftPowerPoint</meta:generator>
<dc:title>ppLayoutTitle</dc:title>
<meta:initial-creator>ODPSlides</meta:initial-creator>
<dc:creator>ODPSlides</dc:creator>
<meta:creation-date>%s</meta:creation-date>
<dc:date>%s</dc:date>
<meta:editing-cycles>1</meta:editing-cycles>
<meta:editing-duration>PT0S</meta:editing-duration>
<meta:document-statistic meta:paragraph-count="38" meta:word-count="60"/>
</office:meta>
</office:document-meta>"""

settings_str = """<office:document-settings xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"/>"""

styles_str = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<office:document-styles xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0" xmlns:smil="urn:oasis:names:tc:opendocument:xmlns:smil-compatible:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0">
<office:styles>

    <style:default-style style:family="graphic">
    <style:graphic-properties draw:fill="solid" draw:fill-color="#4f81bd" draw:opacity="100%" draw:stroke="solid" svg:stroke-width="0.02778in" svg:stroke-color="#385d8a" svg:stroke-opacity="100%"/>
    </style:default-style>

</office:styles>
<office:automatic-styles>
    <style:page-layout style:name="pageLayout1">
    <style:page-layout-properties fo:page-width="10in" fo:page-height="7.5in" style:print-orientation="landscape" style:register-truth-ref-style-name=""/>
    </style:page-layout>
    <style:page-layout style:name="pageLayout3">
    <style:page-layout-properties fo:page-width="7.5in" fo:page-height="10in" style:print-orientation="portrait" style:register-truth-ref-style-name=""/>
    </style:page-layout>
    
</office:automatic-styles>
<office:master-styles>
    <draw:layer-set>
    <draw:layer draw:name="Master1-bg" draw:protected="true"/>
    </draw:layer-set>
    
</office:master-styles>
</office:document-styles>"""

content_str="""<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<office:document-content xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:smil="urn:oasis:names:tc:opendocument:xmlns:smil-compatible:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0">
<office:automatic-styles>
</office:automatic-styles>
<office:body>
    <office:presentation>
    </office:presentation>
</office:body>
</office:document-content>"""

if __name__ == "__main__":
    
    print( get_empty_content_elem() )
    print()
    print( get_empty_styles_elem() )
    print()
    print( get_meta_xml_str() )
    print()
    print( get_mimetype_str() )
    print()
    print( get_settings_xml_str() )
    print()
    print( get_manifest_elem() )
