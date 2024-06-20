from model.folders import Folders
from model.folders_syncs import FoldersSyncs
from controller.sync_data_tree_folders import SyncDataTreeFolders

def main():
  print("Bismillah --> RUN")
  
  _folders = Folders()
  ct_folders = _folders.create_table()
  if not ct_folders:
    print(ct_folders)
    exit()

  _folders_syncs = FoldersSyncs()
  ct_folders_syncs = _folders_syncs.create_table()
  if not ct_folders_syncs:
    print(ct_folders)
    exit()

  path_file = "C:\\Users\\user\\Documents\\MY-CODE\\PYTHON\\python-sync-folderandfile\\FOLDERSYNC"

  _sync_data_tree_folders = SyncDataTreeFolders()
  _data_tree_folders = _sync_data_tree_folders.readTreePathFile(path_file)

  # check
  for info in _data_tree_folders:
    print("Result: ", info["file_name"])
  

if __name__ == "__main__":
  main()