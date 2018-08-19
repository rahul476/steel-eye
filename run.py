"""File with lambda excution funtion"""

import helper

DOWNLOAD_LINK = "https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls"
LAMBDA_URL = "https://8kar3zzax7.execute-api.ap-south-1.amazonaws.com/prod/upload"
SHEET_NAME = "MICs List by CC"

def process():
    """Start the excution of the program"""
    #Download and Parse the xls document
    json_object = helper.download_parse_xls_file(DOWNLOAD_LINK, SHEET_NAME)
    #Save the file to s3 with public access
    object_url = helper.upload_file(LAMBDA_URL, json_object)
    print(object_url)

process()