import os
import string

#root_path = 'C:/Users/your directory  [ onyly  create at fixed place ]'
#folders = ['Folder 1','Folder 2','Folder 3']

#take the current working directory
path=os.getcwd() 

#set the current working directory
root_path=path

#how many folder you wanted to make
foldernum=int(input("How many path you want to create :"))

folders=[]

#folder naming
for i in range(foldernum):
    folderex=input()
    folders.append(folderex)

for folder in folders:
    os.mkdir(os.path.join(root_path,folder))

    
