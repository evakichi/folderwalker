import os
import sys
import zipfile
import time
timer=time.time()
zipfile_name=sys.argv[1]+'.zip'
print ('To Zip'+zipfile_name)
bk_zip = zipfile.ZipFile(zipfile_name,'w')
for foldername, subfolders, filenames in os.walk(sys.argv[1]):
    print('Adding files in {}'.format(foldername))
    bk_zip.write(foldername)
    for filename in filenames:
        bk_zip.write(os.path.join(foldername,filename))
bk_zip.close()
timer=time.time()-timer
print (str(timer)+"sec")
