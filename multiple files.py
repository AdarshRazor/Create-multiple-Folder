#no. of files you want to create
filenum=int(input("How many path you want to create :"))

files=[]

#names of the files
for i in range(filenum):
    fileex=input()
    files.append(fileex)

#print(files)

for item in files:
    f=open(item,"w+")
