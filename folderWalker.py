import os
import sys
import time
timer=time.time()
print ('FolderName,File Count,Real Datasize,Datasize')
for foldername, subfolders, filenames in os.walk(sys.argv[1]):
    filesize=0
    filecount=0
    for filename in filenames:
        filesize=filesize+os.path.getsize(foldername+'\\'+filename)
        filecount=filecount+1
    if(filesize>=1073741824):
        print (foldername +','+str(filecount)+','+str(filesize)+','+'%2.1f'%(filesize/1073741824)+"GiB")
    elif(filesize>=1048576):
        print (foldername +','+str(filecount)+','+str(filesize)+','+'%2.1f'%(filesize/1048576)+"MiB")
    elif(filesize>=1024):
        print (foldername +','+str(filecount)+','+str(filesize)+','+'%2.1f'%(filesize/1024)+"KiB")
    else:
        print (foldername +','+str(filecount)+','+str(filesize)+','+'%d'%(filesize)+"B")
timer=time.time()-timer
print (str(timer)+"sec")
