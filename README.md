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


The newest feature out of the bunch the -restore feature this is a very important feature and is used for emergency circumstances such as you deleted loads of files you didnt mean too. The reset feature will get all the most recent files you deleted using this program and use recycle bin to try to restore and move them back. And it will also make a backup for you so if you cancel halfway through you can go into the backup file and copy paste it into the restore .txt and run the command. And it will restore that backup if possible.

<img src="/assets/Capture.PNG" alt="Capture">


Thats it on how to use the features :)
### Reporting bugs
Make a new issue in the repo.
### What not to touch
DO NOT, under any circumstances, touch the log files/restore files; these are used in the rollback/restore features.
### Updating
Just run update.py to get the latest version on Windows.
### How does it work?
- The program goes through all the directories and subdirectories in Documents, Desktop and Downloads, looking for files which are over the minimum age set in `script.config` and are lower than the maximum size set in `script.config`. If it finds any, it moves them to the junk folder where they are stored until you decide if you want to empty the junk folder, rollback the process or search inside the junk to move some files out.
### Extra config
- If you want to change the configuration of what files are classed as junk, go to `script.config` and change the config for it.
But be wary, the configuration for the age of the files is in seconds so if you want to change it you need to put it in seconds. By default it is set 3 months to stop the risk of moving important files and set to 200 bytes. It also has an external_paths option in it if you put a path/paths in here(if multiple seperate them by comma) then it will search through them as well as the default ones be wary though if system files are on that path, it may mistake them for junk. So make sure if it finds any "junk" you check thoroughly that it isnt anything key to a game or to the system. 
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
- Made it so that it wont check junk folder for junk files anymore.
- The -u function will now update instead of you having to do it manually.
##### 4.0.2
- Had to get rid of -u being able to update the file as it didnt work due to the file itself being deleted by the update. It will now just check for updates.
##### 5.0.0 
- Added new feature where you can add multiple new paths to search in external_paths in script.config seperated by commas or putting on own.
- Due to this new feature there is more chance of people accidently moving system files so to counter this the files have to be above 100 bytes now.
- Now before moving files to junk, you have to triple check before doing it with two inputs to check. This will lower the chances of people moving system files etc as they will be able to look first and check and remove the files they want. 
##### 5.0.1
- It will no longer try to rollback if you have already rolled back.
##### 5.0.2
- Fixed the timestamps will definately get files over three months now.
- Made it so the program now only detects certain file extensions to stop the risk of someone deleting something really important.
- You can no longer search for files below 100 bytes.
- Restore feature added even after deletion of files you can restore them now and get them moved back to their original postion.
With the restore feature you also get a backup file made with it which you can copy paste into restore.txt and run python DirCleaner.py -reset and it will try to restore them and move them back if it is still valid.
##### 5.0.3
- "-reset" has now been changed to "-restore".
##### 5.0.4
- Fixed mistype which stopped you being able to use 1 external path on its own.
- Fixed the -u as it wasnt working due to update of username.
