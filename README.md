# DirCleaner
#Background#
>This is a project which I made myself over the course of three days.
#Features#
-This program has a filter which stops any files which are under three months from being moved.
-This program also stops you from running the program as admin
-This program also has a rollback system which if you think oh no it has moved a lot of files I dont want it too move let it finish then you will be promped with a text bar saying the following do you want to [search] or [empty] or [rollback] proceed to type in rollback this will move all the files which were moved, back to their original place.
-This program also only moves files which are under a 100 bytes.
-You will notice I said move thats because the files are not instantly deleted and instead moved to a junk folder.
#How to use#
-First of all git clone or download zip for https://github.com/WHYSOEASY/DirCleaner.git
-Then proceed to launch DirCleaner.py
-It will start scanning your Desktop, Documents and downloads for files which may fit the filter I mentioned above it finds some it will move them to a junk folder on your desktop do not touch this folder as the program will give you a prompt after cleaning. It will say the following Enter if you want to [rollback] the process [search] for a file in the junk or [empty] the junk rollback will put all the files back into their original places. Search will allow you to search for a file in the junk which you may want to move out seperately and empty will delete everything in junk folder.
#Reporting bugs#
-Just put it in the issue part of the repo.
#What not to touch
-DO NOT by any circumstance touch the log files these are used in the rollback feature.
#Updating
-Just run the update.py to get the latest version.
