import json
import boto3
import os
import requests
import openai


BUCKET_NAME='minutes-prod-contents'

s3 = boto3.resource('s3')

def main(event, context):
    print('🔥🔥🔥')
    print(event)
    get_parameter()
    event_object = event['Records'][0]['s3']['object']['key']
    bucket = s3.Bucket(BUCKET_NAME)
    obj = bucket.Object(event_object).get()

def hoge(event, context):
    print('🔥')
    fname = "YcPwmCj0iGI.m4a"
    openai.api_key = os.environ['OPENAI_API_KEY']
    audio_file = open(fname, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    txt = "\n".join(transcript['text'].split())
    f = open(fname + ".txt", "w")
    f.write(txt)
    f.close()

def get_parameter():
    print('🔥🔥🔥🔥')
    end_point = 'http://localhost:2773'
    path = '/systemsmanager/parameters/get/?name=/minutes/prod/OPENAI_API_KEY'
    url = end_point + path
    headers = {
        'X-Aws-Parameters-Secrets-Token': os.environ['AWS_SESSION_TOKEN']
    }
    res = requests.get(url, headers=headers)
    print(res)

if __name__ == "__main__":
  event = { 'data': '', 'part': '0' }
  hoge(event, '')
