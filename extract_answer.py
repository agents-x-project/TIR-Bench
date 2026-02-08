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
import argparse  # 新增
from openai import AzureOpenAI
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


def get_response_text(model, text, api_key, azure_endpoint, api_version="2025-01-01-preview"):
    client = AzureOpenAI(
        azure_endpoint=azure_endpoint,
        api_key=api_key,
        api_version=api_version
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


def process_file(file_path, model_name, api_key, azure_endpoint, api_version):
    """处理单个JSON文件的逻辑"""
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

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
        
        if 'extracted_answer' in item.keys():
            continue
            
        text = item['prompt']
        response = item['model_response']
        assert response is not None

        full_prompt = create_test_prompt(demo_prompt, text, response)
        extracted_answer = get_response_text(
            model_name, full_prompt, api_key, azure_endpoint, api_version
        )
        item['extracted_answer'] = extracted_answer
        
        if l % 10 == 0:
            print(f"Progress: {l}")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
        l += 1
        
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    
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
        default='/home/ming/results_TIR/',
        help='Directory containing the JSON files'
    )
    
    # Azure OpenAI 参数
    parser.add_argument(
        '--api-key', 
        type=str, 
        default='',
        help='Azure OpenAI API key'
    )
    parser.add_argument(
        '--endpoint', 
        type=str, 
        default='https://gpt.yunstorm.com/',
        help='Azure OpenAI endpoint URL'
    )
    parser.add_argument(
        '--api-version', 
        type=str, 
        default='2025-01-01-preview',
        help='Azure OpenAI API version'
    )
    
    # 模型参数
    parser.add_argument(
        '--model', 
        type=str, 
        default='gpt-4o',
        choices=['gpt-4o', 'gpt-4o-mini', 'o1', 'o3-mini', 'o3', 'o4-mini', 
                 'gpt-4.1', 'gpt-4.1-mini', 'gpt-4.1-nano'],
        help='Model to use for extraction'
    )
    
    # 其他选项
    parser.add_argument(
        '--skip-existing', 
        action='store_true',
        default=True,
        help='Skip items that already have extracted_answer (default: True)'
    )
    parser.add_argument(
        '--no-skip-existing', 
        dest='skip_existing',
        action='store_false',
        help='Force re-extraction even if extracted_answer exists'
    )

    args = parser.parse_args()

    # 处理文件列表
    if not args.files:
        print("No files specified. Use --files to provide comma-separated file list.")
        return

    file_list = [f.strip() for f in args.files.split(',') if f.strip()]
    
    if not file_list:
        print("No valid files to process.")
        return

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
                api_key=args.api_key,
                azure_endpoint=args.endpoint,
                api_version=args.api_version
            )
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue


if __name__ == '__main__':
    main()