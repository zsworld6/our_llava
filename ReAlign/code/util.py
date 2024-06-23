import json
from openai import OpenAI
import asyncio
from typing import Any
import base64


def load_single_jsonl_file(data_file):
    with open(data_file)as f:
        lines = f.readlines()
    return [json.loads(l, strict=False) for l in lines]


def load_single_json_file(data_file):
    with open(data_file)as f:
        data = json.load(f)
    return data


def load_jsonl_data(data_file):
    raw_dataset = []
    if isinstance(data_file, str):
        raw_dataset += load_single_jsonl_file(data_file)
    elif isinstance(data_file, list):
        for f_ in data_file:
            raw_dataset += load_single_jsonl_file(f_)
    return raw_dataset


def load_json_data(data_file):
    raw_dataset = []
    if isinstance(data_file, str):
        raw_dataset += load_single_json_file(data_file)
    elif isinstance(data_file, list):
        for f_ in data_file:
            raw_dataset += load_single_json_file(f_)
    return raw_dataset


def ChatGPT_API(system_instruction, user_input, model, api_key, temperature=0.7, top_p=0.9, n=1, target_length=1024):    
    client = OpenAI(
        api_key=api_key,
        base_url=YOUR_BASEURL
    )
    messages=[
        {"role": "system", "content": system_instruction},
        {"role": 'user', "content": user_input}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,        
        temperature=temperature,
        max_tokens=target_length,
        top_p=top_p,
        n=n,
    )
    return response.choices

def get_image(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    