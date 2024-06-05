import os
import requests
import openai

openai.api_key = "sk-CkSDMVNBWNZZ4VXCC78e599c613941C59e690177328b9220"
openai.api_base = "https://api3.apifans.com/v1"
# 从环境变量中读取API密钥
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("API key not found. Please set the environment variable OPENAI_API_KEY.")
print ("begin to query")
# 设置API URL
usage_url = "https://api.openai.com/v1/dashboard/billing/usage"
headers = {
    "Authorization": f"Bearer {api_key}"
}
print ("begin to query")
# 查询API使用情况
response = requests.get(usage_url, headers=headers)
print ("begin to query")
if response.status_code == 200:
    usage_data = response.json()
    print("Usage Data:", usage_data)
else:
    print("Failed to retrieve usage data. Status code:", response.status_code)
    print("Response:", response.text)
