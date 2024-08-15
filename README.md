## HOW TO RUN:

### 1. Create prompts.csv file with available prompts in the 'inputs' directory with such format:
<table>
  <thead>
    <tr>
      <th>№</th>
      <th>Prompt</th>
      <th>Template</th>
      <th>OPTIONS</th>
      <th>INSTRUCTION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Prompt-1</td>
      <td>Template-1</td>
      <td>OPTIONS-1</td>
      <td>INSTRUCTION-1</td>
    </tr>
<tr>
      <th>...</th>
      <th>.................</th>
      <th>.................</th>
      <th>.................</th>
      <th>.................</th>
    </tr>
    <tr>
      <td>9</td>
      <td>Prompt-9</td>
      <td>Template-9</td>
      <td>OPTIONS-9</td>
      <td>INSTRUCTION-9</td>
    </tr>
  </tbody>
</table>

### 2. Create testcases.csv file with testcases in the 'inputs' directory with such format:
<table>
  <thead>
    <tr>
      <th>№</th>
      <th>Label</th>
      <th>Specification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <th>Label-1</th>
      <th>Specification-1</th>
    </tr>
    <tr>
      <th>...</th>
      <th>.......</th>
      <th>.......................</th>
    </tr>
    <tr>
      <th>9</th>
      <th>Label-9</th>
      <th>Specification-9</th>
    </tr>
  </tbody>
</table>

### 3. Create .env file with:
1. <b>OPENROUTER_API_KEY</b>
<br>
Description: This key is used to authenticate API requests to the OpenRouter service. 
It is essential for interacting with the OpenRouter API.
```
OPENROUTER_API_KEY=sk-****************************
```
<br>
<br>
2. <b>OPENROUTER_BASE_URL</b>
<br>
Description: The base URL for the OpenRouter API. 
This URL is used as the endpoint for all API requests.

Example:
```
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```
<br>
<br>

3. <b>OPENROUTER_DEFAULT_LLM_MODELS</b>
<br>
Description: A comma-separated list of default Large Language Models (LLMs) available for use on OpenRouter. 

Example: 
```
OPENROUTER_DEFAULT_LLM_MODELS=google/palm-2-codechat-bison:free,meta-llama/llama-3.1-8b-instruct:free
```

<br>
<br>

4. <b>PATH_TO_TESTCASES_CSV_FILE</b>
<br>
Description: The path to the CSV file containing test cases. This file is used to provide input data for testing the application's functionality.

Example: 
```
PATH_TO_TESTCASES_CSV_FILE=inputs/testcases.csv
```
<br>

5. <b>PATH_TO_PROMPT_CSV_FILE</b>
<br>
Description: The path to the CSV file containing prompts. This file is used to provide input prompts that the application will use for generating responses.

Example:
```
PATH_TO_PROMPT_CSV_FILE=inputs/prompts.csv
```
<br>
6. <b>TIMEZONE_REGION</b>
<br>
Description: The timezone region for the application. This setting is used to ensure that timestamps and scheduling are handled correctly according to the specified timezone.

Example: 
```
TIMEZONE_REGION=Europe/Kiev
```



## How to run commands:

### On Docker
```
docker-compose up --build
```
### On MacOs (Python 3.10)
```
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run src/app.py
```
**App is running on http://localhost:8501/**
