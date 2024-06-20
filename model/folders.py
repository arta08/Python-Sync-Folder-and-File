import sqlite3

con = sqlite3.connect('python_listfolderandfile.db')
cur = con.cursor()

class Folders:
  # def __init__(self):
  #   print("run -> Folders")

  # @property
  def create_table(self):
    try:
      cur.execute("CREATE TABLE IF NOT EXISTS folders (id INTEGER PRIMARY KEY AUTOINCREMENT, file_path TEXT, file_name varchar, file_ext varchar, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
      con.commit()
      con.close()
      return True
      
    except sqlite3.OperationalError as e:
      con.close()
      print(f"Failed : {e}")
      return False