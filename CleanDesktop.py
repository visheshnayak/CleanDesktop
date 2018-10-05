import shutil

from os import walk

#This scipt clears the desktop and relocates the files according to the name

#defines the path
desktopPath = 'C:\\Users\\visheshn\\Desktop\\'

listOfEntities = []

#gets the list of all the files on the directory
for (dirpath, dirnames, filenames) in walk(desktopPath):
	listOfEntities.extend(filenames)
	break

for file in listOfEntities :
	#conditions according to the prefixes

	#DBScript for work
	if file[:6] == 'DBS_W_':
		shutil.move(desktopPath + file, 'D:\\Vishesh\\Work\\DB\\Scripts\\' + file)
		print ('Moved ' + file)
	
	#Document for work
	elif file[:6] == 'DOC_W_':
		shutil.move(desktopPath + file, 'D:\\Vishesh\\Work\\Documents\\' + file)
		print ('Moved ' + file)
	
	#DBScript for Training 
	elif file[:6] == 'DBS_T_':
		shutil.move(desktopPath + file, 'D:\\Vishesh\\Training\\DB\\' + file)
		print ('Moved ' + file)
	
	else:
		print('Uncategorized ' + file)