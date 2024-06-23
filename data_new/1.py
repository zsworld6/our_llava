import requests
import base64

# 设置 API 密钥
api_key = "sk-eYT6k63VWtNQo4G24a068397AfBb49258aC5Cb3f96A3C3Da"

# 自定义基础 URL
base_url = "https://lonlie.plus7.plus/v1"

# 定义请求头
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# 定义请求体数据
payload = {
    "model": "gpt-4o",
    "prompt": "Hello, how are you?",
    "max_tokens": 50
}

# 发送POST请求
response = requests.post(f"{base_url}/chat/completions", headers=headers, json=payload)

# 打印响应
print(response.json())
