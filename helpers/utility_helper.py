"""Utility Helper Functions"""

import urllib.request
import json
import requests
from xlrd import open_workbook

def download_parse_xls_file(url, sheet_name):
    """Download and parse the xls file,
    then generate the json object (keep the first row as key in dict)"""

    try:
        #Download the file initialise the sheet
        file_name, headers = urllib.request.urlretrieve(url)
        workbook = open_workbook(file_name)
        sheet = workbook.sheet_by_name(sheet_name)

        #Get all the Headers (values in 1st row)
        header = [sheet.cell_value(0, cell).lower() for cell in range(sheet.ncols)]

        #Create list of dictionary from 2nd row
        list_of_dicts = []
        for row_index in range(1, sheet.nrows):
            row_cell = [sheet.cell_value(row_index, col_index) for col_index in range(sheet.ncols)]
            list_of_dicts.append(dict(zip(header, row_cell)))
        
        return json.dumps(list_of_dicts)

    except Exception as error_message:
        return None
    

def upload_file(url, data):
    """Call the lambda api to upload the data"""

    try:
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        response = requests.request(method="POST", url=url, data=data, headers=headers)
        if response.status_code is not 200:
            raise Exception(f"Error uplaoding file with status code : {response.status_code}")

        return response.text
    except Exception as error_message:
        return None
    





