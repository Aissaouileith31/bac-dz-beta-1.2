import flet as ft
import sqlite3 as sq

def crate_all_db():
	conn = sq.connect("arabic_lessons.db")
	cursor = conn.cursor()
	cursor.execute('''
			CREATE TABLE IF NOT EXISTS arabic_lessons(
				id INTEGER PRIMARY KEY,
				link TEXT 
				)
			''')
	print('data base created')
if __name__ == '__main__':
	crate_all_db()




