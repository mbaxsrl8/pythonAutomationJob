#! python3
# Removes the header from all CSV files in the current working dir

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working dir
for csvFileName in os.listdir('./removeCsvHeader'):
    if not csvFileName.endswith('.csv'):
        continue  # skip non-csv files

    print('Removing header from ' + csvFileName + '...')

    # Read the CSV file in (skipping first row)
    csvRows = []
    csvFileObj = open(os.path.join('./removeCsvHeader', csvFileName))
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue  # skip first row
        csvRows.append(row)
    csvFileObj.close()

    # Write out the csv file
    csvFileObj = open(os.path.join('headerRemoved', csvFileName), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
