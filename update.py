import os
import requests
import zipfile

def update():
    print('Starting update')
    cwd = os.getcwd()
    os.chdir(cwd)
    os.system('cd ..')
    os.system('del /F /Q /A DirCleaner')
    os.system('del /F /Q /A master.zip')
    requested = requests.get('https://github.com/WHYSOEASY/DirCleaner/archive/master.zip')
    content = requested.content
    f  = open('master.zip','wb')
    f.write(content)
    f.close()
    zipped = zipfile.ZipFile('master.zip')
    zipped.extractall()
    print('Finished update')

update()
    
