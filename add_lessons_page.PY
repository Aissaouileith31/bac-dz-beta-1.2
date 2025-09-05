import sqlite3
import flet as ft

def add_lessons(page):
    def go_to_home(e):
        from home import home
        page.controls.clear()
        home(page)
        page.update()
    page.title = "Link App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 300

    dropdown_value=None

    # Header Text
    title_text = ft.Text(
        "Add Arabic Lesson Link",
        size=22,
        weight="bold",
        color="blue"
    )

    # Input Field
    link_field = ft.TextField(
        hint_text="Paste the Google Drive link here",
        width=350,
        filled=True
    )
    def dropdown_change(e):
        nonlocal dropdown_value
        dropdown_value= e.control.value

    def publishe(e):
        link = link_field.value.strip()
        if not link:
            page.controls.append(ft.Text("⚠️ Please enter a link.", color="red"))
            page.update()
            return
        

        if dropdown_value=='arabic':

        
            try:
                arabic_db_path = r'database_of_lesson_and_sumeri_all_subject\arabic_lessons.db'
                conn = sqlite3.connect(arabic_db_path)
                cursor = conn.cursor()
                cursor.execute('INSERT INTO arabic_lessons (link) VALUES (?)', (link,))
                conn.commit()
                conn.close()

                link_field.value = ''
                page.controls.append(ft.Text("✅ Link added successfully!", color="green"))
            except Exception as ex:
                page.controls.append(ft.Text(f"❌ Error: {str(ex)}", color="red"))

                page.update()
            try:
                arabic_db_path = r'database_of_lesson_and_sumeri_all_subject\arabic_lessons.db'
                conn = sqlite3.connect(arabic_db_path)
                cursor = conn.cursor()
                cursor.execute('INSERT INTO arabic_lessons (link) VALUES (?)', (link,))
                conn.commit()
                conn.close()

                link_field.value = ''
                page.controls.append(ft.Text("✅ Link added successfully!", color="green"))
            except Exception as ex:
                page.controls.append(ft.Text(f"❌ Error: {str(ex)}", color="red"))

                page.update()        
    

    # Submit Button
    submit_button = ft.ElevatedButton(
        text="Publish",
        on_click=publishe,
        bgcolor="blue",
        color="white"
    )

    subject = ft.Dropdown(label='chouse the subject',width=200,options=[ft.dropdown.Option('arabic'),
        ft.dropdown.Option('math'),ft.dropdown.Option('since'),
        ft.dropdown.Option('phyzic'),ft.dropdown.Option('history & geo'),
        ft.dropdown.Option('eslamic ed'),ft.dropdown.Option('electric eng'),
        ft.dropdown.Option('mecanic eng'),ft.dropdown.Option('civil eng'),
        ft.dropdown.Option('prosess eng'),ft.dropdown.Option('english'),
        ft.dropdown.Option('frensh'),ft.dropdown.Option('economy'),
        ft.dropdown.Option('law'),ft.dropdown.Option('econommic & managemaent'),
        ft.dropdown.Option('acounting '),ft.dropdown.Option('germany'),
        ft.dropdown.Option('spanish'),ft.dropdown.Option('italy'),
        ft.dropdown.Option('art'), ft.dropdown.Option('amazigh')

        ],on_change=dropdown_change)

    # Layout
    page.controls = [
        ft.Column(
            [
                title_text,
                link_field,
                subject,
                submit_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    ]
    page.update()


