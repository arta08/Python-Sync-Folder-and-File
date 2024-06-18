from model.folders import Folders
from model.folders_syncs import FoldersSyncs

def main():
  print("Bismillah --> RUN")
  _folders = Folders()
  _folders_syncs = FoldersSyncs()

  ct_folders = _folders.create_table
  if not ct_folders:
    print(ct_folders)
    exit()

  ct_folders_syncs = _folders_syncs.create_table
  if not ct_folders_syncs:
    print(ct_folders)
    exit()

  

if __name__ == "__main__":
  main()