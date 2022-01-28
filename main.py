import os
import shutil


def my_function(a,b):
    return a+b


file = []
dict_Ext = {"IMAGES": ('.jpg', '.png', '.JPG', '.jpeg'),
            "VIDEO": ('.ogg', '.mp4',),
            "DOCUMENTS": ('.pdf', '.docx', '.doc', '.pps', '.PDF'),
            "MUSIQUE": ('.mp3', '.avi', 'm4a'),
            "LIVRE": ('.epub',)}

for el in dict_Ext:
    #Création de l'arborescence à partir des clés avec suppression si existe déjà
    ##Test History - Autre test
    if os.path.exists(f"c:\\temp\\CLE BM\\{el}"):
        os.rmdir(f"c:\\temp\\CLE BM\\{el}")
        os.makedirs(f"c:\\temp\\CLE BM\\{el}")
    else:
        os.makedirs(f"c:\\temp\\CLE BM\\{el}")
    print(el)
    #Recherche des fichiers correspondants à la clé
    for root, dirs, files in os.walk(f"c:\\temp\\BM\\"):
        for i in files:
            if os.path.splitext(i)[1] in dict_Ext[el]:
                shutil.copyfile(os.path.join(root, i), os.path.join(f"c:\\temp\\CLE BM\\{el}\\", i))

