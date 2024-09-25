import os
import shutil


directory_to_sort = '/Users/nikolastanner/Music/Logic'
directory_for_trash = '/Users/nikolastanner/Music/Logic/Trash'
directory_for_good = '/Users/nikolastanner/Music/Logic/Good'


def sort_files(directory):
     for file_name in os.listdir(directory):
         file_path = directory_to_sort + "/" + file_name
         if (file_name.startswith("trash")):
             shutil.move(file_path,directory_for_trash)
         if (file_name.startswith("good")):
             shutil.move(file_path,directory_for_good)
sort_files(directory_to_sort)
