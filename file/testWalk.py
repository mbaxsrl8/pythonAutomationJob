import os

for folderName, subFolders, fileNames in os.walk('F:\\python projects'):
    print('The current folder is ' + folderName)

    for subFolder in subFolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subFolder)

    for fileName in fileNames:
        print('FILE INSIDE ' + folderName + ': ' + fileName)

    print(' ')
