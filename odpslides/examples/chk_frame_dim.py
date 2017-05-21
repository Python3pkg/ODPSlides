import matplotlib.pyplot as plt
from odpslides.presentation import Presentation


PC_CENTER = 0
PC_CONTENT = 0
PC_RIGHT = None # [100,100,100,100,100]
#PC_RIGHT = [-100,-100,-100,-100,-100]
PC_UP = None # [100,100,100,100,100]
#PC_UP = [-100,-100,-100,-100,-100]

P = Presentation(background_color='#ccffcc',
                 background_image=r'D:\py_proj_2015\ODPSlides\odpslides\templates\image1.png',
                 #grad_start_color='ff9999', grad_end_color="#ffffff", 
                 #grad_angle_deg=45, grad_draw_style='rectangle',
                 footer='Gaea Trilogy', show_date=True)

P.add_title_chart( title='Titan, Wizard, Demon', subtitle='John Varley',
                   pcent_stretch_center=PC_CENTER, pcent_stretch_content=PC_CONTENT,
                   pcent_move_content_right=PC_RIGHT, pcent_move_content_up=PC_UP)


P.add_titled_image( title='Locus, Nebula, Hugo', image_file='Titan.jpg',
                    pcent_stretch_center=PC_CENTER, pcent_stretch_content=PC_CONTENT,
                    pcent_move_content_right=PC_RIGHT, pcent_move_content_up=PC_UP)

P.add_titled_image( title='Locus, Nebula, Hugo', image_file='Titan.jpg',
                    image_2_file='Wizard.jpg', 
                    pcent_stretch_center=PC_CENTER, pcent_stretch_content=PC_CONTENT,
                    pcent_move_content_right=PC_RIGHT, pcent_move_content_up=PC_UP)


P.add_titled_image( title='Locus, Nebula, Hugo', image_file='Titan.jpg',
                    image_2_file='Wizard.jpg', image_3_file='Demon.jpg',
                    big_3rd_img_left=True,
                    pcent_stretch_center=PC_CENTER, pcent_stretch_content=PC_CONTENT,
                    pcent_move_content_right=PC_RIGHT, pcent_move_content_up=PC_UP)

P.add_titled_image( title='Locus, Nebula, Hugo', image_file='Titan.jpg',
                    image_2_file='Wizard.jpg', image_3_file='Demon.jpg',
                    big_3rd_img_left=False,
                    pcent_stretch_center=PC_CENTER, pcent_stretch_content=PC_CONTENT,
                    pcent_move_content_right=PC_RIGHT, pcent_move_content_up=PC_UP)

P.add_titled_image( title='Locus, Nebula, Hugo', image_file='Titan.jpg',
                    image_2_file='Wizard.jpg', image_3_file='Demon.jpg',
                    image_4_file='Demon.jpg',
                    pcent_stretch_center=PC_CENTER, pcent_stretch_content=PC_CONTENT,
                    pcent_move_content_right=PC_RIGHT, pcent_move_content_up=PC_UP)


P.add_titled_text_and_image( text_location='top',
                        title='Text on Top', title_font_color='',  image_2_file='./examples/robot.gif',
                        outline=['My Favorite Duck','    under fire'], text_font_color='', 
                        image_file='./examples/duck.gif', keep_aspect_ratio=True, 
                        pcent_stretch_center=PC_CENTER, pcent_stretch_content=PC_CONTENT, 
                        pcent_move_content_right=PC_RIGHT, pcent_move_content_up=PC_UP)

P.add_titled_text_and_image( text_location='bottom',
                        title='Text on Bottom', title_font_color='',  image_2_file='./examples/robot.gif',
                        outline=['My Favorite Duck','    under fire'], text_font_color='', 
                        image_file='./examples/duck.gif', keep_aspect_ratio=True, 
                        pcent_stretch_center=PC_CENTER, pcent_stretch_content=PC_CONTENT, 
                        pcent_move_content_right=PC_RIGHT, pcent_move_content_up=PC_UP)

P.add_titled_text_and_image( text_location='top',
                        title='Text on Top', title_font_color='',  
                        outline=['My Favorite Duck','    under fire'], text_font_color='', 
                        image_file='./examples/duck.gif', keep_aspect_ratio=True, 
                        pcent_stretch_center=PC_CENTER, pcent_stretch_content=PC_CONTENT, 
                        pcent_move_content_right=PC_RIGHT, pcent_move_content_up=PC_UP)

