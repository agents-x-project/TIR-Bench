<div align="center">

#  TIR-Bench: A Comprehensive Benchmark for Agentic Thinking-with-Images Reasoning



<a href="https://arxiv.org/abs/2511.01833" target="_blank">
    <img alt="arXiv" src="https://img.shields.io/badge/arXiv-red?logo=arxiv" height="20" />
</a>
<a href="https://huggingface.co/datasets/Agents-X/TIR-Bench" target="_blank">
    <img alt="HF Model: ViGaL" src="https://img.shields.io/badge/%F0%9F%A4%97%20_Benchmark-Data-ffc107?color=ffc107&logoColor=white" height="20" />
</a>


</div>

## 🎯Overview
**TIR-Bench** is a comprehensive benchmark designed to evaluate the "thinking-with-images" capabilities of Multimodal Large Language Models (MLLMs), addressing a gap left by existing benchmarks like Visual Search which only test basic operations. As models like OpenAI o3 begin to intelligently create and operate tools to transform images for problem-solving, TIR-Bench provides 13 diverse tasks that each require novel tool use for image processing and manipulation within a chain-of-thought. Our evaluation of 22 leading MLLMs (including open-sourced, proprietary, and tool-augmented models) shows that TIR-Bench is universally challenging and that strong performance requires genuine agentic thinking-with-images capabilities. This repository contains the full benchmark, evaluation scripts, and a pilot study comparing direct versus agentic fine-tuning for this advanced reasoning.


## Download data
Please first download and extract images from https://huggingface.co/datasets/Agents-X/TIR-Bench.

## Extract answers from model responses.

Add azure key in line 32 of extract_answer.py.

Change file path in line 62 and line 66 of extract_answer.py. 

Then run command below:
```bash
bash run_extract_answer.sh
```

Note that response file shoule follow structure below:
```bash
{
  '0': content, 
  '1': content
}
```

## Calculate Score
Change file path in line 42 and line 45 of calculate_score.py. 

Then run command below:
```bash
bash run_calculate_score.sh
```


## Citation
If you use this benchmark in your research, please consider citing it as follows:
```
@article{li2025tir,
  title={TIR-Bench: A Comprehensive Benchmark for Agentic Thinking-with-Images Reasoning},
  author={Li, Ming and Zhong, Jike and Zhao, Shitian and Zhang, Haoquan and Lin, Shaoheng and Lai, Yuxiang and Chen, Wei and Psounis, Konstantinos and Zhang, Kaipeng},
  journal={arXiv preprint arXiv:2511.01833},
  year={2025}
}
```
