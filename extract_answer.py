import os
import base64
from binascii import Error

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
from demo_prompts import demo_prompt_instrument, demo_prompt_refcoco, demo_prompt_contrast, demo_prompt_jigsaw, demo_prompt_color, demo_prompt_maze, demo_prompt_math, demo_prompt_symbolic, demo_prompt_word_search, demo_prompt_rotation_game, demo_prompt_spot_difference, demo_prompt_visual_search

def create_test_prompt(demo_prompt, query, response):
    demo_prompt = demo_prompt.strip()
    test_prompt = f"Question: {query}\n\nModel response: {response}"
    full_prompt = f"{demo_prompt}\n\n{test_prompt}\n\nExtracted answer: "
    return full_prompt


def get_response_text(model, text):
    key = ''
    client = AzureOpenAI(
        azure_endpoint="https://gpt.yunstorm.com/",
        api_key=key,
        api_version="2025-01-01-preview"
    )
    patience = 100
    while patience > 0:
        patience -= 1
        try:
            response = client.chat.completions.create(
                model=model,
                # use model in list [gpt-4o, gpt-4o-mini, o1, o3-mini, o3, o4-mini, gpt-4.1, gpt-4.1-mini, gpt-4.1-nano]
                messages=[{"role": "system", "content": [
                    {
                        "type": "text",
                        "text": " Assistant is a large language model trained by OpenAI."
                    }
                ]}, {"role": "user", "content": [
                    {
                        "type": "text",
                        "text": text
                    }
                ]}]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(e)

#lists = 'TIR_collection_InternVL3-38B.json,TIR_collection_InternVL3-8B.json, TIR_collection_Qwen2.5-VL-3B-Instruct.json  ,TIR_collection_Qwen2.5-VL-7B-Instruct.json,  TIR_collection_llava-v1.6-vicuna-7b.json, TIR_collection_InternVL3-78B.json,  TIR_collection_Qwen2.5-VL-32B-Instruct.json,  TIR_collection_Qwen2.5-VL-72B-Instruct.json,  TIR_collection_llava-v1.6-mistral-7b.json'
lists =  ''#'TIR_collection_llava-next-72b.json, TIR_collection_llava-v1.6-34b.json'
lists = lists.split(',')
lists = [i.strip() for i in lists]
for p in lists:
    path = '/home/ming/results_TIR/'+p
    print(path)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    keys = data.keys()
    l=0

    assert len(keys)==1215

    for key in keys:
        item = data[key]
        if 'task' in item.keys():
            task = item['task']
        else:
            task = item['category']
        if task=='ocr':
            continue

        if task=='maze':
            demo_prompt = demo_prompt_maze
        elif task=='color':
            demo_prompt = demo_prompt_color
        elif task=='math':
            demo_prompt = demo_prompt_math
        elif task=='word_search':
            demo_prompt = demo_prompt_word_search
        elif task == 'jigsaw':
            demo_prompt = demo_prompt_jigsaw
        elif task=='rotation_game':
            demo_prompt = demo_prompt_rotation_game
        elif task=='refcoco':
            demo_prompt = demo_prompt_refcoco
        elif task=='spot_difference':
            demo_prompt = demo_prompt_spot_difference
        elif task=='visual_search':
            demo_prompt = demo_prompt_visual_search
        elif task=='symbolic':
            demo_prompt = demo_prompt_symbolic
        elif task=='contrast':
            demo_prompt = demo_prompt_contrast
        elif task=='instrument':
            demo_prompt = demo_prompt_instrument
        else:
            raise Exception("Incorrect task name.")
        if 'extracted_answer' in item.keys():
            continue
        text = item['prompt']
        response = item['model_response']
        assert response!=None

        full_prompt = create_test_prompt(demo_prompt, text, response)
        extracted_answer = get_response_text('gpt-4o', full_prompt)
        item['extracted_answer'] = extracted_answer
        if l%10==0:
            print(l)
            with open(path , 'w') as f:
                json.dump(data, f,ensure_ascii=False)
        l+=1
    with open(path , 'w') as f:
        json.dump(data, f,ensure_ascii=False)

