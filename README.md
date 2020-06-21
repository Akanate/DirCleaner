# DirCleaner
## Disclaimer
This program moves files around; use it at your own risk. I have implemented features which should stop data loss, but if it does, I am not responsible. This program is still in beta.
## Requirements
- Python3
- Windows only
### How to use
First of all, use git clone or download the ZIP from <https://github.com/WHYSOEASY/DirCleaner.git>.
<img src="/assets/git_clone.png" alt="Git clone image">

<img src="/assets/git clone 2.png" alt="Git clone two">
Now after you have done that change dircetory into DirCleaner.

Next do python DirCleaner.py --help


<img src="/assets/--help_name.jpg" alt="Help1">


Then after hitting enter you will be greeted by this screen.


<img src="/assets/--help.jpg" alt="help2">


Now these are all of the options which you can use with the cleaner.

The way to clean your computer is the option -c


<img src="/assets/clean_name.jpg" alt="clean">


Then hit enter and it will proceed to clean your computer.


<img src="/assets/clean_info.jpg" alt="cleaning">


The next feature is the -t feature this gets rid of all of your current temporary files.


<img src="/assets/temp_name.jpg" alt="temp0">


Then click enter and it will start to delete the temporary files.


<img src="/assets/temp_info.jpg" alt="temp1">


Now one of the most brilliant features the rollback feature.

If you feel that the cleaner has moved files you didnt want moving simply cancel the clean control c.

Then do python DirCleaner.py -r and it will rollback the process.


<img src="/assets/rollback_new.jpg" alt="roll">


Then click enter and it will proceed to move all the files back to their original places.


<img src="/assets/rollback_info.jpg" alt="roll1">


Now the -u feature this will check for updates and if there is one it will tell you.


<img src="/assets/update_name.jpg" alt="update">


Then click enter.


<img src="/assets/update_info.jpg" alt="update1">


Next feature is the search feature you can search in the junk for a file which you may want to delete or move seprately.


<img src="/assets/search_name.jpg" alt="searched">


Then type in what you want to search and click enter.


<img src="/assets/search_info.jpg" alt="searched1">


Thats it on how to use the features :)
### Reporting bugs
Make a new issue in the repo.
### What not to touch
DO NOT, under any circumstances, touch the log files; these are used in the rollback feature.
### Updating
Just run update.py to get the latest version on Windows.
### How does it work?
- The program goes through all the directories and subdirectories in Documents, Desktop and Downloads, looking for files which are over the minimum age set in `script.config` and are lower than the maximum size set in `script.config`. If it finds any, it moves them to the junk folder where they are stored until you decide if you want to empty the junk folder, rollback the process or search inside the junk to move some files out.
### Extra config
- If you want to change the configuration of what files are classed as junk, go to `script.config` and change the config for it.
But be wary, the configuration for the age of the files is in seconds so if you want to change it you need to put it in seconds. By default it is set 3 months to stop the risk of moving important files and set to 100 bytes.
### Make sure to rate!
- Like this? Please star this project to show your support :)
### Update log
- Make sure to consistently run update.py 

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
- Fixed loads of bugs with update checkup and stopped admin checkup from skipping even if it was true.
##### 1.0.0
- Fixed a massive bug which would make it so it wouldn't go through sub-directories at all. 
##### 1.0.1
- Minor changes.
##### 1.0.2
- Complete code cleanup for optimisation.
##### 1.0.3
- Minor code fixes.
##### 1.0.4
- Fixed rollback feature.
##### 2.0.0
- Arguments added.
- Admin check removed.
- Grammar fixes.
##### 2.0.1
- Code additions including -j for making junk folder needed for -c.
##### 2.0.2
- Rollback fixed
- Wipe log can be turned off and on
- Code cleanup
##### 3.0.0 
- Linux Compatibility removed
##### 3.0.1 
- Colours added
- Banner added
- README.md updated
##### 3.0.2 
- No longer moves files straight allows the user to choose which files they dont want to move before continuing.
##### 3.0.3
- Fixed bug where you could not click enter to move the files after removing some of the files you dont want moving.
##### 3.0.5
- Code cleanup made it so then if no files are found for junk it will exit.
##### 3.0.6
- Simple change of the word clean to analysis when searching for files which class as junk.
##### 4.0.0
- A change which completely fixed the cleaner check it out now it works lol.
##### 4.0.1
- Made it so if it cant find a desktop folder it will fallback to a documents folder instead.
- Fixed a few bugs.
