import shutil

from os import walk

#This scipt clears the desktop and relocates the files according to the name

#defines the path
desktopPath = 'C:\\Users\\visheshn\\Desktop'

listOfEntities = []

#gets the list of all the files on the directory
for (dirpath, dirnames, filenames) in walk(desktopPath):
	listOfEntities.extend(filenames)
	break

for file in listOfEntities :
	#conditions according to the prefixes
	#DBScript for training
	if file[6:] == 'DBS_T_':
		pass