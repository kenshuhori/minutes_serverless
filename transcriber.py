import json
import boto3
import os
import requests
import openai


BUCKET_NAME='minutes-prod-contents'

s3 = boto3.resource('s3')

def main(event, context):
    print(event)
    fname = "/tmp/leothefootball"
    openai.api_key = get_parameter()
    event_object = event['Records'][0]['s3']['object']['key']
    bucket = s3.Bucket(BUCKET_NAME)
    bucket.download_file(event_object, '/tmp/hoge.m4a')
    audio_file = open('/tmp/hoge.m4a', "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print("🔥")
    txt = "\n".join(transcript['text'].split())
    f = open(fname + ".txt", "w")
    f.write(txt)
    f.close()
    upload(fname + ".txt")

def get_parameter():
    end_point = 'http://localhost:2773'
    path = '/systemsmanager/parameters/get/'
    query_parameter = '?name=/minutes/prod/OPENAI_API_KEY&withDecryption=true'
    url = end_point + path + query_parameter
    headers = {
        'X-Aws-Parameters-Secrets-Token': os.environ['AWS_SESSION_TOKEN']
    }
    res = requests.get(url, headers=headers)
    return res.json()['Parameter']['Value']

def upload(file):
    response = s3.Object(BUCKET_NAME, f'/documents/{os.path.basename(file)}').upload_file(file)
    return response

if __name__ == "__main__":
  event = { 'data': '', 'part': '0' }
  main(event, '')
