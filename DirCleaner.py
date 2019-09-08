# Get the modules needed.
import os, shutil, time, glob, datetime, configparser, requests, argparse, sys
from os.path import expanduser
class Cleaner:
    def __init__(self):
        # configparser set up.
        config = configparser.ConfigParser()
        config.read("script.config")
        # Config variables.
        self.minperiod = config.get("MAIN", "minperiod")
        self.minsize = config.get("MAIN", "minsize")
        self.new_minsize = int(self.minsize)
        self.new_minperiod = int(self.minperiod)
        self.l = config.get("MAIN","wipelog")
        self.log = str(self.l)
        # Path variables.
        self.junk = os.path.expanduser('~/Desktop/junk')
        self.desktop = os.path.expanduser('~/Desktop')
        self.documents = os.path.expanduser('~/Documents')
        self.downloads = os.path.expanduser('~/Downloads')
        self.temp = os.path.expanduser('~/AppData/Local/Temp')
        self.listed = [self.documents,self.downloads,self.desktop]
        self.counter = 0
        self.scanned = 0
        self.create()
    
    def create(self):
        if os.path.exists(self.junk):
            self.arguments()
        else:
            os.mkdir(self.junk)
            self.arguments()
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
        parser.add_argument('--help',action="help",help='Help page.')
        args = parser.parse_args()
        if args.r:
            self.rollback()
        elif args.s:
            self.search()
        elif args.e:
            self.empty()
        elif args.c:
            self.cleaning()
        elif args.u:
            self.update_check()
        elif args.t:
            self.temp_it()
        elif args.j:
            self.junky()
        if len(sys.argv[0]) != 1:
            print('Do python DirCleaner.py --help to see the options.')

    def junky(self):
        if os.path.exists(self.junk):
            print('You already have a junk folder')
            exit()
        else:
            print('Making junk folder for you')
            os.mkdir(self.junk)
            exit()
    # Checks for updates by checking the Github repo.
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
                print('Most recent version installed. Cotinuing...')


    # Goes through all files and subdirs in Documents, Desktop and Downloads looking for files which fit the filter.
    def cleaning(self):
        print('Starting clean of documents, downloads and desktop...')
        time.sleep(5)
        print("Clean started. This could take up to two mins, depending on your computer's speed and the amount of files.")
        time.sleep(1)
        for i in range(0,3):
            for directory, _, filenames in os.walk(self.listed[i]):        
                for filename in filenames:
                    try:
                        from_path = os.path.join(directory,filename)
                        new_path = os.path.join(self.junk,filename)
                        self.scanned += 1
                        if os.stat(from_path).st_size < self.new_minsize and time.time() - os.path.getmtime(from_path) > (self.new_minperiod) and self.junk not in from_path:
                            shutil.move(from_path,self.junk)
                            self.counter += 1
                            f = open('log.txt','a')
                            f.write('\n')
                            f.write(from_path+' moved to '+new_path)
                            f.close()
                            print(f'Moved {from_path} to {self.junk}')
                        else:
                            #print(f'skipped {from_path}')
                            pass
                    except Exception as e:
                        print(f'Cannot move {from_path} reason: {e}')
                        pass
        print(f'Scanned: {self.scanned} Moved: {self.counter}')
        exit()

    # (only works on Windows) Checks temp folder for trash temp files.
    def temp_it(self):
        os.chdir(self.temp)
        print('Removing trash temp files...')
        for temp_file in glob.glob('*.tmp'):
            try:
                temporary = os.path.join(self.temp,temp_file)
                self.counter += 1
                os.remove(temp_file)
                print(f'Removed {temporary}.')
                self.counter += 1
            except Exception as e:
                print(f'Could not remove {temporary} due to: {e}')
                pass
        print(f'Total files removed: {self.counter}')
        exit()


    # Searches for files in the junk folder.
    def search(self):
        searched = input('Enter the file you want to search for: ')
        searched_up = os.path.join(self.junk,searched)
        if os.path.exists(searched_up):
            choice = input('What do you want to do with this file? [move] or [delete]: ')
            if choice == 'move':
                where = input('Where do you want to move it to?: ')
                shutil.move(searched_up,where)
                print(f'Your file {searched_up} has been moved to {where}.')
            else:
                print('Invalid option.')
                self.search()
        else:
            print('That file does not exist.')
            self.search()

    # Clears the junk.
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
        log_file = open('log.txt','r')
        for line in log_file:
            try:
                lined = line.strip()
                paths = lined.split(' moved to ')
                if len(paths) != 2:
                    continue
                old = paths[0]
                new = paths[1]
                newed = old.rsplit("\\", 1)[0]
                print(f'Reversing changes; moving {new} to {newed}.')
                shutil.move(new,newed)
            except Exception as e:
                print(f'Could not move {new} to {newed} due to: {e}')
                pass
        if self.log == 'True':
            t = open('log.txt','w+').close()
            print('Wiped log')
            exit()
        else:
            print('Not wiping log set to True to wipe log')
            exit()
if __name__ == '__main__':
    Cleaner()



