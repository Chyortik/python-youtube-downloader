import os

def createFolderForTiff(folder_name, path):
    _fold_name = folder_name.replace(':', ' ').replace('.', ' ')
    _path = path


    if not(os.path.exists(_path+"/"+_fold_name)):
        os.chdir(_path)
        os.mkdir(_fold_name)
    else:
        print('Папка C:/'+folder_name+' уже существует!')


folder_names = ["downloaded"]
pathh = "C:/"

for name in folder_names:
    createFolderForTiff(name,pathh)