# DirCleaner
## Disclaimer
This program moves files around; use it at your own risk. I have implemented features which should stop data loss, but if it does, I am not responsible. This program is still in beta.
## Features
This program has a filter which stops any files which are younger than 3 months from being moved.


This program also prevents you from running it as an admin.


This program also has a rollback system, so if you think "oh no, it has moved a lot of files I dont want it to move", let it finish, then you will be prompted with a text bar saying the following: "Do you want to [search], [empty] or [rollback]?" Proceed to type in rollback. This will move all the files which were moved back to their original place.


This program also only moves files which are under 100 bytes in size.


You will notice I said move. That's because the files are not instantly deleted, and instead moved to a junk folder.
### How to use
First of all, use git clone or download the ZIP from <https://github.com/WHYSOEASY/DirCleaner.git>.
<img src="/assetsgit clone.png" alt="Git clone image">

<img src="/assets/git clone 2.png" alt="Git clone two">
Then cd  into the DirCleaner directory
<img src="/assets/cd.jpg" alt="cd">
Then proceed to launch DirCleaner.py.
<img src="/assets/start_program.png" alt="Starting the progran">
Then after it has cleaned up your files, you will be prompted with this.
<img src="/assets/executing_program.png" alt="Executing program">
Search will allow you to search for a file in the junk and move or delete it.
<img src="/assets/search.png" alt="searching">
Empty will delete all the files in the junk for you.
<img src="/assets/155ED3CE-19D4-4E96-99D1-3759E444483C.png" alt="empty">
And rollback will look inside the log file and reverse the changes, putting all the files back to where they were.
<img src="/assets/rollback.png" alt="rollback">


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
