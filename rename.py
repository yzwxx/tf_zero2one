#! /usr/bin/env python 
# -*-coding:utf-8 -*-

'''
This script is used for renaming the image filenames from a complex string to sth like X.jpg
'''
import os
def rename_all(filePath):
	allFiles = os.listdir(filePath)
	# allFiles is a list of all filenames under filePath 
	index = 1
	for fileName in allFiles:
		if fileName.endswith('.jpg'):
			newName = str(index) + '.jpg'
			fileName_full = os.path.join(filePath,fileName)
			newName_full = os.path.join(filePath,newName)
	# tip: os.rename requires absolute file path,otherwise an OSError:No such file or directory will be raised
			os.rename(fileName_full,newName_full)
			index += 1
		else:
			pass



if __name__ == '__main__':
	filePath = os.path.join(os.getcwd(),'test')
	rename_all(filePath)