+++
title = 'Langsmith vs OpenAI Evals vs DeepEval: A Comprehensive Evaluation'
date = 2024-10-14T12:35:30+03:00
draft = false
author = 'Yaroslav Biziuk'
+++


# Langsmith vs OpenAI Evals vs DeepEval: A Comprehensive Evaluation

## Evaluating and Testing

Langsmith offers an online UI for prompt testing using either a custom dataset or manual inputs. This feature is particularly convenient because it allows users to store prompts along with their commit history and test results. Unfortunately, in DeepEval, testing cannot be done directly through the UI. Instead, users must use code to create `TestCase` objects and evaluate the results through the UI. Also OpenAI provides a powerful SDK for evaluating prompts. However, it requires a bit more setup.


![img_1.png](/dont_trust_ai/posts/comprehensive_frameworks_evaluation/img_1.png)

*Picture 1. Prompt saved in Langsmith*

![img_2.png](/dont_trust_ai/posts/comprehensive_frameworks_evaluation/img_2.png)  

*Picture 2. Langsmith SDK for testing*  

![img_3.png](/dont_trust_ai/posts/comprehensive_frameworks_evaluation/img_3.png)
![img_3_1.png](/dont_trust_ai/posts/comprehensive_frameworks_evaluation/img_3_1.png)

*Picture 3. OpenAI SDK for testing and evaluating*

### Metrics

Metrics are crucial for evaluating LLM performance. All three frameworks—Langsmith, OpenAI Evals, and DeepEval—support both default metrics and custom metric creation. Here is how it's implemented across the frameworks:

![img_4.png](/dont_trust_ai/posts/comprehensive_frameworks_evaluation/img_4.png)

*Picture 4. Default metrics in Langsmith*  

![img_5.png](/dont_trust_ai/posts/comprehensive_frameworks_evaluation/img_5.png) 

*Picture 5. Creating custom metrics in Langsmith* 

![img_6.png](/dont_trust_ai/posts/comprehensive_frameworks_evaluation/img_6.png)

*Picture 6. Default metrics in DeepEval*  
...  
*Picture 7. Creating custom metrics in DeepEval*  
...  
*Picture 8. Default metrics in OpenAI Eval*  
...  
*Picture 9. Creating custom metrics in OpenAI Eval*

### Conclusion on metrics

DeepEval stands out for its simplicity and user-friendly features, including easy-to-use default metrics and simple custom metric creation, requiring only two parameters: evaluation criteria and evaluation steps. On the other hand, OpenAI Evals and Langsmith offer more flexibility for custom evaluations by allowing users to create entirely custom prompts for LLM performance assessment. While DeepEval is ideal for ease of use, OpenAI Evals and Langsmith offer more precision and flexibility. Langsmith also allows testing directly within its playground, making it a fully-contained framework for prompt development. Additionally, OpenAI Evals provides almost free dataset testing, though result evaluation requires either manual methods or the paid LLM metrics feature.

The cost of evaluating responses with LLM metrics can vary. For example, using GPT-4o-mini to check the match between `expected_response` and `actual_response` typically costs about one cent for nine test cases, but this cost depends on the LLM model that we want to use and the context size being sent to the LLM in Judge.



## Dataset Management

Langsmith can automatically collect datasets from user inputs and allow them to be downloaded for further evaluation and testing using different prompts or LLM models in OpenAI Evals. DeepEval offers a similar feature, but this functionality is executed via code using the `save_as(file_path)` function.

...  
*Picture 10. Downloading dataset in JSONL format*  
...  
*Picture 11. Importing dataset into OpenAI Evals for testing*

## Monitoring Calls

OpenAI Evals does not support monitoring, so the comparison will focus on Langsmith and DeepEval. Langsmith offers a convenient way to monitor LLM calls by wrapping the OpenAI client in a function from the Langsmith library:

```python
client = wrap_openai(get_client())
```

This allows for tracking input, output, tokens, pricing, etc. By adding the `@traceable` decorator, users can also monitor function execution time and input parameters.

...  
*Picture 12. Monitoring call to OpenAI in Langsmith*  
...  
*Picture 13. Monitoring function call in Langsmith*

DeepEval, on the other hand, provides a simpler monitoring process. By sending a call to DeepEval, specifying the input, output, and other parameters, monitoring is easily achieved:

```python
deepeval.monitor(
    event_name="Stevens Agent",
    model=llm_model,
    input=input_text,
    response=llm_response,
    token_cost=total_cost,
    completion_time=completion_time,
)
```

...  
*Picture 14. Monitoring calls in DeepEval*  
...  
*Picture 15. Detailed call page in DeepEval*

## Adding New Examples to Dataset

In Langsmith, adding new test cases to a dataset involves selecting the required test cases, clicking “Add to Dataset,” and choosing the target dataset.

...  
*Picture 16. Selecting the required test cases in Langsmith*  
...  
*Picture 17. Selecting a dataset in Langsmith*  
...  
*Picture 18. Added test cases in dataset in Langsmith*

Test cases can also be edited by modifying the `input` or `output`.

...  
*Picture 19. Editing the test cases in Langsmith*

In DeepEval, the process is similar, but it allows users to immediately add expected output, retrieval context, and other details. User comments and feedback are also reviewed on the same page.

...  
*Picture 20. Selecting the required test cases in DeepEval*  
...  
*Picture 21. Selecting a dataset in DeepEval*  
...  
*Picture 22. Added test cases in dataset in DeepEval*  
...  
*Picture 23. Editing the test cases in DeepEval*

## Collecting Human Feedback

One of the best ways to improve LLM performance is through human-in-the-loop techniques, where user feedback is collected to further optimize responses.

In Langsmith, feedback can be sent using the following code:

```python
llm_response = call_llm(input)
run = get_current_run_tree()

return llm_response, run.id
```

With the `run.id`, feedback can be submitted:

```python
def send_feedback_to_langsmith():
    langsmith_client = LangsmithClient()
    langsmith_client.create_feedback(
        run_id,
        key="Correctness",
        score=0.8,
        comment="Very well",
        correction={
            "Expected result": "1200-N not 1200-C"
        }
    )
```

...  
*Picture 24. Monitoring Langsmith LLM calls filtered by feedback*  
...  
*Picture 25. Detail feedback page in Langsmith*

In DeepEval, the response ID is returned as a result of the `deepeval.monitor` function, and this ID is used for feedback tracking:

```python
response_id = deepeval.monitor(
    event_name="Stevens Agent",
    model=llm_model,
    input=input_text,
    response=llm_response,
    token_cost=total_cost,
    completion_time=completion_time,
)
return llm_response, response_id
```

...  
*Picture 26. Monitoring DeepEval LLM calls filtered by feedback*  


![img_27.png](/dont_trust_ai/posts/comprehensive_frameworks_evaluation/img_27.png) 

*Picture 27. Detail feedback page in DeepEval*

## Pricing

### LangSmith Pricing

![img.png](/dont_trust_ai/posts/comprehensive_frameworks_evaluation/img_28.png)
*Picture 28. LangSmith Pricing*

### DeepEval Pricing

![img.png](/dont_trust_ai/posts/comprehensive_frameworks_evaluation/img_29.png)
*Picture 29. DeepEval Pricing*

## Overall Conclusion

Each of these frameworks provides valuable tools for developing and maintaining LLM applications. OpenAI Evals is well-suited for prompt optimization on large datasets, as it allows for relatively cost-free testing. DeepEval offers the simplest and most intuitive interface. Langsmith stands out as the most flexible framework, but mastering it requires a significant time investment. Ultimately, the choice between these tools depends on individual preferences and project requirements.