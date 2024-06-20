#sync_data_tree_folders

from pathlib import Path
import os

class SyncDataTreeFolders: 
  
  def readTreePathFile(__, path_folder_sync):
    data = []
    for root, dirs, files in os.walk(path_folder_sync):
      for file in files:
        file_path = Path(root) / file
        _file_ext = file_path.suffix
        _file_name = file_path.stem
        _file_path_text = root + "\\"
        _dict_file = dict(file_name=_file_name, file_path_text=_file_path_text, file_ext=_file_ext)
        data.append(_dict_file)
    return data
