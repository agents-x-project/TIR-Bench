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
