import sqlite3
from _config import DATABASE_PATH
print DATABASE_PATH
with sqlite3.connect(DATABASE_PATH) as connection:
	cursor=connection.cursor()
	cursor.execute("""CREATE TABLE tasks(task_id INTEGER primary key autoincrement, 
					name text not null,due_date text not null, priority integer not null, 
					status integer not null""")

	cursor.execute('''INSERT INTO tasks (name, due_date, priority, status) 
		VALUES("Finish this tutorial", "03/25/2015", 10, 1)''')
	cursor.execute(
	'INSERT INTO tasks (name, due_date, priority, status)'
	'VALUES("Finish Real Python Course 2", "03/25/2015", 10, 1)'
	)