import sqlite3
import os
from pathlib import Path

con = sqlite3.connect('python_listfolderandfile.db')
cur = con.cursor()

try:
    cur.execute("SELECT * FROM folders")
except sqlite3.OperationalError:
    cur.execute("CREATE TABLE folders (id INTEGER PRIMARY KEY AUTOINCREMENT, file_path TEXT, file_name varchar, file_ext varchar, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

folder_path = 'FOLDERSYNC'
for root, dirs, files in os.walk(folder_path):
    # print(root)
    for file in files:
        file_path = Path(root) / file
        file_ext = file_path.suffix
        file_name = file_path.stem
        file_path_text = root + "\\"

        # Insert to table
        q_insert_folders = "INSERT INTO folders (file_path, file_name, file_ext) VALUES (?, ?, ?)"
        cur.execute(q_insert_folders, (file_path_text, file_name, file_ext))
        con.commit()

con.close()
