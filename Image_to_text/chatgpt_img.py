from openai import OpenAI
import base64
import requests
import translate_chinese
import os
api_key = ""

def img_to_text():
  folder_path = os.getcwd() + "\\image"
  def encode_image(image_path):
    with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')
  # //////////////////////////////////////////////////////////////////////////////////////
  def get_latest_image(folder_path):
      jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
      if not jpg_files:
          return None
      latest_file = max(
          jpg_files,
          key=lambda f: os.path.getmtime(os.path.join(folder_path, f))
      )
      return os.path.join(folder_path, latest_file)
  image_path = get_latest_image(folder_path)
  # //////////////////////////////////////////////////////////////////////////////////////
  base64_image = encode_image(image_path)

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What’s in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
  assistant_response = response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
  reply = translate_chinese.gpt(assistant_response)
  # reply.replace("這張圖像似乎顯示了一個")
  return reply