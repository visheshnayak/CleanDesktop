import shutil
import os
import logging
import datetime
import sys

from xml.dom import minidom

#This scipt clears the desktop and relocates the files according to the name

try:
	#sets the logging component
	logging.basicConfig(filename='App.log', level=logging.DEBUG)
	logging.info('Started the CleanDesktop script at ' + str(datetime.datetime.time(datetime.datetime.now())))

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
			try:
				#compare the prefixes from the files and from config
				if file[:6] == prefix:
					shutil.move(desktopPath + file, files.firstChild.data + file)
					logging.info('Moved ' + file)
			except PermissionError as pe:
				logging.info('Exception occurred at ' + str(datetime.datetime.time(datetime.datetime.now())) + ' : The file is open in some other application. Hence, couldn\'t be moved')
			except:
				logging.info('Exception occurred at ' + str(datetime.datetime.time(datetime.datetime.now())) + ' : ' +  sys.exc_info()[0])



except:
	print(sys.exc_info()[0])