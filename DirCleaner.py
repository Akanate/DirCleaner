# Get the modules needed.
import os, shutil, time, glob, ctypes, datetime, configparser, requests
from os.path import expanduser

# configparser set up.
config = configparser.ConfigParser()
config.read("script.config")

#Config variables.
minperiod = config.get("MAIN", "minperiod")
minsize = config.get("MAIN", "minsize")
checkadmin = config.get("MAIN", "checkadmin")
new_minsize = int(minsize)
new_minperiod = int(minperiod)

# Checks for an update
def update_check():
    print('Checking for updates...')
    contents = requests.get('https://raw.githubusercontent.com/WHYSOEASY/DirCleaner/master/info.txt')
    contented = contents.content
    new_contents = contented.decode()
    newer_contents = new_contents.strip()
    print(newer_contents)
    with open('info.txt','r') as f:
        if f != newer_contents:
            print('New update available applying update')
            check = expanduser('~/Appdata/Local/Temp')
            if os.path.exists(check):
                print('Windows detected you need to run update.py')
                exit()
            else:
                print('Other os detected you need to run update.sh')
                exit()
        else:
            print('Most recent version continuing')
            admin_check()
#Checks if the user is an admin
def admin_check():
    if checkadmin == True:
        print('Checking this program is not running as admin...')
        try:
           is_admin = os.getuid() == 0
        except AttributeError:
           is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
           if is_admin == True:
               print('You need to run this program without admin privileges. This is to prevent data loss.')
               exit()
           else:
               print("You're all clear. Continuing...")
               precheck()
    else:
        print("Skipping admin check...")
        precheck()

# Checks if you have a junk folder/creates one if none exists.
def precheck():
    print('Checking for junk folder...')
    junk = expanduser('~/Desktop/junk')
    if os.path.exists(junk):
        print('Junk folder already exists. Continuing...')
        doc()
    else:
        print("Junk folder doesn't exist. Creating the folder...")
        os.mkdir(junk)
        print('Created junk folder. Continuing...')
        doc()

# Goes through all files and subdirs in Documents looking for files which fit the filter
def doc():
    counter = 0
    print('Cleaning Documents folder...')
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
                if seconds > new_minperiod:
                    if from_path != to_path:
                        if os.stat(from_path).st_size < new_minsize:
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

# Goes through all files and subdirs in the Desktop folder, looking for files which fit the filter.
def desk():
    counter = 0
    print('Cleaning Desktop folder...')
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
                if seconds > new_minperiod:
                    if os.stat(from_path).st_size < new_minsize:
                        shutil.move(from_path,to_path)
                        f = open('log.txt','a') 
                        f.write('\n')
                        f.write(from_path+' moved to '+to_path)
                        f.close()
                        counter += 1
                        print(f'Moved {from_path} to {to_path}.')
                    else:
                        # print(f'skipped {from_path}')
                        pass
            except Exception as e:
                    print(f'Cannot move {from_path}. Reason: {e}')
        print(f'Moved {counter} amount of junk files.')
        down()

# Goes through all files and subdirs in the Downloads folder, looking for files which fit the filter.
def down():
    counter = 0
    print('Cleaning Downloads...')
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
                if seconds > new_minperiod:
                    if os.stat(from_path).st_size < new_minsize:
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
                    print(f'Cannot move {from_path}. Reason: {e}')
        print(f'Moved {counter} amount of junk files.')
        temp_it()
#Only works on windows checks temp folder looking for trash temp files.
def temp_it():
    counter = 0
    temp = expanduser('~/Appdata/Local/Temp')
    print('Removing trash temp files...')
    for directories,_ , filenames in os.walk(temp):
        for i in filenames:
            try:
                temporary = os.path.join(directories,i)
                if temporary.endswith('*.tmp'):
                    os.remove(temporary)
                    print('Removed {temporary}.')
                    counter += 1
            except Exception as e:
                print(f'Could not remove {temporary} due to:{e}')
                pass
    print(f'Removed a total of {counter} temp files.')
    confirm()

#Choose your options
def confirm():
    choice = input('Enter if you want to: [rollback] the process, [search] for a file in the junk folder or [empty] the junk folder: ')
    if choice == 'search':
        search()
    elif choice == 'empty':
        empty()
    elif choice == 'rollback':
        rollback()
    else:
        print('Enter a valid choice.')
        confirm()
#Searches for files in junk folder
def search():
    junk = os.path.expanduser('~/Desktop/junk')
    searched = input('Enter the file you want to search for: ')
    searched_up = os.path.join(junk,searched)
    if os.path.exists(searched_up):
        choice = input('What do you want to do with this file? [move] or [delete]: ')
        if choice == 'move':
            where = input('Where do you want to move it to?: ')
            shutil.move(searched_up,where)
            print(f'Your file {searched_up} has been moved to {where}.')
            confirm()
        else:
            print('Invalid option.')
            search()
    else:
        print('That file does not exist.')
        confirm()
#Clears the junk
def empty():
    junk = os.path.expanduser('~/Desktop/junk')
    print('Emptying the junk folder...')
    for directory, _, filename in os.walk(junk):
        for i in filename:
            try:
                joined = os.path.join(directory,i)
                os.remove(joined)
                print(f'Removed {joined}.')
            except Exception as e:
                print(f'Could not delete {joined} due to: {e}')
                pass
        print('Finished.')
        exit()
#Reverses changes made by the program.
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
                    print(f'Reversing changes; moving {new} to {old}.')
                    shutil.move(new,old)
        except Exception as e:
            print(f'Could not move {new} to {old} due to: {e}')
            pass
        print('Wiped log')
        f = open('log.txt','w+')
        f.write('')
        f.close()
        confirm()


update_check()
