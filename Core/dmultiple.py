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

#variables
n_list=[]

# download files
for x in f:
    x = x.rstrip('\n')
    xfileext = x.split('/')[-1]
    xfileext2 = xfileext.split('.')[-1]
    clean=xfileext.rstrip(xfileext2+'.')
    url=x
    r = requests.get(url)
    
    #append list and check 
    n_list_exists=n_list.count(clean)
    n_list.append(clean)
    # create dupe () to simulate windows copy
    #create ()
    if (n_list_exists==0):
        dupe_extend = ''
    else:
        dupe = n_list_exists
        dupe_extend = '('+str(dupe)+')'
    
    
    print (clean)
    with open(xfileext, 'wb') as u:
            u.write(r.content)
            u.close()
            #rename
            clean = xfileext.rstrip(xfileext2+'.')+dupe_extend+'.'+xfileext2
            print ("saved as",clean)
            os.rename(u.name,clean)
            shutil.move(clean, pathmin+'assets')

