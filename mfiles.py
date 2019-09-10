
#f= open("guru99.txt","w+")

filenum=int(input("How many path you want to create :"))

files=[]

for i in range(filenum):
    fileex=input()
    files.append(fileex)

#print(files)

for item in files:
    f=open(item,"w+")