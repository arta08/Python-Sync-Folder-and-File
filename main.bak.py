import sqlite3
import os
from pathlib import Path

con = sqlite3.connect('python_listfolderandfile.db')
cur = con.cursor()

# Create Master Table
try:
    cur.execute("SELECT * FROM folders")
except sqlite3.OperationalError:
    cur.execute("CREATE TABLE folders (id INTEGER PRIMARY KEY AUTOINCREMENT, file_path TEXT, file_name varchar, file_ext varchar, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

# Create Backup table for SYNC
try:
    cur.execute("SELECT * FROM folders_syncs")
    cur.execute("DELETE FROM folders_syncs")
except sqlite3.OperationalError:
    cur.execute("CREATE TABLE folders_syncs (id INTEGER PRIMARY KEY AUTOINCREMENT, file_path TEXT, file_name varchar, file_ext varchar, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

# Read tree path file
folder_path = 'FOLDERSYNC'
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = Path(root) / file
        file_ext = file_path.suffix
        file_name = file_path.stem
        file_path_text = root + "\\"

        # Insert to table sync
        q_insert_folders = "INSERT INTO folders_syncs (file_path, file_name, file_ext) VALUES (?, ?, ?)"
        cur.execute(q_insert_folders, (file_path_text, file_name, file_ext))
        con.commit()

# Sync from table sync to master table
try : 
    q_insert_from_sync = "INSERT INTO folders (file_path, file_name, file_ext) SELECT file_path, file_name,file_ext FROM folders_syncs b WHERE NOT EXISTS (SELECT a.file_path, a.file_name, a.file_ext FROM folders a WHERE a.file_path = b.file_path AND a.file_name = b.file_name AND a.file_ext = b.file_ext)"
    cur.execute(q_insert_from_sync)
    con.commit()
except sqlite3.IntegrityError:
    print("Failed Sync Insert")

try :
    q_delete_nothing_in_sync = "DELETE FROM folders WHERE NOT EXISTS (SELECT 1 FROM folders_syncs b WHERE folders.file_path = b.file_path AND folders.file_name = b.file_name  AND folders.file_ext = b.file_ext)"
    cur.execute(q_delete_nothing_in_sync)
    con.commit()
except sqlite3.IntegrityError:
    print("Failed Sync Delete")

con.close()
