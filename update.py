import os
import time
import shutil
print('you have to have git hub terminal installed for this update to work')
time.sleep(10)
os.chdir('..')
shutil.rmtree('DirCleaner')
os.system('git clone https://github.com/WHYSOEASY/DirCleaner.git')
print('Update Finished!!!!')