P.add_titled_text_and_image( text_location='bottom',
                        title='Text on Bottom', title_font_color='',  
                        outline=['My Favorite Duck','    under fire'], text_font_color='', 
                        image_file='./examples/duck.gif', keep_aspect_ratio=True, 
                        pcent_stretch_center=PC_CENTER, pcent_stretch_content=PC_CONTENT, 
                        pcent_move_content_right=PC_RIGHT, pcent_move_content_up=PC_UP)

sL = ['1st','\t2nd','\t\t3rd','            4th','Normal < 1st but > 9','    Indent 2nd']
s2L = ['1st(2)','\t2nd(2)','\t\t3rd(2)','            4th(2)','Normal < 1st but > 9(2)','    Indent 2nd(2)']
        
P.add_titled_outline_chart( title='My Second Title', outline=sL, 
                            title_font_color='blue', text_font_color='green',
                            pcent_stretch_center=PC_CENTER, pcent_stretch_content=PC_CONTENT,
                            pcent_move_content_right=PC_RIGHT, pcent_move_content_up=PC_UP)

P.add_titled_two_outline_chart(title='2 Columns of Text', title_font_color='', 
                               outline=sL, text_font_color='r', 
                               outline_2=s2L, text_2_font_color='g', 
                               pcent_stretch_center=PC_CENTER, pcent_stretch_content=PC_CONTENT,
                               pcent_move_content_right=PC_RIGHT, pcent_move_content_up=PC_UP)
countD = {}
content_item_N = 1
def get_class_name( frame_class ):
    global content_item_N
    N = countD.get(frame_class, 1)
    countD[frame_class] = N + 1
    
    if 1:#if frame_class not in ['date-time', 'footer', 'page-number', 'title']:
        cid = '(%i)\n'%content_item_N
        content_item_N += 1
    else:
        cid = ''
    
    if N==1:
        return cid + frame_class
    else:
        return cid + frame_class + ' #%i'%N
        

for ipage,page in enumerate(P.new_content_pageL):
    countD = {}
    content_item_N = 1
    fig = plt.figure()
    print('Page #%i, %s'%(ipage+1, page.disp_name))
    print('Top  ', page.top_blockade)
    print('Bot  ', page.bottom_blockade)
    print('Right',page.right_blockade)
    print('Left ',page.left_blockade)
    print('Unique Blockade Objects =',len(page.unique_blockadeD), sorted( page.unique_blockadeD.keys() ))
    for iframe,fd in enumerate(page.frame_dimL):
        print('    ',fd.bbox, fd.bottom_blockade)
        #print '       Top  ',fd.top_blockade
        #print '       Bot  ',fd.bottom_blockade
        #print '       Right',fd.right_blockade
        #print '       Left ',fd.left_blockade
        
        draw_frame = page.draw_frameL[iframe]
        bb = fd.bbox
        xL = [bb.left_x, bb.right_x, bb.right_x, bb.left_x,    bb.left_x]
        yL = [bb.top_y,  bb.top_y,   bb.bottom_y, bb.bottom_y, bb.top_y]
        plt.plot(xL, yL,  label=fd.my_frame_class, linewidth=3)
        
        plt.text(0.5*(bb.left_x + bb.right_x), 0.5*(bb.bottom_y + bb.top_y), 
                get_class_name(fd.my_frame_class),
                horizontalalignment='center', fontsize=18,
                verticalalignment='center')        
        
        for b in list(page.unique_blockadeD.values()):
            #for b in [fd.left_blockade, fd.right_blockade, fd.top_blockade, fd.bottom_blockade]:
            plt.plot( [b.p0.x, b.p1.x], [b.p0.y, b.p1.y], 'r-' )
        

        
    plt.ylim(8.0, 0.0)
    plt.xlim(0.0, 10.)
    
    #plt.savefig( 'Page%i_%s.png'%(ipage+1, page.disp_name.replace(' ','_')) )
        
        
    print('-'*77)

    #plt.legend(loc='best')
    #plt.grid(True)
    plt.title( 'Page #%i, %s'%(ipage+1, page.disp_name) )


plt.show()
 