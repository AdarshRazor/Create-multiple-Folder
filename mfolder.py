import os
import string

#root_path = 'C:/Users/Adarsh/Dropbox/Project R.Y.U.N'
#folders = ['Folder 1','Folder x','Folder y']

path=os.getcwd()

root_path=path

foldernum=int(input("How many path you want to create :"))

folders=[]

for i in range(foldernum):
    folderex=input()
    folders.append(folderex)

for folder in folders:
    os.mkdir(os.path.join(root_path,folder))

    