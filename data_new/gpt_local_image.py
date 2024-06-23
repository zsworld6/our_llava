import base64
import requests
api_key="sk-eYT6k63VWtNQo4G24a068397AfBb49258aC5Cb3f96A3C3Da",
    # base_url="https://lonlie.plus7.plus/v1"
# OpenAI API Key
# api_key = "sk-0z5DsAu12nUg7NrSE3Be4d76E5294aE7900b1b3e37007698"
# base_url="https://lonlie.plus7.plus/v1"
# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "/home/cs2916_t1/b8bd61e5dd7c9f2290c2b3df273554dc.png"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4o",
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

response = requests.post("https://lonlie.plus7.plus/v1/chat/completions", headers=headers, json=payload)

print(response.json())