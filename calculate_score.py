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
    # 定义默认参数值（保持与原脚本一致）
    default_tasks = 'maze, color, word_search, jigsaw, rotation_game, ocr, refcoco, spot_difference, visual_search, symbolic, math, contrast, instrument'
    default_safe_tasks = 'maze, color, rotation_game, refcoco, visual_search, symbolic, math, contrast, instrument'
    default_lists = ''
    default_data_dir = '/home/ming/results_TIR/'

    # 设置argparse
    parser = argparse.ArgumentParser(description='Evaluate TIR model responses')
    
    parser.add_argument('--tasks', type=str, default=default_tasks,
                        help='Comma-separated list of all tasks')
    parser.add_argument('--safe-tasks', type=str, default=default_safe_tasks,
                        help='Comma-separated list of safe tasks for standard evaluation')
    parser.add_argument('--lists', type=str, default=default_lists,
                        help='Comma-separated list of JSON files to process')
    parser.add_argument('--data-dir', type=str, default=default_data_dir,
                        help='Directory containing result files')
    
    args = parser.parse_args()

    # 解析参数（保持与原脚本相同的处理方式）
    tasks = [task.strip() for task in args.tasks.split(',')]
    assert len(tasks) == 13, f"Expected 13 tasks, got {len(tasks)}"

    safe_tasks = [task.strip() for task in args.safe_tasks.split(',')]
    
    lists = [i.strip() for i in args.lists.split(',') if i.strip()]
    
    # 如果没有指定文件，退出
    if not lists:
        print("No files specified. Use --lists to provide comma-separated file list.")
        return

    # 主处理逻辑（保持原脚本完全不变）
    for p in lists:
        path = os.path.join(args.data_dir, p)
        print(path)
        
        if not os.path.exists(path):
            print(f"Warning: File not found: {path}")
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        keys = data.keys()

        task_correct = {}
        for task in tasks:
            task_correct[task] = []
        correct = 0

        for key in keys:
            item = data[key]
            correctness = 0
            if 'task' in item.keys():
                task = item['task']
            else:
                task = item['category']
            if task != 'ocr':
                assert 'extracted_answer' in item.keys()
                if item['extracted_answer'] == None:
                    item['extracted_answer'] = ''
            if task in safe_tasks:
                extracted_answer = item['extracted_answer'].replace('*', '').strip()
                answer = str(item['answer'])
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

            elif task == 'ocr':
                answer = str(item['answer'])
                response = item['model_response']
                if type(response) == list:
                    response = response[0]
                if '60.jpg' in item['image_1']:
                    answer = 'mobi'
                if '62.jpg' in item['image_1']:
                    answer = 'aires'
                if answer in response:
                    correctness = 1
                    correct += correctness

            elif task == 'word_search':
                answer = str(item['answer'])
                extracted_answer = item['extracted_answer'].replace('*', '').strip()
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
                answer = str(item['answer'])
                extracted_answer = item['extracted_answer'].replace('*', '').strip()
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
                answer = str(data[key]['answer'])
                extracted_answer = data[key]['extracted_answer'].replace('*', '').strip()
                try:
                    if 'metadata' in data[key].keys():
                        meta_key = 'metadata'
                    else:
                        meta_key = 'meta_data'
                    m_re = extract_consecutive_n_squared(extracted_answer, data[key][meta_key]['difficulty'])
                    a_re = extract_consecutive_n_squared(answer, data[key][meta_key]['difficulty'])
                    correctness = compare(a_re, m_re)
                    correct += correctness
                except Exception as e:
                    pass

            item['true_false'] = correctness
            task_correct[task].append(correctness)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
            
        print(f'{p}: {correct / len(keys)}')
        for task in tasks:
            if len(task_correct[task]) == 0:
                continue
            print(f'{task}(number: {len(task_correct[task])}): {sum(task_correct[task]) / len(task_correct[task])}')

        print('\n\n')


if __name__ == '__main__':
    main()