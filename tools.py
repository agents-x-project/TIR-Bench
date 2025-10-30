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
from demo_prompts import demo_prompt_color
from Levenshtein import distance
import re
from math_verify import parse, verify



def extract_consecutive_n_squared(s, n):
    """
    提取字符串中第一个连续出现的 n^2 个数字的序列

    参数:
        s (str): 输入字符串（混合内容）
        n (int): 维度，目标提取 n^2 个数字

    返回:
        List[int]: 第一个匹配到的连续 n^2 个数字
    """
    total = n * n
    # 匹配：连续由数字和合法分隔符（逗号、空格、换行）组成的段落
    sequences = re.findall(r'[\d\s,，]+', s)
    #print(len(sequences))
    for seq in sequences:
        # 从该段落中提取所有数字
        nums = re.findall(r'\d+', seq)
        #print(nums)
        if len(nums) == total:
            return [int(num) for num in nums]

    raise ValueError(f"未找到连续的 {total} 个数字的子序列。")

def compare(l1,l2):
    correct = 0
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            correct += 1
    return correct/len(l1)

def extract_consecutive_integers(s):
    # 匹配数字，允许数字之间有空格或逗号分隔
    matches = re.findall(r'\d+(?=[,\s]*|\b)', s)
    return [int(num) for num in matches]

def extract_two_numbers(text):
    # 正则匹配两个连续数字，中间为逗号或逗号+空格
    match = re.search(r'\b(\d+)\s*,\s*(\d+)\b', text)
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        return num1, num2
    return None  # 没找到就返回 None

def list_iou(l_response, l_answer):
    set_response = set(l_response)
    set_answer = set(l_answer)
    intersection = set_response & set_answer  # 交集
    union = set_response | set_answer         # 并集
    if not union:
        return 1.0  # 两个都是空列表，IoU 定义为 1
    return len(intersection) / len(union)

def classify_string(s):
    if s.isalpha():
        return 1
    try:
        int(s)
        return 2
    except ValueError:
        pass
    try:
        float(s)
        return 3
    except ValueError:
        pass
    return 4


def get_most_similar(prediction, choices):
    """
    Use the Levenshtein distance (or edit distance) to determine which of the choices is most similar to the given prediction
    """
    distances = [distance(prediction, choice) for choice in choices]
    ind = distances.index(min(distances))
    return choices[ind]


results = {}


def judge_int(extracted_answer, answer):
    correctness = 0
    extraction = extracted_answer.replace('Extracted answer:', '').strip()
    extraction = re.sub(r"[A-Za-z*:\s]+", "", extraction).strip()
    try:
        extraction = int(extraction)
        answer = int(answer)
        if extraction == answer:
            correctness = 1
    except:
        correctness = 0

    if correctness == 0:
        try:
            extraction = parse(extracted_answer)
            if float(verify(extraction, parse(str(answer)))) > 0:
                correctness = 1.0
        except Exception:
            pass

    return correctness


def judge_float(extracted_answer, answer):
    correctness = 0
    extraction = extracted_answer.replace('Extracted answer:', '').strip()
    extraction = re.sub(r"[A-Za-z*:\s]+", "", extraction).strip()
    try:
        extraction = float(extraction)
        answer = float(answer)
        if extraction == answer:
            correctness = 1
    except:
        correctness = 0

    if correctness == 0:
        try:
            extraction = parse(extracted_answer)
            if float(verify(extraction, parse(str(answer)))) > 0:
                correctness = 1.0
        except Exception:
            pass

    return correctness


def judge_choice(extracted_answer, answer, item):
    choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'H']
    correctness= 0
    if len(answer) == 1:
        # single choice question
        if answer in choices:
            extraction = extracted_answer.replace('Extracted answer:', '').strip()
            if extraction not in choices:
                # select the most similar option
                for x in choices:
                    if x + '. ' + extraction in item['prompt'] or x + '.' + extraction in item[
                        'prompt'] or x + ' ' + extraction in item['prompt'] or x + '' + extraction in item[
                        'prompt']:
                        extraction = x
                extraction = get_most_similar(extraction, choices)
            if extraction == answer:
                correctness = 1
    else:
        # multi-choice question
        sorted_answer = ''.join(sorted(answer))
        sorted_extracted_answer = ''.join(sorted(extracted_answer))
        if sorted_answer == sorted_extracted_answer:
            correctness = 1

    return correctness
