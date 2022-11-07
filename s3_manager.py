import boto3
import os

from secrets import ACCESS_KEY, SECRET_ACCESS_KEY

class S3Manager:
    def send(self):
        client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_ACCESS_KEY)

        for file in os.listdir():
            if '.csv' in file:
                upload_file_bucket = "onwelo-bucket-recruitment"
                upload_file_key = "big_mac_index/" + str(file)
                client.upload_file(file, upload_file_bucket, upload_file_key)
