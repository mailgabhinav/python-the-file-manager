import os
import shutil

fromdir="C:/Users/mailg/Downloads"
todir="C:/Users/mailg/OneDrive/Desktop/NewFolder"

listoffiles=os.listdir(fromdir)

print(listoffiles)

for filename in listoffiles:
    name,extension=os.path.splitext(filename)
    print(extension)
    print(name)
    if extension=='':
        continue
    if extension in ["pdf"]:
        path1=fromdir+"/"+filename
        path2=todir+"/"+"NewFolder"
        path3=todir+"/"+"NewFolder"+"/"+filename
        print(path1)
        print(path3)
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
























