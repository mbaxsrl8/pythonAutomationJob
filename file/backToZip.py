#! /usr/bin/python3
# Copies an entire folder and its contents into a ZIP whose file name increments

import zipfile
import os


def backUpToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file
    folder = os.path.abspath(folder)  # make sure folder is absolute

    # Figure out the filename this code should use based on what files already exist
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '__' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1

    # Create the zip file
    print('Creating %s...' % (zipFileName))
    backUpZip = zipfile.ZipFile(zipFileName, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for folderName, subFolders, filenames in os.walk(folder):
        print('Adding files in %s...' % folderName)
        # Add the current folder to the ZIP file
        backUpZip.write(folderName)
        # Add all the files in this folder to the ZIP  file
        for filename in filenames:
            newBase = os.path.basename(folder) + '__'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # don't backup the backup ZIP files
            backUpZip.write(os.path.join(folderName, filename))

    backUpZip.close()
    print('Done')


backUpToZip('F:\\QQMusicCache')
