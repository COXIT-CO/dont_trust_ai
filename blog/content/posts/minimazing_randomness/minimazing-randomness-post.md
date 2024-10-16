+++
title = 'Minimizing Randomness in GPT Responses: A Guide to Using Seeds, Top_p, and Monitoring System Fingerprints'
date = 2024-10-15T13:09:30+03:00
draft = false 
author = 'Yaroslav Biziuk'
+++


When working with large language models (LLMs) like GPT, a major challenge is ensuring consistency in responses. These models are inherently stochastic, meaning randomness is embedded in their behavior. However, in certain applications, such as testing or content generation where consistency is crucial, it becomes essential to minimize this variability. In this article, we'll explore how to control randomness using parameters like seeds and `top_p`, and why monitoring the `system_fingerprint` parameter is critical. We'll also discuss why achieving full determinism in LLM responses is ultimately impossible.

## 1. Why Full Determinism Is Impossible

While setting a seed and controlling parameters like `top_p` can help reduce randomness, true determinism in LLM responses is impossible to achieve for several reasons:

- **Non-deterministic Model Behavior**: Even when `top_p` is set to an extremely low value (e.g., `top_p = 0.00000001`), which allows only the highest-ranking token to be selected, the model can still produce different outputs over time. This is due to underlying non-deterministic faults within the model. On longer text generations, even with such strict `top_p` settings, the highest-ranked token may switch occasionally due to the complex vector math that happens before token sampling. This behavior comes from the probabilistic nature of neural networks, meaning that token choice can vary despite tight constraints.

- **System Fingerprint Variability**: The `system_fingerprint` parameter provides a unique identifier for the backend system serving the model. However, this fingerprint can change every time you call the model. When the fingerprint changes, it can indicate that the underlying API backend or model architecture has been updated. As a result, even with identical seeds and settings, slight changes in the model's internal mechanics can lead to different outputs. Thus, even with strong controls over randomness, true determinism remains out of reach.

## 2. Using a Seed to Control Randomness

One of the most effective ways to reduce variability is by setting a seed. This ensures that, for a given input, the model produces the same output each time. While this helps create repeatability, it’s important to remember that due to the non-deterministic nature of LLMs, even this won’t guarantee perfect consistency across different API calls or versions of the model (especially if the `system_fingerprint` changes).

Lets test this parameters on our dataset. Call structure for GPT (_**gpt-4o-2024-05-13**_):

```python
completion = client.chat.completions.create(
    model=llm_model,
    temperature=0,
    seed=111,
    messages=[
        {
            "role": "system",
            "content": prompt_template.format(
                OPTIONS=options, INSTRUCTION=instruction, INPUT_TEXT=input_text
            ),
        }
    ],
)
```

Output:

![img_2.png](/dont_trust_ai/posts/minimazing_randomness/img_2.png)


