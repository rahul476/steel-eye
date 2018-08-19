"""Amazon Helper"""

import os
import json
import boto3

BUCKET_NAME = os.environ.get("BUCKET_NAME")
S3_KEY = os.environ.get("S3_KEY")

S3_URL = "https://s3-ap-south-1.amazonaws.com/{0}/{1}"

def upload(key_name, body_content):
    """Upload the given file to s3, with the given key"""
    s3 = boto3.resource('s3')
    s3.Bucket(BUCKET_NAME).put_object(Key=key_name, Body=body_content, ACL='public-read')
    object_url = S3_URL.format(BUCKET_NAME, key_name)
    return object_url

def lambda_handler(event, context):
    """Process the lambda function"""
    event = json.dumps(event)
    return upload(S3_KEY, event)
