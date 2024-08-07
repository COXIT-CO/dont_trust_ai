## HOW TO RUN:

```
python -m venv .venv
.venv\Scripts\activate 
streamlit run app.py
```
And then enter your LMM settings and prompt

### Example:

```
Input LLM model: anthropic/claude-3.5-sonnet
Input temperature of model: 0
Input your prompt:

You are Casework expert. 
You review specification and follow the instruction to pick correct Series option which represents cabinets materials and thickness:  
OPTIONS: {OPTIONS} 
INSTRUCTION: {INSTRUCTION}   
SPECIFICATION: {INPUT_TEXT}   
You think step by step. You markup the result option as following:  
RESULT: result series

```

### Create constants.py file with variables for prompt