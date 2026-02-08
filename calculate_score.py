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
import tempfile
from tqdm import tqdm
import re
import concurrent.futures
import json
import argparse  # 新增
from openai import AzureOpenAI
from demo_prompts import demo_prompt_color
from Levenshtein import distance
import re
from math_verify import parse, verify

from tools import *
import ast


def main():

    # 设置argparse
    parser = argparse.ArgumentParser(description='Evaluate TIR model responses')
    
    parser.add_argument('--lists', type=str,
                        help='Comma-separated list of JSON files to process')
    parser.add_argument('--data-dir', type=str,
                        help='Directory containing result files')
    
    args = parser.parse_args()

    # 解析参数
    lists = [i.strip() for i in args.lists.split(',') if i.strip()]
    
    # 如果没有指定文件，退出
    if not lists:
        print("No files specified. Use --lists to provide comma-separated file list.")
        return

    # 主处理逻辑
    for p in lists:
        path = os.path.join(args.data_dir, p)
        print(path)
        
        if not os.path.exists(path):
            print(f"Warning: File not found: {path}")
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        keys = data.keys()

        # 动态收集所有遇到的 task 类型
        task_correct = {}
        correct = 0
        total = len(keys)

        for key in keys:
            item = data[key]
            correctness = 0
            
            # 获取 task 名称
            if 'task' in item.keys():
                task = item['task']
            else:
                task = item['category']
            
            # 初始化 task 的列表（如果是新遇到的 task）
            if task not in task_correct:
                task_correct[task] = []
            
            # 处理 answer 提取
            if task != 'ocr':
                assert 'extracted_answer' in item.keys()
                if item['extracted_answer'] == None:
                    item['extracted_answer'] = ''
            
            # 统一处理：清理 extracted_answer
            extracted_answer = item['extracted_answer'].replace('*', '').strip() if item['extracted_answer'] else ''
            answer = str(item['answer'])

            # 根据 task 类型判断正确性
            if task == 'ocr':
                response = item['model_response']
                if type(response) == list:
                    response = response[0]
                # 特殊 case 处理
                if '60.jpg' in item['image_1']:
                    answer = 'mobi'
                if '62.jpg' in item['image_1']:
                    answer = 'aires'
                if answer in response:
                    correctness = 1
                    correct += correctness

            elif task == 'word_search':
                extraction = re.sub(r"[A-Za-z*:\s]+", "", extracted_answer).strip()
                if classify_string(answer) == 2:
                    correctness = judge_int(extracted_answer, answer)
                    correct = correct + correctness
                else:
                    try:
                        a1, a2 = extract_two_numbers(answer)
                        r1, r2 = extract_two_numbers(extracted_answer)
                        if a1 == r1 and a2 == r2:
                            correctness = 1
                            correct += 1
                    except:
                        pass

            elif task == 'spot_difference':
                if classify_string(answer) == 2:
                    correctness = judge_int(extracted_answer, answer)
                    correct = correct + correctness
                else:
                    try:
                        list_answer = extract_consecutive_integers(answer)
                        list_response = extract_consecutive_integers(extracted_answer)
                        correctness = list_iou(list_response, list_answer)
                        correct += correctness
                    except:
                        pass

            elif task == 'jigsaw':
                try:
                    if 'metadata' in item.keys():
                        meta_key = 'metadata'
                    else:
                        meta_key = 'meta_data'
                    m_re = extract_consecutive_n_squared(extracted_answer, item[meta_key]['difficulty'])
                    a_re = extract_consecutive_n_squared(answer, item[meta_key]['difficulty'])
                    correctness = compare(a_re, m_re)
                    correct += correctness
                except Exception as e:
                    pass

            else:
                # 其他所有任务使用标准评估逻辑
                string_type = classify_string(answer)
                if string_type == 1:
                    correctness = judge_choice(extracted_answer, answer, item)
                    correct = correct + correctness
                elif string_type == 2:
                    # int
                    correctness = judge_int(extracted_answer, answer)
                    correct = correct + correctness
                elif string_type == 3:
                    # float
                    correctness = judge_float(extracted_answer, answer)
                    correct = correct + correctness
                elif string_type == 4:
                    print(f'error {task}, answer is wrong')
                    print(item['question_id'])

            item['true_false'] = correctness
            task_correct[task].append(correctness)

        # 保存结果
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
        
        # 输出总体结果
        print(f'{p}: {correct / total}')
        
        # 输出每个 task 的结果
        for task in sorted(task_correct.keys()):
            task_list = task_correct[task]
            if len(task_list) == 0:
                continue
            task_acc = sum(task_list) / len(task_list)
            print(f'{task}(number: {len(task_list)}): {task_acc}')

        print('\n\n')


if __name__ == '__main__':
    main()