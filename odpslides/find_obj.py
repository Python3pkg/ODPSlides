# Python 2 and 3




from odpslides.namespace import XMLNS_STR, force_to_short, force_to_tag, ODF_NAMESPACES

def NS( path_or_tag ): 
    """
    force into tag format like: '{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table' 
    
    (This is for backward compatibility... this is same as "force_to_tag".
    """
    return force_to_tag( path_or_tag )
    
        
def NS_attrib( attD ):
    """
    Convert a dictionary of attrib to tag format 
    like: '{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table' : 'value'
    """
    D = {}
    for key,val in list(attD.items()):
        D[ NS(key) ] = val
    return D


def elem_set(elem, path_or_tag, val, nsOD):
    """Allows short path for element set value"""
    tag = NS( path_or_tag, nsOD )
    elem.set( tag, val )
    

def find_elem_w_attrib(path_or_tag, parent, nsOD, attrib=None, nth_match=0, return_list=False ):
    """
    Find Element(s) in parent with matching attrib (if any)
    Return the nth matching element (defaults to 1st one, index=0)
    Also returns the global position (i_match) in the parent of attrib match
    
    Return None if no matching Element found
    """
    
    tag = NS( path_or_tag, nsOD )
    
    # Create dictionary of 
    D = {}
    if attrib:
        for atag,val in list(attrib.items()):
            atag = NS( atag, nsOD )
            D[atag] = val
    
    matchL = parent.findall( tag )
    returnL = []
    
    for i_match,elem in enumerate(matchL):
        got_attrib = True
        for atag, val in list(D.items()):
            if elem.get(atag, None) != val:
                got_attrib = False
        if got_attrib:
            returnL.append( (elem, i_match) )
    
    # If nothing matches, return None
    if len(returnL)==0:
        return None, None
    
    # Can return entire list or nth matching Element
    if return_list:
        return returnL  # a list of tuples (elem, i_match)
    else:
        # an extra line just to remind me of the tuple returned
        elem, i_match = returnL[nth_match]
        return elem, i_match
   

if __name__ == "__main__":
    
    
    print( NS( 'draw:page'  ) )
    print( NS( 'draw:page/draw:frame'  ) )
    print('............................')
    print( force_to_tag( 'draw:page'  ) )
    print( force_to_tag( 'draw:page/draw:frame'  ) )
    
    print('............................')
    print( NS_attrib( {'draw:id':'id1'}  ) )
    
