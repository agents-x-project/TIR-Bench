import os
import base64
from openai import OpenAI
from typing import Optional, Dict, Any, Union, List
import logging
import matplotlib.pyplot as plt
from PIL import Image
import io
import numpy as np
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
# import cairosvg
import tempfile
from tqdm import tqdm
import re
import concurrent.futures
import json
import os
from openai import AzureOpenAI
from oai_module import get_response_toole_using, encode_image_to_base64, get_response, get_response_toole_using_boyue,get_response_toole_using_high

def encode_image_to_base64(image_path):
    """
    将本地图片编码为 base64 格式，返回可用于 OpenAI API 的 data URL。

    参数:
        image_path (str): 图片的本地路径（例如 "example.png"）

    返回:
        str: 以 "data:image/...;base64," 开头的完整 base64 编码字符串
    """
    # 自动判断图片 MIME 类型
    if image_path.lower().endswith(".png"):
        mime_type = "image/png"
    elif image_path.lower().endswith(".jpg") or image_path.lower().endswith(".jpeg"):
        mime_type = "image/jpeg"
    elif image_path.lower().endswith(".webp"):
        mime_type = "image/webp"
    else:
        raise ValueError("Unsupported image format. Only PNG, JPG, and WEBP are supported.")

    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return f"data:{mime_type};base64,{encoded_string}"




def get_response_openai(model, image, text,multi_image=None):
    client = OpenAI(api_key='')
    patience = 3
    if multi_image==None:
        input_items = [
            {
                "role": "user",
                "content": [
                    # 文本先放在最前面
                    {"type": "input_text", "text": text},

                    # 公开 URL

                    # Base64（用 data URI 包一层）
                    {
                        "type": "input_image",
                        "image_url": image
                    },

                ],
            }
        ]
    else:
        input_items = [
            {
                "role": "user",
                "content": [
                    # 文本先放在最前面
                    {"type": "input_text", "text": text},

                    # 公开 URL

                    # Base64（用 data URI 包一层）
                    {
                        "type": "input_image",
                        "image_url": image[0]
                    },

                    {
                        "type": "input_image",
                        "image_url": image[1]
                    },

                ],
            }
        ]
    while patience > 0:
        patience -= 1
        try:
            instructions = """
            You are a VQA problem solver. When tackling VQA problems, you may write code and run it by using the python tool to help you better perceive and address problems if needed.
            """

            resp = client.responses.create(
                model=model,
                input=input_items,
                timeout=6000,
            )

            return resp
        except Exception as e:
            print(e)


model = os.environ.get("RUN_NAME", None)
task = os.environ.get("TASK", None)


file_path = ''
save_path = ''
image_path = ''
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
if os.path.exists(save_path):
    with open(save_path, 'r', encoding='utf-8') as f:
        model_responses = json.load(f)
else:
    model_responses = {}



for i in range(len(data)):
    print(i)
    if str(i) in model_responses.keys() and model_responses[str(i)]['model_response']!=None:
        continue
    new_item = data[i]

    image1 = encode_image_to_base64(os.path.join(image_path, data[i]['image_1']))
    image2 = data[i]['image_2']
    if image2 != None:
        image2 = encode_image_to_base64(os.path.join(image_path, data[i]['image_2']))
        image = [image1, image2]
    else:
        image = image1
    text = data[i]['prompt']


    if image2 != None:
        response = get_response_openai(model, image, text, multi_image=True)
    else:
        response = get_response_openai(model, image, text)

    print('********************')
    if response != None:
        print(response.output[-1].content[0].text)
    print('********************')
    print(data[i]['answer'])
    print('********************')
    # print(data[i]['correct_answer'])
    if response != None:
        new_item['model_response'] = response.output[-1].content[0].text
        new_item['all_response'] = str(response)
    else:
        new_item['model_response'] = None

    model_responses[str(i)] = new_item
    with open(save_path, 'w') as f:
        json.dump(model_responses, f, ensure_ascii=False)