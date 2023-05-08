import json
import boto3
import subprocess, base64

BUCKET_NAME='minutes-prod-contents'

s3 = boto3.resource('s3')

def main(event, context):
  video_id = "YcPwmCj0iGI"
  part = 0
  returncode, error_message, file = extract(video_id, part)
  if returncode != 1:
    upload(file)
  else:
    print(error_message)

def extract(video_id, part):
  result = subprocess.run(["yt-dlp", "-f", "m4a", "-o", f"/tmp/videos/%(channel_id)s/{part}/%(id)s.%(ext)s", video_id], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  return result.returncode, result.stderr, filename(result.stdout)

def upload(file):
  # filename = file.replace('/tmp/videos/', '')
  response = s3.upload_file(file, BUCKET_NAME)
  return response

if __name__ == "__main__":
  event = { 'data': '', 'part': '0' }
  main(event, '')
