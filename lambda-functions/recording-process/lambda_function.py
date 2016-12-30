from __future__ import print_function

import json
import urllib
import boto3
import base64
import mimetypes
import os

import StringIO

print('Iam Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    # Get the object from the event and show its content type
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        body = response['Body'].read()
        decoded = StringIO.StringIO(base64.b64decode(body))
        file_name = os.path.basename(key).rstrip('.b64')
        content_type = mimetypes.guess_type(file_name)[0]
        s3.put_object(
            Bucket=bucket,
            Key='%s/%s' % (os.path.dirname(key), file_name),
            Body=decoded,
            ACL='public-read',
            ContentType=content_type)
        s3.delete_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        print('S3 URL: ' + str({'s3_url': 'https://s3.amazonaws.com/%s/%s' % (os.path.dirname(key), file_name)}))
        return {'s3_url': 'https://s3.amazonaws.com/%s/%s' % (os.path.dirname(key), file_name)}
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

