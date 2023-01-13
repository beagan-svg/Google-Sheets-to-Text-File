import os
import csv
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


def main():
    download_sheet("1zN7iNrgDse61K8ZLzpo7xY4aqOY6CONnEvIQoDLfDLQ")


def download_sheet(id):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)

    # Sample Google Sheet document: https://docs.google.com/spreadsheets/d/1zN7iNrgDse61K8ZLzpo7xY4aqOY6CONnEvIQoDLfDLQ/
    # Replace this ID 
    docID = id

    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_key(docID)

    # Write to csv file
    csvFileNames = []
    for i, worksheet in enumerate(spreadsheet.worksheets()):
        filename = str(i + 1) + '_' + str(worksheet.title) + '.csv'
        csvFileNames.append(filename)
        with open(filename, 'w', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(worksheet.get_all_values())

    # If you want to download in excel format
    '''
    with pd.ExcelWriter(spreadsheet.title + '.xlsx') as writer:
        for i in range(len(csvFileNames)):
            read_file = pd.read_csv(csvFileNames[i])
            newSheetName = csvFileNames[i].split('_', 1)[-1].replace('.csv', '')
            read_file.to_excel(writer, sheet_name=newSheetName, index=None)

    for i in csvFileNames:
        os.remove(i)
    '''

if __name__ == '__main__':
    main()
