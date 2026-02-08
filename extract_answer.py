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
import tempfile
from tqdm import tqdm
import re
import concurrent.futures
import json
import argparse
from openai import OpenAI
from demo_prompts import (
    demo_prompt_instrument, demo_prompt_refcoco, demo_prompt_contrast,
    demo_prompt_jigsaw, demo_prompt_color, demo_prompt_maze, demo_prompt_math,
    demo_prompt_symbolic, demo_prompt_word_search, demo_prompt_rotation_game,
    demo_prompt_spot_difference, demo_prompt_visual_search
)


def create_test_prompt(demo_prompt, query, response):
    demo_prompt = demo_prompt.strip()
    test_prompt = f"Question: {query}\n\nModel response: {response}"
    full_prompt = f"{demo_prompt}\n\n{test_prompt}\n\nExtracted answer: "
    return full_prompt


def get_response_text(model, text, api_key, base_url):
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )
    patience = 100
    while patience > 0:
        patience -= 1
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": [{"type": "text", "text": " Assistant is a large language model trained by OpenAI."}]},
                    {"role": "user", "content": [{"type": "text", "text": text}]}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(e)


def process_file(file_path, model_name, api_config_path):
    """处理单个JSON文件的逻辑"""
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    api_config = json.load(open(api_config_path, "r"))
    api_key = api_config['api_key']
    base_url = api_config['base_url']

    keys = data.keys()
    l = 0

    assert len(keys) == 1215, f"Expected 1215 keys, got {len(keys)}"

    for key in keys:
        item = data[key]
        if 'task' in item.keys():
            task = item['task']
        else:
            task = item['category']
        
        if task == 'ocr':
            continue

        # 选择对应的demo prompt
        demo_prompt_map = {
            'maze': demo_prompt_maze,
            'color': demo_prompt_color,
            'math': demo_prompt_math,
            'word_search': demo_prompt_word_search,
            'jigsaw': demo_prompt_jigsaw,
            'rotation_game': demo_prompt_rotation_game,
            'refcoco': demo_prompt_refcoco,
            'spot_difference': demo_prompt_spot_difference,
            'visual_search': demo_prompt_visual_search,
            'symbolic': demo_prompt_symbolic,
            'contrast': demo_prompt_contrast,
            'instrument': demo_prompt_instrument
        }
        
        if task not in demo_prompt_map:
            raise Exception(f"Incorrect task name: {task}")
        
        demo_prompt = demo_prompt_map[task]
        
        # 对所有 item 都直接提取 answer，无论是否已经存在 extracted_answer
        text = item['prompt']
        response = item['model_response']
        assert response is not None

        full_prompt = create_test_prompt(demo_prompt, text, response)
        extracted_answer = get_response_text(
            model_name, full_prompt, api_key, base_url
        )
        item['extracted_answer'] = extracted_answer
        
        if l % 10 == 0:
            print(f"Progress: {l}")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
        l += 1
        
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Completed: {file_path}")


def main():
    parser = argparse.ArgumentParser(description='Extract answers from model responses using Azure OpenAI')
    
    # 文件列表参数
    parser.add_argument(
        '--files', 
        type=str, 
        default='',
        help='Comma-separated list of JSON files to process (e.g., "file1.json,file2.json")'
    )
    
    # 路径参数
    parser.add_argument(
        '--data-dir', 
        type=str, 
        default='/home/user/results_TIR/',
        help='Directory containing the JSON files'
    )
    
    # Azure OpenAI 参数
    parser.add_argument(
        '--api-config-path', 
        type=str, 
        default='',
        help='OpenAI API config path'
    )
    # 模型参数
    parser.add_argument(
        '--model', 
        type=str, 
        default='gpt-4.1',
        choices=['gpt-4.1', 'gpt-4.1-mini', 'gpt-4.1-nano'],
        help='Model to use for extraction'
    )

    args = parser.parse_args()

    file_list = [f.strip() for f in args.files.split(',') if f.strip()]

    # 处理每个文件
    for filename in file_list:
        file_path = os.path.join(args.data_dir, filename)
        
        if not os.path.exists(file_path):
            print(f"Warning: File not found: {file_path}")
            continue
            
        try:
            process_file(
                file_path=file_path,
                model_name=args.model,
                api_config_path=args.api_config_path
            )
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue


if __name__ == '__main__':
    main()