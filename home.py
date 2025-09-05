from flet import *
from base64_string_icon_path import icons
hovering = False

def home(page):
    page.padding=1
    page.bgcolor="#2F4F7F"
    page.scroll="auto"
    page.update()
    def go_to_add_page(e):
        from add_page import add_page
        page.controls.clear()
        add_page(page)
        page.update()
    def go_to_normal_subject(e):
        from normal_subject import normal_subject
        page.controls.clear()
        normal_subject(page)
        page.update()

    def go_to_youtub_page(e):
        from youtub import youtub
        page.controls.clear()
        youtub(page)
        page.update()

    def go_to_bac_subject_page(e):
        from bac_subject import bac_subject
        page.controls.clear()
        bac_subject(page)
        page.update()


    def go_to_lessons_page(e):
        from lessons import lessons

        page.controls.clear()
        lessons(page)
        page.update()
    def animate_buttons(e):
        global hovering
        if e.data == 'true' and not hovering:

            e.control.scale = 1.2
            hovering = True
        elif e.data == "false" and hovering:
            e.control.scale=1
            hovering = False
        page.update()
    # HEADER

    def open_drawer(e):
        page.drawer.open = True
        page.update()
    page.drawer = NavigationDrawer(
        bgcolor="#2F4F7F",
        controls=[ListTile(Container(content=Column(controls=[
            ElevatedButton(bgcolor='#8A0000',color='white',height=60,on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[13],width=50,height=50),Text('home',size=20,text_align=TextAlign.CENTER)])),
            ElevatedButton(bgcolor='#8A0000',color="white",height=60,on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[0],width=50,height=50),Text('aboutus',size=20,text_align=TextAlign.CENTER)])),
            ElevatedButton(bgcolor='#8A0000',color="white",height=60,on_hover=animate_buttons,content=Row(controls=[Image(src_base64=icons[0],width=50,height=50),Text('give feedback',size=20,text_align=TextAlign.CENTER)])),
            ElevatedButton(bgcolor='#8A0000',color="white",height=60,on_hover=animate_buttons,on_click=go_to_add_page,content=Row(controls=[Image(src_base64=icons[0],width=50,height=50),Text('Add',size=20,text_align=TextAlign.CENTER)])),
            
            ],
            scroll='auto'))

            )])

    page.appbar = AppBar(
        bgcolor='#2F4F5F',
        title=Text('BAC DZ - algeria futur',size=20,weight='bold',text_align=TextAlign.CENTER,offset=Offset(0.1,0),color='white'),
        leading=ElevatedButton('| | |',on_click=open_drawer,on_hover=animate_buttons,color='black',bgcolor='white',width=40,height=40,offset=Offset(0.2,0)),
        center_title=True)


    
    


    


    first_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries',color='white',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('we offert a complet and well-structured lessons for all BAC subject ',color='white',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#2F4F2F ',on_hover=animate_buttons,on_click=go_to_lessons_page,content=Container(content=Stack([Image(src_base64=icons[17],width=50,height=50,top=5,left=0),Text('lessons and summaries',size=20,text_align=TextAlign.CENTER,offset=Offset(0.1,0))])))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor='#4CAF51',
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )


    second_frame = Row([
        Container(
            content=Column([
                Text('youtube channel',color='white',weight='bold',size=33),
                Text('all what you need from channel for all subject',color='white',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#CC0000',on_hover=animate_buttons,on_click=go_to_youtub_page,content=Container(content=Stack([Image(src_base64=icons[24],width=60,height=60,top=0,left=0),Text('youtube          channel',size=20,text_align=TextAlign.CENTER,offset=Offset(0.1,0))])),offset=Offset(0,0.6))],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor='#FF3737',
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    therd_frame = Row([
        Container(
            content=Column([
                Text('previous BAC subject ',color='black',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('We offert all past BAc test for more trainig',color='black',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#999900',on_hover=animate_buttons,on_click=go_to_bac_subject_page,content=Container(content=Stack([Image(src_base64=icons[23],width=60,height=60,top=0,left=0),Text('BAC                           subject',size=20,text_align=TextAlign.CENTER,offset=Offset(0.1,0))])))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor='#CCCC66',
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    fourth_frame = Row([
        Container(
            content=Column([
                Text('subject of the school year',color='black',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('we also offert the school year subject ',color='black',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#7A288A',on_hover=animate_buttons,on_click=go_to_normal_subject,content=Container(content=Stack([Image(src_base64=icons[23],width=60,height=60,top=0,left=0),Text('school year                           subject',size=20,text_align=TextAlign.CENTER,offset=Offset(0.1,0))])))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor='#C7B8EA',
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )


    fifth_frame = Row([
        Container(
            content=Column([
                Text('Ask AI',color='white',weight='bold',size=33),
                Text('if you are confuse ask AI for more information',color='white',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#032B44',on_hover=animate_buttons,content=Container(content=Stack([Image(src_base64=icons[1],width=50,height=50,top=0,left=0),Text('ask                             AI',size=20,text_align=TextAlign.CENTER,offset=Offset(0.1,0))])))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            bgcolor='#2F4F9F',
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    six_frame = Row([
        Container(
            content=Column([
                Text('ZOOM cours ',color='white',weight='bold',size=33),
                Text('COMMING SOON',color='white',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(text='COMMING SOON',width=200,height=60,color='white',bgcolor='#8A0000',style=ButtonStyle(text_style=TextStyle(size=20)))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )
    def page_resaize(e):
        if page.width < 600:
            page.controls.append(Column(controls=[first_frame,second_frame,therd_frame,fourth_frame,fifth_frame]))

        else:
            page.controls.append(Row(controls=[first_frame,second_frame],alignment= MainAxisAlignment.CENTER,spacing=100))
            page.controls.append(Row(controls=[therd_frame,fourth_frame],alignment= MainAxisAlignment.CENTER,spacing=100))
            page.controls.append(Row(controls=[fifth_frame],alignment= MainAxisAlignment.CENTER,spacing=100))


        page.update()
    page.on_resize = page_resaize
    page_resaize(None)
