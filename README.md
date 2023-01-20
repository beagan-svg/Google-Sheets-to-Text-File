Sheets-to-Text-File
=================================================
![cover](images/sheet_to_text.png)

## About
A python script to download Google Sheets Data as a text file (csv/excel). This script supports downoload of multiple sheets in one spreadsheet

Table of Contents
-----------------
* [Usage](#usage)
* [Authors and history](#authors-and-history)
* [Acknowledgments](#acknowledgments)
* [References](#references)

## Usage
1. Clone the repository
```bash
git clone 'https://github.com/beagan-svg/Google-Sheets-to-Text-File'
```
2. Install the necessary Python packages using these commands
```bash
pip install gspread
pip install pandas
pip install oauth2client
pip install openpyxl
```
3. In the sheet_to_text.py file, replace string with ID of the document you want to download. ID can be found on google sheet URL.
Example:
```bash
1zN7iNrgDse61K8ZLzpo7xY4aqOY6CONnEvIQoDLfDLQ would be the ID for the URL: https://docs.google.com/spreadsheets/d/1zN7iNrgDse61K8ZLzpo7xY4aqOY6CONnEvIQoDLfDLQ/
```
4. Run the Script.
```bash
python3 sheet_to_text.py
``` 
## Authors and History

* Beagan Nguy - Algorithm Design
* Anish Chakka - Project Manager
* Aaron Oster - Project Lead

## Acknowledgments

Allen Institute Bioinformatics Core Team

