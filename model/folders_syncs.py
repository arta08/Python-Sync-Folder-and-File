import sqlite3

con = sqlite3.connect('python_listfolderandfile.db')
cur = con.cursor()

class FoldersSyncs: 
  def __init__(self):
    print("run -> FoldersSyncs")

  @property
  def create_table(self):
    try:
      cur.execute("CREATE TABLE IF NOT EXISTS folders_syncs (id INTEGER PRIMARY KEY AUTOINCREMENT, file_path TEXT, file_name varchar, file_ext varchar, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
      con.commit()

    except sqlite3.OperationalError as e:
      con.close()
      print(f"Failed : {e}")
      return False
    
    cur.execute("DELETE FROM folders_syncs")
    con.commit()
    con.close()
    return True