[First call](https://docs.google.com/spreadsheets/d/1Y89Ga7uMHcSwVp0T4tqsBT4xwPSrb_8pjLL9A3ECtV4/edit?usp=sharing)


![img_3.png](/dont_trust_ai/posts/minimazing_randomness/img_3.png)

[Second call](https://docs.google.com/spreadsheets/d/1Y89Ga7uMHcSwVp0T4tqsBT4xwPSrb_8pjLL9A3ECtV4/edit?gid=482158444#gid=482158444)

![img_4.png](/dont_trust_ai/posts/minimazing_randomness/img_4.png)

[Third call](https://docs.google.com/spreadsheets/d/1Y89Ga7uMHcSwVp0T4tqsBT4xwPSrb_8pjLL9A3ECtV4/edit?gid=1411585284#gid=1411585284)

The same call to Claude(**_claude-3.5-sonnet-2024-06-20_**) gave three identical response for 3 calls:

![img_5.png](/dont_trust_ai/posts/minimazing_randomness/img_5.png)

Another call structure:
```python
completion = client.chat.completions.create(
   		model=llm_model,
   		temperature=0,
   		seed=999,
   		messages=[
       		{
           		"role": "system",
           		"content": prompt_template.format(
               		OPTIONS=options, INSTRUCTION=instruction
           		)},
       		{
           		"role": "user",
           		"content": input_text,
       		}
        ]
)
```

![img_6.png](/dont_trust_ai/posts/minimazing_randomness/img_6.png)

First call

![img_7.png](/dont_trust_ai/posts/minimazing_randomness/img_7.png)

Second and Third calls

### Conclusion: 
As demonstrated by the testing results above, setting the temperature or top_p to zero and utilizing a fixed seed do not guarantee determinism in model responses. The key factor influencing the outcome lies in the vector mathematics employed during the token selection process ([espesially in Third Layer of token generation : Beam Search with Randomness](https://neuralgap.io/understanding-randomness-within-llms-neuralgap/#:~:text=Layer%203%3A%20Beam%20Search%20with%20Randomness)). This process of selecting tokens can be compared to Dijkstra’s algorithm. While traditional algorithms like Dijkstra’s evaluate all possible paths to ensure an optimal solution, LLMs do not exhaustively explore every potential token combination. This would indeed lead to significantly slower response times. Instead, LLMs prioritize computational efficiency by selecting highly probable tokens based on contextual patterns, which sometimes results in variability across responses. LLM doesn’t check all possible solutions to find the best one but generates outputs that are likely correct, because of that, we can see different result series to the same input cabinet specification. As a result, the model may produce slightly different answers with each invocation, driven by its focus on optimizing computational resources while balancing accuracy.

## 3. Controlling Output Diversity with Top_p

The `top_p` parameter controls the probability distribution from which the model selects the next token. Setting `top_p` to a lower value restricts the model to a smaller pool of possible token choices, narrowing down the output variability.

However, lowering `top_p` too much can lead to unintended consequences:

- **Chain of Thought Resolution Issues**: For complex tasks that require multi-step reasoning or explanations (e.g., chain of thought processes), setting `top_p` too low (e.g., `top_p = 0.0001`) can drastically degrade the model's ability to think through problems. The lack of diversity in token selection limits the model’s ability to explore nuanced responses, leading to overly deterministic but shallow outputs.

- **Performance Deterioration**: Lowering `top_p` to extreme levels can result in outputs that are either repetitive or overly simplistic, as the model is forced to choose from a very narrow set of tokens.

But the top_p parameter, even when set alongside a constant seed for deterministic outputs, does not guarantee consistent results across multiple runs. Below you can see proof of this.

Call to Claude(**_claude-3.5-sonnet-2024-06-20_**) with this structure:
```python
completion = await client.chat.completions.create(
   model=llm_model,
   top_p=0.00001,
   seed=111,
   messages=[
       {
           "role": "system",
           "content": prompt_template.format(
               OPTIONS=options, INSTRUCTION=instruction
           ),
       },
       {
           "role": "user",
           "content": input_text,
       }
   ]
)
```
![img_8.png](/dont_trust_ai/posts/minimazing_randomness/img_8.png)

First call

![img_9.png](/dont_trust_ai/posts/minimazing_randomness/img_9.png)

Second call

![img_10.png](/dont_trust_ai/posts/minimazing_randomness/img_10.png)

Third call

## 4. Temperature and Top_p: Avoid Using Together

Both **temperature** and **top_p** control the randomness of the model’s responses, but in different ways:

- **Temperature**: This parameter controls the randomness in token selection by scaling the probability distribution. Lower values (e.g., `temperature = 0.1`) make the model more deterministic, while higher values (e.g., `temperature = 1.0`) increase diversity.

- **Top_p**: This parameter limits the set of tokens considered for selection based on their cumulative probability.

According to the documentation of both GPT and Claude, using **temperature** and **top_p** together can lead to unpredictable behavior and poor performance. When both are set simultaneously, the combined effect may confuse the model, leading to degraded reasoning abilities and lower-quality outputs. For example, using both parameters might significantly hamper tasks that require detailed reasoning, like multi-step logic or chain of thought processes.


## 5. Additional Information on **Temperature** and **n** Parameter
When you set the parameter **n** and the GPT-powered chat generated three responses for a single input, the behavior was as follows:
- With the **temperature** parameter set to 0, all three responses were identical. This is because the GPT model generated all three responses in the same system state with a constant **system fingerprint**. However, when you restarted the LLM call, the response would change due to a different fingerprint.
- On the other hand, when you set the **temperature** parameter to 0.15 and the **n** parameter to 3, the three generated responses for the same input were different. This indicates that with a constant **system fingerprint**, the **temperature** or **top_p** parameter is the only factor affecting the diversity of the generated responses.

**Example with temp = 0, n = 3:**

![img.png](/dont_trust_ai/posts/minimazing_randomness/img.png)

**Example with temp = 0.15, n=3:**

![img_1.png](/dont_trust_ai/posts/minimazing_randomness/img_1.png)

## Conclusion
Minimizing randomness in GPT responses is crucial in scenarios where consistency is needed, but true determinism remains elusive due to the **non-deterministic nature** of the model and variability in the **system_fingerprint**. By carefully controlling **temperature**, **seeds**, and **top_p** settings, you can reduce randomness, though you must be cautious about over-constraining the model, as it may degrade performance in complex tasks. Monitoring **system_fingerprint** changes is also key to distinguishing random variation from API backend updates, helping you manage LLM behavior more effectively.

In our view, improving prompts and instructions is main essential step in reducing randomness.  Another solution might be simplifying the input specification, by using additional LLM calls to extract only relevant data and removing unnecessary information, it would help to reduce hallucinations and prevent GPT from becoming confused. Unlike GPT, this issue is less critical in Claude. Since Claude manages large datasets effectively and consistently produces stable output, it makes sense to retain the current results. As for now, the main method to improve Claude’s accuracy is inserting into a prompt one or a few shotsvexamples selected through vector search based on the highest similarity. That can effectively improve accuracy without increasing complexity.

## References

1. [The “seed” option for GPT does not increase the determinism level](https://community.openai.com/t/the-seed-option-for-gpt-does-not-increase-the-determinism-level/512892)

2. [ChatCompletions are not deterministic even with seed set, temperature=0, top_p=0, n=1](https://community.openai.com/t/chatcompletions-are-not-deterministic-even-with-seed-set-temperature-0-top-p-0-n-1/685769)

3. [Determinism I: Understanding Randomness Within LLMs](https://neuralgap.io/understanding-randomness-within-llms-neuralgap/#:~:text=Layer%203%3A%20Beam%20Search%20with%20Randomness)
