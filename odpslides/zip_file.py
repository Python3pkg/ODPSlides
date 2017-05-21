# Support Python 2 and 3




import os
import sys
import zipfile
import time

from odpslides.template_xml_file import TemplateXML_File

here = os.path.abspath(os.path.dirname(__file__))


def zipfile_insert( zipfileobj, filename, data):
    """Create a file named filename, inside the zip archive.
    
       "data" is the encode('UTF-8') string that is placed into filename.

       (Not called by User)
    """

    if isinstance( data, TemplateXML_File ):
        data = data.tostring()

    # zip seems to struggle with non-ascii characters
    #data = data.encode('utf-8')

    now = time.localtime(time.time())[:6]
    info = zipfile.ZipInfo(filename)
    info.date_time = now
    info.compress_type = zipfile.ZIP_DEFLATED
    zipfileobj.writestr(info, data)


