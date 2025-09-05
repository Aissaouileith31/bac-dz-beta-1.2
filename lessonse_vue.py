import sqlite3
import flet as ft



def main(page: ft.Page):
    page.title = "Link App"
    arabic_db_path = r'database_of_lesson_and_sumeri_all_subject\arabic_lessons.db'
    conn = sqlite3.connect(arabic_db_path)
    cursor = conn.cursor()

    # حقل إدخال الرابط
    link_field = ft.TextField(hint_text="put the drive link of your file")

    def add_link(e):
        link = link_field.value
        cursor.execute('INSERT INTO arabic_lessons (link) VALUES (?)', (link,))
        conn.commit()
        link_field.value = ''
        page.controls.append(ft.ElevatedButton(text="Link",expand=True, on_click=lambda e, link=link: page.launch_url(link)))
        page.update()

    # زر إضافة الرابط
    page.controls = [
        link_field,
        ft.ElevatedButton(text="publi", on_click=add_link),
    ]

    # عرض الروابط المضافة
    cursor.execute('''
        SELECT link FROM arabic_lessons''')
    links = cursor.fetchall()
    for link in links:
        page.controls.append(ft.ElevatedButton(text="Link",expand=True, on_click=lambda e, link=link[0]: page.launch_url(link)))

    page.update()

ft.app(target=main,view=None,host='0.0.0.0',port=3135)