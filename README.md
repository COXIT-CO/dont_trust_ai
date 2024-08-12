## HOW TO RUN:
### 1. Create constants.py file with:
- PROMPT
- OPTIONS
- INSTRUCTION
- INPUT_TEXT_1
- INPUT_TEXT_2
- ...
- INPUT_TEXT_9

### 2. Create .env file with:
- OPENROUTER_API_KEY
- DEFAULT_LLM_MODEL
- DEFAULT_LLM_TEMPERATURE
- CSV_FILE_PATH
### 3. Add testcases.csv file with data
```
docker-compose up --build
```
App is running on http://localhost:8501/

## And then enter your LMM settings and prompt


