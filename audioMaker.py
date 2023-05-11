import json
import boto3
import subprocess, base64, os
import yt_dlp

BUCKET_NAME='minutes-prod-contents'

s3 = boto3.resource('s3')
ydl_opts = {
    'format': 'm4a',
    'outtmpl': '/tmp/videos/%(id)s.%(ext)s'
}

def main(event, context):
    video_id = 'YcPwmCj0iGI'
    part = 0
    returncode, error_message, file = extract(video_id, part)
    if returncode != 1:
        upload(file)
    else:
        print(error_message)

def extract(video_id, part):
    urls = [f'https://www.youtube.com/watch?v={video_id}']
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(urls)
    return error_code, 'error_message if exists...', f'/tmp/videos/{video_id}.m4a'

def upload(file):
    response = s3.Object(BUCKET_NAME, f'/audios/{os.path.basename(file)}').upload_file(file)
    return response

if __name__ == "__main__":
    event = { 'data': '', 'part': '0' }
    main(event, '')
