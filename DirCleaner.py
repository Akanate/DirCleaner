# Get the modules needed.
import os 
import shutil
import time 
import glob 
import datetime
import sys
import winshell
import configparser 
import requests 
import argparse 
import colorama
from win32com.shell import shell,shellcon
import os
from colorama import Fore, Back, Style
from colorama import init 
import art
from art import tprint
from os.path import expanduser
from datetime import datetime
init()
class Cleaner:
    def __init__(self):
        # configparser set up.
        config = configparser.ConfigParser()
        config.read("script.config")
        # Config variables.
        self.minperiod = config.get("MAIN", "minperiod")
        self.minsize = config.get("MAIN", "minsize")
        self.extra_dir = config.get("MAIN","external_paths")
        self.extra_paths = str(self.extra_dir)
        self.new_minsize = int(self.minsize)
        self.new_minperiod = int(self.minperiod)
        self.recycle_bin = os.path.expanduser("C:/$Recycle.bin")
        self.formats = ['.txt','.doc','.docx','.rtf']
        self.times_array = []
        self.check = 0
        # Path variables.
        self.junk = os.path.expanduser('~/Desktop/junk')
        self.desktop = os.path.expanduser('~/Desktop')
        self.documents = os.path.expanduser('~/Documents')
        self.downloads = os.path.expanduser('~/Downloads')
        self.temp = os.path.expanduser('~/AppData/Local/Temp')
        self.listed = [self.documents,self.downloads,self.desktop]
        self.counter = 0
        self.scanned = 0
        self.paths = []
        self.banner()

    def banner(self):
        tprint('DirCleaner')
        print(Fore.LIGHTMAGENTA_EX + 'Made by Akanate')
        self.create()
         
    def create(self):
        if os.path.exists(self.junk):
            self.arguments()
        else:
            self.check +=1
            self.junk = os.path.expanduser('~/Documents/Junk')
            if os.path.exists(self.junk):
                self.arguments()
            else:
                os.mkdir(self.junk)
                self.arguments()

    def extra_dirs(self):
        counter = 0
        if str(self.extra_dir) == "None":
            print(Fore.YELLOW + "Found No Extra Paths continuing....")
            self.cleaning()
        else:
            dict_ = list(str(self.extra_dir))
            if "," in dict_:
                splitted = self.extra_dir.split(',')
                if len(splitted) > 1:
                    for values in splitted:
                        if os.path.exists(values):
                            counter += 1
                            time.sleep(1)
                            print(Fore.GREEN + f'{values} is a valid path continuing....')
                            self.listed.append(values)
                        else:
                            time.sleep(0.5)
                            print(Fore.RED + f'{values} invalid path ignoring.....')
                    print(Fore.GREEN + f'Continuing with {counter} extra paths')
                    self.cleaning()
            else:
                try:
                    if os.path.exists(self.extra_dir):
                        print(Fore.GREEN + f"{self.extra_dir} is a valid path continuing")
                        time.sleep(1)
                        self.listed.append(str(self.extra_dirs))
                        print(Fore.GREEN + "Continuing with 1 extra dir")
                        self.cleaning()
                except Exception as e:
                    print(Fore.RED + f"{self.extra_dir} invalid path ignoring")
                    self.cleaning()

    # Argparser arguments.
    def arguments(self):
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument('-r',action='store_true',help='Rolls back the cleaning process.')
        parser.add_argument('-s',action='store_true',help='Allows you to search through the junk.')
        parser.add_argument('-e',action='store_true',help='Empties the junk.')
        parser.add_argument('-c',action='store_true',help='Cleans your computer.')
        parser.add_argument('-u',action='store_true',help='Checks for updates.')
        parser.add_argument('-t',action='store_true',help='Wipes temp files.')
        parser.add_argument('-j',action='store_true',help='This will make the junk file needed for the -c option')
        parser.add_argument('-restore',action='store_true',help='Emergency restore goes into recycling bin and restores the most recent deleted files by this program.')
        parser.add_argument('--help',action="help",help='Help page.')
        args = parser.parse_args()
        if args.r:
            self.rollback()
        elif args.s:
            self.search()
        elif args.e:
            self.empty()
        elif args.c:
            self.extra_dirs()
        elif args.u:
            self.update_check()
        elif args.t:
            self.temp_it()
        elif args.j:
            self.junky()
        elif args.restore:
            self.restore()
        if len(sys.argv[0]) != 1:
            print('Do python DirCleaner.py --help to see the options.')

    def junky(self):
        if os.path.exists(self.junk):
            print(Fore.GREEN + 'You already have a junk folder')
            exit()
        else:
            print(Fore.YELLOW + 'Making junk folder for you')
            os.mkdir(self.junk)
            exit()

    # Checks for updates by checking the Github repo.
    def update_check(self):
        print(Fore.YELLOW + 'Checking for updates...')
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
                print(Fore.YELLOW + 'New update available!!!')
                print(f'{newer_contents}')
            else:
                print(Fore.GREEN + 'Most recent version installed. Continuing...')


    # Goes through all files and subdirs in Documents, Desktop and Downloads looking for files which fit the filter.
    def cleaning(self):
        if self.check == 1:
            junked = os.path.expanduser('~/Documents/Junk')
        else:
            junked = os.path.expanduser('~/Desktop/Junk')
        print(Fore.YELLOW + 'Starting analysis of documents, downloads and desktop...')
        time.sleep(5)
        print(Fore.GREEN + "Analysis started. This could take up to two mins, depending on your computer's speed and the amount of files.")
        time.sleep(1)
        for i in range(0,len(self.listed)):
            for directory, _, filenames in os.walk(self.listed[i]):   
                for filename in filenames:
                    try:
                        from_path = os.path.join(directory,filename)
                        new_path = os.path.join(junked,filename)
                        self.scanned += 1
                        if int(os.stat(from_path).st_size) < self.new_minsize and self.new_minperiod < time.time() - os.path.getmtime(from_path):
                            from_path.replace('\\','/')
                            g = from_path.split('\\')
                            if from_path.lower().endswith(('.txt','.rtf','.doc','.docx')):
                                if os.stat(from_path).st_size < 100:
                                    continue
                                if "Junk" in g:
                                    continue
                                self.paths.append(from_path)
                                f = open('log.txt','a')
                                a = open('restore.txt','a')
                                f.write('\n')
                                f.write(from_path+' moved to '+new_path)
                                a.write('\n')
                                a.write(new_path+','+from_path)
                                a.close()
                                f.close()
                                self.counter += 1
                                print(Fore.GREEN + (f'Found files which could be junk {from_path}'))
                        else:
                            #print(Fore.RED + f'skipped {from_path} size:{os.stat(from_path).st_size} age:{time.time() - os.path.getmtime(from_path)}')
                            pass
                    except Exception as e:
                        print(Fore.RED + (f'Cannot move {from_path} reason: {e}'))
                        pass
        print(Fore.YELLOW +(f'Scanned: {self.scanned} found file which could be junk {self.counter}'))
        self.move()

    def move(self):
        try:
            if len(self.paths) != 0:
                os.system('cls')
                counter = 0
                for i in self.paths:
                    counter += 1
                    print(Fore.YELLOW + (f'{counter}: {i}'))
                n = input('Enter the number which you want to not move if you do not want to remove anything and start moving the files to junk then type START if not type exit: ')
                if n == 'START':
                    choice = input(f'Are you sure you want to move {self.counter} files to junk? Y/N')
                    if choice == "Y":
                        self.move_dirs()
                    else:
                        print(Fore.YELLOW + "EXITING!!!")
                elif n == 'exit':
                    print(Fore.YELLOW + "EXITING!!!")
                    exit()
                else:
                    g = self.paths[int(n) - 1]
                    self.paths.remove(g)
                    self.move()
            else:
                print(Fore.RED + 'We could not find any files which were junk')
        except ValueError as e:
            print(Fore.RED + 'You cannot enter a word instead of a number')
            self.move()
    def move_dirs(self):
        count = 0
        print(Fore.YELLOW + 'Moving files to junk now')
        for dirs in self.paths:
            try:
                shutil.move(dirs,self.junk)
                print(Fore.GREEN + (f'Moved {dirs} to {self.junk}'))
                count += 1
            except Exception as e:
                print(Fore.RED + (f'Couldnt move {dirs} due to: {e}'))
                pass
        print(Fore.YELLOW + (f'Finished moving {count} files to {self.junk}'))

    # (only works on Windows) Checks temp folder for trash temp files.
    def temp_it(self):
        os.chdir(self.temp)
        print(Fore.YELLOW + 'Removing trash temp files...')
        for temp_file in glob.glob('*.tmp'):
            try:
                temporary = os.path.join(self.temp,temp_file)
                os.remove(temp_file)
                print(Fore.GREEN + (f'Removed {temporary}.'))
                self.counter += 1
            except Exception as e:
                print(Fore.RED + (f'Could not remove {temporary} due to: {e}'))
                pass
        print(Fore.YELLOW + (f'Total files removed: {self.counter}'))
        exit()


    # Searches for files in the junk folder.
    def search(self):
        print(Fore.YELLOW + 'Enter the file you want to search for: ',end='')
        searched = input()
        searched_up = os.path.join(self.junk,searched)
        if os.path.exists(searched_up):
            print(Fore.YELLOW +'What do you want to do with this file? [move] or [delete]: ',end='')
            choice = input()
            if choice == 'move':
                where = input(Fore.YELLOW + 'Where do you want to move it to?: ')
                shutil.move(searched_up,where)
                print(Fore.GREEN + (f'Your file {searched_up} has been moved to {where}.'))
            else:
                print(Fore.RED + 'Invalid option.')
                self.search()
        else:
            print(Fore.RED + 'That file does not exist.')
            self.search()

    # Clears the junk.
    def empty(self):
        if self.check > 0:
            junk1 = os.path.expanduser('~/Documents/Junk')
        else:
            junk1 = os.path.expanduser('~/Desktop/Junk')
        print(Fore.GREEN +'Emptying the junk folder...')
        for directory, _, filename in os.walk(junk1):
            for i in filename:
                try:
                    joined = os.path.join(directory,i)
                    self.recycle(joined)
                    print(Fore.GREEN + (f'Removed {joined}.'))
                except Exception as e:
                    print(Fore.RED + (f'Could not delete {joined}'))
                    pass
        print(Fore.GREEN + 'Finished.')
        g = open('log.txt','w+').close()
        exit()

    #Reverses changes made by the program.
    def check_rollback(self):
        t = open('log.txt','r')
        contents = t.read()
        if contents == "":
            return 1
        else:
            return
    def rollback(self):
        log_file = open('log.txt','r')
        print(Fore.YELLOW + 'Checking rollback file.....')
        value = self.check_rollback()
        if value == 1:
            print(Fore.RED + 'Rollback file is empty cancelling rollback....')
            return
        print(Fore.GREEN + 'Starting rollback process....')
        for line in log_file:
            try:
                lined = line.strip()
                paths = lined.split(' moved to ')
                if len(paths) != 2:
                    continue
                old = paths[0]
                new = paths[1]
                newed = old.rsplit("\\", 1)[0]
                print(Fore.GREEN + (f'Reversing changes; moving {new} to {newed}.'))
                shutil.move(new,newed)
            except Exception as e:
                print(Fore.GREEN + (f'Could not move {new} to {newed} due to: {e}'))
                pass
        g = open('log.txt','w+')
        g.truncate()

    def backup(self):
        restore_file = open("restore.txt",'r')
        contents = restore_file.read()
        file_name = "restore_backup" + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.txt'
        with open(file_name,'a') as backup_file:
            print(Fore.YELLOW + f'Backup file created {file_name} use this to restore files if loss of power etc copy this into the restore.txt file.')
            backup_file.write(contents)

    def restore(self):
        restore_file = open("restore.txt",'r')
        self.backup()
        for files in restore_file:
            try:
                splitted = files.split(',')
                new_file = splitted[0]
                if len(splitted) != 2:
                    continue
                filed = new_file.rstrip('\n')
                filepath = os.path.abspath(filed)
                new_file1 = splitted[1]
                filed2 = new_file1.rstrip('\n')
                new_filepath = os.path.abspath(filed2)
                winshell.undelete(filepath)
                print(Fore.GREEN + f'Restored file > {filed}')
                shutil.move(filepath,new_filepath)
                print(Fore.MAGENTA + f'Moving back to original position {splitted[1]}')
            except Exception as e:
                print(Fore.RED + f"Failed to restore file {filed}")
        open("restore.txt",'w+').close()
    
    def recycle(self,filename):
        try:
            if not os.path.exists(filename):
                return True
            res= shell.SHFileOperation((0,shellcon.FO_DELETE,filename,None, shellcon.FOF_SILENT | shellcon.FOF_ALLOWUNDO | shellcon.FOF_NOCONFIRMATION,None,None))
            if not res[1]:
                os.remove(filename)
        except Exception as e:
            pass
            

if __name__ == '__main__':
    Cleaner()
