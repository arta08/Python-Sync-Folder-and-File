#sync_data_tree_folders

from pathlib import Path

class SyncDataTreeFolders: 
  
  def readTreePathFile(folder_path):
    for root, dirs, files in os.walk(folder_path):
      for file in files:
        file_path = Path(root) / file
        file_ext = file_path.suffix
        file_name = file_path.stem
        file_path_text = root + "\\"
        