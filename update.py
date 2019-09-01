import os
import time
import shutil
print('Note: Git must be installed for the update to work.')
time.sleep(10)
os.chdir('..')
os.system('rmdir /q /s DirCleaner')
os.system('git clone https://github.com/WHYSOEASY/DirCleaner.git')
print('Update finished.')
