<div align="center">

#  PyVision: Agentic Vision with Dynamic Tooling



<a href="https://arxiv.org/abs/2507.07998" target="_blank">
    <img alt="arXiv" src="https://img.shields.io/badge/arXiv-red?logo=arxiv" height="20" />
</a>
<a href="TIR-Bench: A Comprehensive Benchmark for Agentic Thinking-with-Images Reasoning" target="_blank">
    <img alt="HF Model: ViGaL" src="https://img.shields.io/badge/%F0%9F%A4%97%20_Benchmark-Data-ffc107?color=ffc107&logoColor=white" height="20" />
</a>


</div>

## Extract answers from model responses.

Add azure key in line 32 of extract_answer.py.

Change file path in line 62 and line 66 of extract_answer.py. 

Then run command below:
```bash
python extract_answer.py
```

Note that response file shoule follow structure below:
```json
{
'0': content, '1': content, ...
}
```

## Calculate Score
Change file path in line 42 and line 45 of calculate_score.py. 

Then run command below:
```bash
python calculate_score.py
```
