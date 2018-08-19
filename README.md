## Steel-Eye

Python project to download a xls file and process it to a json file and then upload the json file to s3.

### Getting Started

Download the external library boto3 and xlrd. Run the below command

```
pip install -r requirements.txt
```

Entry point for the program is run.py which downloads the xls file and process it to create a json file (containing the list of dictionaries) and call the api deployed in lambda (check lambda setup). Run the below command to start

```
python run.py
```

### Lambda setup

Delpoy awshelper.py file to AWS Lambda with awshelper.lamdba_handler as handler.
Set the environment variable 

```
S3_KEY = [S3PATH]
BUCKET_NAME = [S3BUCKETNAME]
```



