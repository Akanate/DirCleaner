#Get the modules i need
import os, shutil, time, glob, ctypes, datetime
from os.path import expanduser
#Checks the users have not got admin.
def admin_check():
    print('Checking this program is not running as admin')
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            print('You need to run this program without admin privilages')
            exit()
        else:
            print('Your all clear continuing')
            precheck()

#Checks if you have a junk file made to store rubbish files if not it creates one for you.
def precheck():
    print('Making a junk folder if it is already created will continue')
    junk = expanduser('~/Desktop/junk')
    if os.path.exists(junk):
        print('Already exists continuing')
        doc()
    else:
        print('Does not exist creating the folder')
        os.mkdir(junk)
        print('Created junk folder continuing')
        doc()

#Goes through all files and subdirs in documents looking for files which fit the filter
def doc():
    counter = 0
    print('Cleaning Documents')
    home = os.path.expanduser('~/Documents')
    junk = expanduser('~/Desktop/junk')
    for directory, _, filenames in os.walk(home):        
        for filename in filenames:
            try:
                from_path = os.path.join(directory,filename)
                to_path = os.path.join(junk,filename)
                now = datetime.datetime.now()
                then = datetime.datetime.fromtimestamp(os.path.getmtime(from_path))
                tdelta = now - then
                seconds = tdelta.total_seconds()
                if seconds > 7884000:
                    if from_path != to_path:
                        if os.stat(from_path).st_size < 100:
                            shutil.move(from_path,to_path)
                            f = open('log.txt','a')
                            f.write('\n')
                            f.write(from_path+' moved to '+to_path)
                            f.close()
                            counter += 1
                            print(f'Moved {from_path} to {to_path}')
                        else:
                            # print(f'skipped {from_path}')
                            pass
            except Exception as e:
                    print(f'Cannot move {from_path} reason: {e}')
        print(f'Moved {counter} amount of junk files')
        desk()

#Goes through all files and subdirs in desktop looking for files which fit the filter.
def desk():
    counter = 0
    print('Cleaning Desktop')
    home = os.path.expanduser('~/Desktop')
    junk = expanduser('~/Desktop/junk')
    for directory, _, filenames in os.walk(home):        
        for filename in filenames:
            try:
                from_path = os.path.join(directory,filename)
                to_path = os.path.join(junk,filename)
                now = datetime.datetime.now()
                then = datetime.datetime.fromtimestamp(os.path.getmtime(from_path))
                tdelta = now - then
                seconds = tdelta.total_seconds()
                if seconds > 7884000:
                    if os.stat(from_path).st_size < 100:
                        shutil.move(from_path,to_path)
                        f = open('log.txt','a') 
                        f.write('\n')
                        f.write(from_path+' moved to '+to_path)
                        f.close()
                        counter += 1
                        print(f'Moved {from_path} to {to_path}')
                    else:
                        # print(f'skipped {from_path}')
                        pass
            except Exception as e:
                    print(f'Cannot move {from_path} reason: {e}')
        print(f'Moved {counter} amount of junk files')
        down()

#Goes through all files and subdirs in downloads looking for files which fit the filter
def down():
    counter = 0
    print('Cleaning downloads')
    home = os.path.expanduser('~/Downloads')
    junk = expanduser('~/Desktop/junk')
    for directory, _, filenames in os.walk(home):        
        for filename in filenames:
            try:
                from_path = os.path.join(directory,filename)
                to_path = os.path.join(junk,filename)
                now = datetime.datetime.now()
                then = datetime.datetime.fromtimestamp(os.path.getmtime(from_path))
                tdelta = now - then
                seconds = tdelta.total_seconds()
                if seconds > 7884000:
                    if os.stat(from_path).st_size < 100:
                        shutil.move(from_path,to_path)
                        f = open('log.txt','a') 
                        f.write('\n')
                        f.write(from_path+' moved to '+to_path)
                        f.close()
                        counter += 1
                        print(f'Moved {from_path} to {to_path}')
                    else:
                        # print(f'skipped {from_path}')
                        pass
            except Exception as e:
                    print(f'Cannot move {from_path} reason: {e}')
        print(f'Moved {counter} amount of junk files')
        temp_it()

def temp_it():
    counter = 0
    temp = expanduser('~/Appdata/Local/Temp')
    print('Removing trash temp file')
    for directories,_ , filenames in os.walk(temp):
        for i in filenames:
            try:
                temporary = os.path.join(directories,i)
                if temporary.endswith('*.tmp'):
                    os.remove(temporary)
                    print('Removed {temporary}')
                    counter += 1
             except Exception as e:
                print(f'Could not remove {temporary} due to:{e}')
                pass
    print(f'Removed a total of {counter} temp files')
    junky()
    
def junky():
    choice = input('Enter if you want to [rollback] the process [search] for a file in the junk or [empty] the junk: ')
    if choice == 'search':
        search()
    elif choice == 'empty':
        empty()
    elif choice == 'rollback':
        rollback()
    else:
        print('Enter a valid choice')
        junky()
    

def search():
    junk = os.path.expanduser('~/Desktop/junk')
    searched = input('Enter the file you want to search for and remove out of junk: ')
    searched_up = os.path.join(junk,searched)
    if os.path.exists(searched_up):
        choice = input('What do you want to do with this file [move] [delete]: ')
        if choice == 'move':
            where = input('Where do you want to move it: ')
            shutil.move(searched_up,where)
            print(f'Your file {searched_up} has been moved to {where}')
            junky()
        else:
            print('invalid option')
            search()
    else:
        print('That file does not exist')
        juny()

def empty():
    junk = os.path.expanduser('~/Desktop/junk')
    print('Emptying the junk now')
    for directory, _, filename in os.walk(junk):
        for i in filename:
            try:
                joined = os.path.join(directory,i)
                os.remove(joined)
                print(f'Removed {joined}')
            except Exception as e:
                print(f'Could not delete {joined} due to: {e}')
                pass
        print('Finished')
        exit()
def rollback():
        try:
            log_file = open('log.txt','r')
            for line in log_file:
                    lined = line.strip()
                    paths = lined.split(' moved to ')
                    if len(paths) != 2:
                        continue
                    old = paths[0]
                    new = paths[1]
                    print(f'Reversing changes moving {new} to {old}')
                    shutil.move(new,old)
        except Exception as e:
            print(f'Could not move {new} to {old} due to: {e}')
            pass
        print('Wiped log')
        f = open('log.txt','w+')
        f.write('')
        f.close()
        junky()


admin_check()
