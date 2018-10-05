import shutil
import os

from xml.dom import minidom

#This scipt clears the desktop and relocates the files according to the name

#defines the path to desktop
desktopPath = os.path.join('C:\\', os.environ['HOMEPATH'], 'Desktop\\')

listOfEntities = []

#gets the list of all the files on the directory
for (dirpath, dirnames, filenames) in os.walk(desktopPath):
	listOfEntities.extend(filenames)
	break

#read the config file
config = minidom.parse('config.xml')

filetypes = config.getElementsByTagName('file')

#get the prefixes
for files in filetypes:
	prefix = files.attributes['prefix'].value

	for file in listOfEntities :
		#conditions according to the prefixes

		#compare the prefixes from the files and from config
		if file[:6] == prefix:
			shutil.move(desktopPath + file, files.firstChild.data + file)
			print ('moved ' + file)