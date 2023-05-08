import json
import subprocess, base64

def execute(event, context):
  # video_id = event['queryStringParameters']['video_id']
  # part = event['queryStringParameters']['part']
  returncode, error_message, file = extract("YcPwmCj0iGI", 0)
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": event
  }

  response = {
      "statusCode": 200,
      "body": json.dumps(body)
  }

  return response

def extract(video_id, part):
  result = subprocess.run(["yt-dlp", "-f", "m4a", "-o", f"/tmp/videos/%(channel_id)s/{part}/%(id)s.%(ext)s", video_id], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  return result.returncode, result.stderr, filename(result.stdout)

if __name__ == "__main__":
  event = { 'data': '', 'part': '0' }
  execute(event, '')
