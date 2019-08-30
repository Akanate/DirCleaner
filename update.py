import os


def make_sure():
    print('Make sure to have git terminal installed before running this program')
    choice = input('Do you have git terminal y/n: ')
    if choice == 'y':
        update()
    elif choice == 'n':
        exit()
    else:
        print('Enter a valid choice')

def update():
    count = 0
    while count < 1:
        try:
            print('Starting update')
            cwd = os.getcwd()
            os.chdir(cwd)
            os.system('cd ..')
            os.remove('DirCleaner')
            os.system('git clone https://github.com/WHYSOEASY/DirCleaner')
            print('Finished update')
            count += 1
        except Exception as e:
            pass
make_sure()
    
