import requests
import os
import pathlib
import shutil
import re
from pathlib import Path

path = pathlib.Path(__file__).parent.absolute()
pathmin = str(path).rstrip('Core')

#txt file to read lines from
f = open("oneplus8links.txt", "r")
sum=0
# download files
for x in f:
    x = x.rstrip('\n')
    xfileext = x.split('/')[-1]
    xfileext2 = xfileext.split('.')[-1]
    clean=xfileext.rstrip(xfileext2+'.')
    url=x
    r = requests.get(url)
    sum=sum+1
    with open(xfileext, 'wb') as u:
            u.write(r.content)
            u.close()
            #rename
            clean= xfileext.rstrip(xfileext2+'.')+'('+str(sum)+')'+'.'+xfileext2
            print (clean)
            os.rename(u.name,clean)
            shutil.move(clean, pathmin+'assets')
            
