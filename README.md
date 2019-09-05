# DirCleaner
## Disclaimer
This program moves files around; use it at your own risk. I have implemented features which should stop data loss, but if it does, I am not responsible. This program is still in beta.
## Requirements
- Python3
- Windows or Linux pc
## Features
This program has a filter which stops any files which are younger than 3 months from being moved.


This program also prevents you from running it as an admin.


This program also has a rollback system, so if you think "oh no, it has moved a lot of files I dont want it to move", let it finish, then you will be prompted with a text bar saying the following: "Do you want to [search], [empty] or [rollback]?" Proceed to type in rollback. This will move all the files which were moved back to their original place.


This program also only moves files which are under 100 bytes in size.


You will notice I said move. That's because the files are not instantly deleted, and instead moved to a junk folder.
### How to use
First of all, use git clone or download the ZIP from <https://github.com/WHYSOEASY/DirCleaner.git>.
<img src="/assets/git_clone.png" alt="Git clone image">

<img src="/assets/git clone 2.png" alt="Git clone two">
Then cd  into the DirCleaner directory
<img src="/assets/help_simple.png" alt="cd">
Then proceed to do python DirCleaner.py --help this will bring up a help menu.
<img src="/assets/help.png" alt="Starting the progran">
Then you will be given some options to use as command line arguments
<img src="/assets/clean.png" alt="Executing program">
The -c option will clean your computer.
<img src="/assets/rollback.png" alt="searching">
The -r option or the rollback feature will allow you to undo all the changes made.
<img src="/assets/empty1.png" alt="empty">
The -e option or empty will empty the junk for you deleting everything in it.
<img src="/assets/temp.png" alt="temp">
The -t option or temp deleter removes all temp files of non importance.
<img src="/assets/search.png" alt='search'>
The -s option or the search option allows you to search for a singular item in the junk and move or delete it.
<img src="/assets/update.png" alt="update">
The -u option or update option checks for updates.
### Reporting bugs
Make a new issue in the repo.
### What not to touch
DO NOT by any circumstance touch the log files these are used in the rollback feature.
### Updating
Just run update.py to get the latest version on Windows. Run update.sh if you are on Linux/any other Unix-based OS.
### How does it work?
- The program goes through all the directories and subdirectories in Documents, Desktop and Downloads, looking for files which are over the minimum age set in `script.config` and are lower than the maximum size set in `script.config`. If it finds any, it moves them to the junk folder where they are stored until you decide if you want to empty the junk folder, rollback the process or search inside the junk to move some files out.
### Extra config
- If you want to change the configuration of what files are classed as junk. Go to `script.config` and change the config for it
but be wary the configuration for the age of the files is in seconds so if you want to change it you need to put it in seconds by default it is set 3 months to stop the risk of moving important files and set too a 100 bytes.
### Make sure to rate!
- Like this? Please star this project to show your support :)
### Update log
- Make sure to consistently run update.py/.sh (depending on your OS).

##### 0.1.1
- Fixed an error where function `junky` was spelt wrong on the move part of the search option.
##### 0.2.0
- Lots of changes including grammar fixes and config changes to the program have been made by @Rexogamer.
##### 0.2.1
- You can now disable the admin check in `script.config`.
##### 0.2.2
- Fixed indentation and syntax errors that were made in the previous update on accident by RexoGamer
##### 0.2.3
- Massive amount of bug fixes due to the fact that the config parser uses strings not integers and lots of indentation errors all fixed.
##### 0.2.4
- Update checkup added
##### 0.2.5
- Fixed loads of bugs with update checkup and stopped admin checkup from skipping even if it was true
##### 1.00
- Fixed a massive big which would make it so then it would not go through sub directories at all. 
##### 1.0.1
- Minor changes
##### 1.0.2
- Complete code cleanup for optimisation.
##### 1.0.3
- Minor code fixes
##### 1.0.4
- Fixed rollback feature
##### 2.00
- Arguments added
