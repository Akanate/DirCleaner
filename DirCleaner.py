# Get the modules needed.
import os, shutil, time, glob, ctypes, datetime, configparser, requests
from os.path import expanduser
class Cleaner:
    def __init__(self):
        # configparser set up.
        config = configparser.ConfigParser()
        config.read("script.config")

        #Config variables.
        self.minperiod = config.get("MAIN", "minperiod")
        self.minsize = config.get("MAIN", "minsize")
        self.checkadmin = config.get("MAIN", "checkadmin")
        self.new_minsize = int(self.minsize)
        self.new_minperiod = int(self.minperiod)
        #Path Variables
        self.junk = os.path.expanduser('~/Desktop/junk')
        self.desktop = os.path.expanduser('~/Desktop')
        self.documents = os.path.expanduser('~/Documents')
        self.downloads = os.path.expanduser('~/Downloads')
        self.temp = os.path.expanduser('~/Appdate/Local/Temp')
        self.listed = [self.documents,self.downloads,self.desktop]
        self.counter = 0
        self.scanned = 0
        self.update_check()

    # Checks for an update
    def update_check(self):
        print('Checking for updates...')
        contents = requests.get('https://raw.githubusercontent.com/WHYSOEASY/DirCleaner/master/info.txt')
        contented = contents.content
        new_contents = contented.decode()
        newer_contents1 = new_contents.strip()
        g = open('new_info.txt','a')
        g.write(newer_contents1)
        g.close()
        t = open('new_info.txt','r')
        newer_contents = t.read().strip() 
        t.close()
        os.remove('new_info.txt')
        with open('info.txt','r') as f:
            contents = f.read().strip()
            if contents != newer_contents:
                print('New update available applying update')
                print(f'{newer_contents}')
                check = expanduser('~/Appdata/Local/Temp')
                if os.path.exists(check):
                    print('Windows detected you need to run update.py')
                    exit()
                else:
                    print('Other os detected you need to run update.sh')
                    exit()
            else:
                print('Most recent version continuing')
                self.admin_check()
    #Checks if athe user is an admin
    def admin_check(self):
        if self.checkadmin == 'True':
            print('Checking this program is not running as admin...')
            try:
                is_admin = os.getuid() == 0
            except AttributeError:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == 'True':
                    print('You need to run this program without admin privileges. This is to prevent data loss.')
                    exit()
                else:
                    print("You're all clear. Continuing...")
                    self.precheck()
        else:
            print("Skipping admin check...")
            self.precheck()

    # Checks if you have a junk folder/creates one if none exists.
    def precheck(self):
        print('Checking for junk folder...')
        if os.path.exists(self.junk):
            print('Junk folder already exists. Continuing...')
            self.cleaning()
        else:
            print("Junk folder doesn't exist. Creating the folder...")
            os.mkdir(self.junk)
            print('Created junk folder. Continuing...')
            self.cleaning()

    # Goes through all files and subdirs in Documents, Desktop and downloads looking for files which fit the filter
    def cleaning(self):
        print('Starting cleaning of documents, downloads and desktop...')
        for i in range(0,3):
            for directories in self.listed:
                for directory, _, filenames in os.walk(self.listed[i]):        
                    for filename in filenames:
                        try:
                            from_path = os.path.join(directory,filename)
                            to_path = os.path.join(self.junk,filename)
                            self.scanned += 1
                            if os.stat(from_path).st_size < self.new_minsize and time.time() - os.path.getmtime(from_path) > (self.new_minperiod) and self.junk not in from_path:
                                shutil.move(from_path,to_path)
                                self.counter += 1
                                print(f'Moved {from_path} to {to_path}')
                            else:
                                #print(f'skipped {from_path}')
                                pass
                        except Exception as e:
                            print(f'Cannot move {from_path} reason: {e}')
                            pass
        self.temp_it()

    #Only works on windows checks temp folder looking for trash temp files.
    def temp_it(self):
        print('Removing trash temp files...')
        for directories,_ , filenames in os.walk(self.temp):
            for i in filenames:
                try:
                    temporary = os.path.join(directories,i)
                    self.scanned += 1
                    if temporary.endswith('*.tmp'):
                        os.remove(temporary)
                        print('Removed {temporary}.')
                        self.counter += 1
                except Exception as e:
                    print(f'Could not remove {temporary} due to:{e}')
                    pass
        print(f'Total files moved not accurate as errors could have been encountered {self.counter} and total files scanned {self.scanned}')
        self.confirm()

    #Choose your options
    def confirm(self):
        choice = input('Enter if you want to: [rollback] the process, [search] for a file in the junk folder or [empty] the junk folder: ')
        if choice == 'search':
            self.search()
        elif choice == 'empty':
            self.empty()
        elif choice == 'rollback':
            self.rollback()
        else:
            print('Enter a valid choice.')
            self.confirm()

    #Searches for files in junk folder
    def search(self):
        searched = input('Enter the file you want to search for: ')
        searched_up = os.path.join(self.junk,searched)
        if os.path.exists(searched_up):
            choice = input('What do you want to do with this file? [move] or [delete]: ')
            if choice == 'move':
                where = input('Where do you want to move it to?: ')
                shutil.move(searched_up,where)
                print(f'Your file {searched_up} has been moved to {where}.')
                self.confirm()
            else:
                print('Invalid option.')
                self.search()
        else:
            print('That file does not exist.')
            self.confirm()

    #Clears the junk
    def empty(self):
        print('Emptying the junk folder...')
        for directory, _, filename in os.walk(self.junk):
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
    def rollback(self):
        try:
            log_file = open('log.txt','r+')
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
        log_file.truncate()

Cleaner()


