import os
import openai

def main(event, context):
  print('🔥🔥🔥')
  fname = "YcPwmCj0iGI.m4a"
  openai.api_key = os.environ['OPENAI_API_KEY']
  audio_file = open(fname, "rb")
  transcript = openai.Audio.transcribe("whisper-1", audio_file)
  txt = transcript['text']
  f = open(fname + ".txt", "w")
  f.write(txt)
  f.close()

if __name__ == "__main__":
  event = { 'data': '', 'part': '0' }
  main(event, '')
