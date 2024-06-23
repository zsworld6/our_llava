from openai import OpenAI
import base64
import requests
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "/home/cs2916_t1/b8bd61e5dd7c9f2290c2b3df273554dc.png"

# Getting the base64 string
base64_image = encode_image(image_path)

client = OpenAI(
    api_key="sk-VgOwR6H4OERWSIno00413793Eb974a239d850d0d7071De31",
# https://api3.apifans.com/v1",
    base_url="https://api3.apifans.com/v1"
)

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0].message.content)