+++
title = 'Differences in Prompting Techniques: Claude vs. GPT'
date = 2024-10-15T11:29:11+03:00
draft = false
author = 'Yaroslav Biziuk'
+++


# Differences in Prompting Techniques: Claude vs. GPT

## 1. Introduction

When working with language models (LLMs) like Claude and GPT, the effectiveness of prompts can vary significantly based on the model's architecture and capabilities. This article explores key differences in prompting strategies for Claude and GPT, using advanced techniques such as meta-prompting, XML tagging, and the Chain of Thoughts (CoT) method. By understanding these differences, users can optimize their prompts to enhance the accuracy and reliability of LLM outputs.

## 2. Context Window Size and Information Processing

One of the most significant differences between Claude and GPT lies in their **context window size** - the amount of text they can handle in a single prompt.

- **Claude** (`claude-3.5-sonnet`) can process up to **200,000 tokens**, making it ideal for tasks requiring the analysis of large documents or aggregating data from multiple sources. This is especially valuable in business and academic research, where Claude can process entire reports or research papers in one go. Due to this large capacity, prompts for Claude need to be clear and explicit to focus the model on relevant parts of the input.

- **GPT-4** (`gpt-4o-2024-08-06`) supports up to **128,000 tokens**. Although this is smaller than Claude’s window, it is still a significant improvement over previous models. GPT is suited for tasks involving moderate-length documents or well-defined queries.

For our specific testcase, with Stevens AI Chatbot, Claude's prompts in average have 9000 tokens per input and 600 tokens per output. For GPT, it’s 9000 tokens per input and 650 tokens per out, because of different token embeddings 

In practice, Claude’s larger context window means prompt engineering requires attention to chunking and summarizing within the input to make the most of its potential, while GPT might be better suited for more focused and precise tasks

## 3. Role of Examples and Instructions

Both models benefit from **examples** and **clear instructions**:

- **Claude**: [Examples play a central role](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting). For complex tasks, offering several examples that showcase the expected response pattern can significantly improve the output. It’s important to ensure that these examples are concise and relevant, avoiding unnecessary complexity. 
**Importantly**, examples have to be diverse in order not to tend LLM to the basis.

We provided our prompt with an example with an example of correctly resolving our Testcase-2 (1100-C). 

[**Example One-Shot Claude Prompt**:](https://docs.google.com/spreadsheets/d/1ql5LsHlODBEmA7Js9csNvWwkovHqSKe_sGw5wsoIJ8g/edit?gid=215193183#gid=215193183)
```xml
You are a Casework expert tasked with reviewing a specification and selecting the correct Series option that represents cabinet materials and thickness. 

Follow these instructions carefully:
1. Review the available Series options:
<options>
{OPTIONS}
</options>

2. Carefully read and understand the following instructions for selection:

{INSTRUCTION}

3. Examine the provided specification:
<specification>
SPECIFICATION_USER_INPUT
</specification>

4. After your analysis, provide your reasoning and selection in the following format:
   <thinking>
   [Include your step-by-step reasoning here]
   </thinking>
   
   <result>
   RESULT: [Insert selected Series option here]
   </result>

<example>
Specification: 
PART 2 - PRODUCTS
2.2 MATERIALS
General: Provide materials that comply with requirements of the AWI quality standard for each type of woodwork and quality grade specified, unless otherwise indicated.
Wood Products: Comply with the following:
Particleboard: ANSI A208.1, Grade M-2 M-2-Exterior Glue (at wet sink areas).
High-Pressure Decorative Laminate: NEMA LD 3, grades as indicated, or if not indicated, as required by woodwork quality standard.
Available Manufacturers: Subject to compliance with requirements, manufacturers offering high-pressure decorative laminates that may be incorporated into the Work include, but are not limited to, the following:

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

2.8 LAMINATE COUNTERTOPS
Quality Standard: Comply with AWI Section 400 requirements for high-pressure decorative laminate countertops.
Grade: Premium.
High-Pressure Decorative Laminate Grade: HGS.
Colors, Patterns, and Finishes: Provide materials and products that result in colors and textures of exposed laminate surfaces complying with the following requirements:
Provide Architect's selections from manufacturer's full range of colors and finishes in the following categories:
Solid colors.
Grain Direction: Parallel to cabinet fronts.
Edge Treatment: 3mm PVC. Color to match laminate.
Core Material at Sinks: Particleboard made with exterior glue, or exterior-grade plywood.

Answer:
<thinking>
Let's analyze the specification step-by-step:

1. Core Material Selection:
- The specification mentions "Particleboard: ANSI A208.1, Grade M-2 M-2-Exterior Glue (at wet sink areas)."
- There's no mention of NAUF or urea formaldehyde restrictions.
- Default to Industrial Particleboard CARB Compliant.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


6. Cabinet Edgebanding Selection:
- Not explicitly specified, default to Flat (.020") PVC Cabinet Edgebanding.

Based on these selections, we can narrow down our options to series that have:
- Industrial Particleboard CARB Compliant core
- HPL fronts and ends
- Square Flat Edge

The series that best matches these criteria is:
</thinking>

<result>
RESULT: 1100-C - Sq Flat Edge HPL Frts & HPL Ends IPB CARB Compliant Core
</result>
</example>

Remember to base your decision solely on the information provided in the specification, instruction, and available options.
Do not make assumptions or introduce external information.
```

#### Claude output:
![img.png](/dont_trust_ai/posts/difference_in_gpt_claude_prompting/img.png)

**Сonclusion**: LLM chose IPB Core Compliant and Sq Flat Edge, although previously she easily solved this test case (1200-NAUF), which means that one test case can form the basis to which the LLM will tend when making its answer. Therefore, according to the [Claude documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting#example-analyzing-customer-feedback), examples should be diverse.



[Example prompt with Few Shots](https://docs.google.com/spreadsheets/d/1ql5LsHlODBEmA7Js9csNvWwkovHqSKe_sGw5wsoIJ8g/edit?gid=723452655#gid=723452655). We provided our prompt with an example of correctly resolving our second test case (1100-C) with IPB Core Compliant and first (1200-N) with NAUF PB Core.

**Output**:
![img_1.png](/dont_trust_ai/posts/difference_in_gpt_claude_prompting/img_1.png)

![img_2.png](/dont_trust_ai/posts/difference_in_gpt_claude_prompting/img_2.png)

<div style="text-align: right;">
<a href="https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting#example-analyzing-customer-feedback">Claude documentation</a>
</div>

We asked Claude to evaluate our examples on relevance, diversity and clarity.

**Output**:
```xml
Certainly, I'd be happy to evaluate the examples for relevance, diversity, and clarity. Let me analyze each example:

Example 1:
This example is highly relevant as it demonstrates the process of analyzing a specification and selecting the appropriate Series option. It shows a clear step-by-step thought process, which is excellent for illustrating how to approach the task.

The example covers various aspects of cabinet construction, including core material, front and end materials, thickness, and edging. This diversity in the specification details helps to showcase how different elements are considered in the decision-making process.

The thinking process is clearly laid out, making it easy to follow the reasoning behind the final selection. The format, with separate <thinking> and <result> tags, is clear and consistent with the instructions.

Example 2:
This example is also relevant and provides a different set of specifications to analyze. It adds diversity to the set of examples by presenting a case where No Added Urea Formaldehyde (NAUF) core is specified, which wasn't a factor in the first example.

The specification in this example is more detailed and covers additional elements like hardware and accessories, countertops, and solid surface materials. This breadth of information tests the ability to focus on the relevant details for cabinet construction while filtering out extraneous information.

The thinking process is again clearly laid out, following the same format as the first example. This consistency aids in clarity and understanding.

Overall evaluation:
1. Relevance: Both examples are highly relevant to the task of analyzing specifications and selecting the appropriate Series option for cabinet construction.

2. Diversity: The examples provide good diversity in terms of the specifications presented. They cover different materials, construction details, and environmental considerations (NAUF vs. non-NAUF). This diversity helps to illustrate how the selection process can vary based on different requirements.

3. Clarity: Both examples are clear in their presentation. The step-by-step thinking process is well-articulated, making it easy to follow the reasoning. The consistent use of the <thinking> and <result> tags adds to the clarity.

Suggestion for improvement:
While these examples are strong, you could consider adding a third example that presents a more challenging or ambiguous case. This could help illustrate how to handle situations where the specification is less clear-cut or where there might be conflicting information to resolve. This would add another layer of complexity and further demonstrate the critical thinking skills required for this task.

```

###  Conclusion: 
Adding more solved test cases to the prompt boosts accuracy by providing more context, especially with few-shot methods like chain of thought, which improve reasoning. However, this approach becomes impractical due to high token costs.

Retrieval-Augmented Generation (RAG) offers a better solution. It retrieves relevant information from external sources, reducing the number of tokens in the prompt while maintaining accuracy and relevance. By using only the most important context, RAG optimizes performance without overloading the model with excessive token usage.
## 4. Meta-Prompting

Meta-prompting is a technique used to refine and enhance the performance of a prompt. For Claude LLM, meta-prompting can significantly improve prompt effectiveness. The [Claude documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator) recommends using the  "Generate a Prompt" feature that allows users to quickly create the first prompt or enhance their existing prompts. This functionality supports iterative improvements, helping to fine-tune prompts based on specific needs.

In contrast, meta-prompting for GPT has not shown substantial improvements in performance in our tests. Although this may be case-specific, it highlights a fundamental difference in how these models handle prompt enhancements

![img_3.png](/dont_trust_ai/posts/difference_in_gpt_claude_prompting/img_3.png)

<div style="text-align: right;">
<a href="https://console.anthropic.com/dashboard">Claude playground</a>
</div>

## 5. Formatting Prompts


The way prompts are formatted and segmented can affect the performance of LLMs. Claude’s documentation recommends using XML tags to separate parts of the prompt template or large prompts. This method has proven effective in practice, improving the results **significantly**.

For GPT, it is advised to specify the delimiter being used, such as “_You will be provided with a pair of articles (delimited with XML tags)._” This indicates a fundamental difference in how Claude and GPT handle prompt formatting.

![img_4.png](/dont_trust_ai/posts/difference_in_gpt_claude_prompting/img_4.png)
<div style="text-align: right;">
<a href="https://docs.google.com/spreadsheets/d/1jIxjzUWG-6xBVIa2ay6yDpLyeuOh_hR_ZB75a47KX_E/edit?gid=257656347#gid=257656347">Claude docs</a>
</div>

![img_5.png](/dont_trust_ai/posts/difference_in_gpt_claude_prompting/img_5.png)
<div style="text-align: right;">
<a href="https://platform.openai.com/docs/guides/prompt-engineering/strategy-write-clear-instructions">GPT docs</a>
</div>

- **Claude**: Claude benefits from using XML tags to separate parts of the prompt, improving results:

  ```xml
  <options>{OPTIONS}</options>
  
  <instruction>{INSTRUCTION}</instruction>
  
  <specification>{INPUT_TEXT}</specification>
  ```

- **GPT**: Prompt formatting should specify delimiters, but over-segmentation can reduce effectiveness:
  ```xml
  OPTIONS: 
  {OPTIONS}

  INSTRUCTION: 
  {INSTRUCTION}

  SPECIFICATION: 
  {INPUT_TEXT}
  ```
  **Example GPT (delimited with XML tags)**:
  ```xml
  You will be provided with a instruction, options, specification (delimited with XML tags): 
  <options>
     [OPTIONS]
  </options>
  
  <instruction>
     [INSTRUCTION]
  </instruction>
  
  <specification>
     [INPUT_TEXT]
  </specification>
  ```

## 6. System and User Input Separation

GPT and Claude’s performance improves when system prompts and user inputs are separated, enabling the model to process information more effectively. For example, the system prompt can provide specific instructions, while the user input is handled independently.

- **Example**:
  ```json
  messages=[
      {
          "role": "system",
          "content": prompt_template.format(
              OPTIONS=options, INSTRUCTION=instruction,
          ),
      },
      {
          "role": "user",
          "content": input_text,
      },
  ]
  ```

Additionally, it was observed that when **XML tags** were used to separate user input for Claude, it actually led to **worse results**. Specifically, tagging inputs separately (e.g., encapsulating user input within XML tags) made it harder for Claude to generate meaningful responses, likely due to how the model parses structured inputs compared to plain text. This finding highlights the importance of avoiding unnecessary formatting structures like XML tags when separating inputs for Claude.

#### Example Prompt for Claude:

```xml
You are a Casework expert tasked with reviewing a specification and selecting the correct Series option that represents cabinet materials and thickness. Follow these instructions carefully:

1. Review the available Series options:
<options>
{OPTIONS}
</options>

2. Carefully read and understand the following instructions for selection:
{INSTRUCTION}

3. Examine the provided specification:
<specification>
SPECIFICATION_USER_INPUT
</specification>

4. After your analysis, provide your reasoning and selection in the following format:
   <thinking>
   [Include your step-by-step reasoning here]
   </thinking>

   <result>
   RESULT: [Insert selected Series option here]
   </result>

Remember to base your decision solely on the information provided in the specification, instruction, and available options.
Do not make assumptions or introduce external information.
```

#### Worse Results:
```python
messages = [
    {
        "role": "system",
        "content": prompt_template.format(
            OPTIONS=options, INSTRUCTION=instruction,
        ),
    },
    {
        "role": "user",
        "content": f"<specification>{input_text}<specification/>",
    },
]
```

#### Better Results:
```python
messages = [
    {
        "role": "system",
        "content": prompt_template.format(
            OPTIONS=options, INSTRUCTION=instruction,
        ),
    },
    {
        "role": "user",
        "content": input_text,
    },
]
```

## 7. Chain of Thoughts (CoT) Technique

The Chain of Thoughts (CoT) technique is essential for guiding LLMs through complex instructions by encouraging them to think step-by-step. For Claude, it is recommended to use XML tags to designate where the model should include its reasoning. This structured approach helps Claude organize its thoughts and produce coherent outputs.

For GPT, a simpler approach of instructing the model to "think step by step" or "take your time" is often sufficient. This technique encourages GPT to consider each step in the process but does not require the specific tagging used in Claude.

#### Example for Claude:
```xml
<thinking>
   [Include your step-by-step reasoning here]
</thinking>
```

**Output:**
```xml
<thinking>
Let's analyze the specification step-by-step:

1. Core Material Selection:
   - The specification mentions "Particleboard: ANSI A208.1, Grade M-2 M-2-Exterior Glue (at wet sink areas)."
   - There's no mention of NAUF or urea formaldehyde restrictions.
   - Default to Industrial Particleboard CARB Compliant.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

4. Ends Material Selection:
 - The specification states "Bottoms and Ends of Cabinets, and Tops of Wall Cabinets and Tall Cabinets: 3/4-inch particleboard, plastic-laminate faced on exposed surfaces, thermoset decorative panels on semiexposed surfaces"
 - This indicates we should select High Pressure Laminate (HPL) for the ends

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  
Based on these selections, we can narrow down our options to series that have:
- Industrial Particleboard CARB Compliant core
- HPL fronts and ends
- Square Flat Edge

The series that best matches these criteria is:
</thinking>

<result>
RESULT: 1200-N - 3mm HPL Frts & HPL Ends NAUF PB Core
</result>
```

#### Example for GPT:
```python
You think step by step. Take your time to answer.
```

**Output:**

```xml
### Step-by-Step Analysis:

#### 1. Material Requirements:
- **Core Material**: The specification mentions that adhesives should not contain urea formaldehyde. Therefore, we should select NAUF (No Added Urea Formaldehyde) Particleboard.
- **Fronts Material**: The specification requires high-pressure decorative laminate (HPL) for exposed surfaces.
- **Fronts Thickness**: The specification mentions GP-50 (0.050-inch nominal thickness) for horizontal surfaces and GP-28 (0.028-inch nominal thickness) for vertical surfaces. However, for the fronts, we will consider the standard thickness options provided in the series.
- **Ends Material**: The ends should match the fronts, which is HPL.
- **Fronts Edging**: The specification does not allow PVC edging, so we should look for options without PVC edging.
- **Cabinet Edgebanding**: The specification does not allow PVC edging, so we should look for options without PVC edging.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

### Step 3: Fronts Material Selection
- The specification states that door and drawer fronts must be matching high pressure laminate (HPL) on both sides.
- Therefore, the fronts material should be High Pressure Laminate (HPL).

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#### 7. Cabinet Edgebanding Selection:
- **Selected Cabinet Edgebanding**: Since PVC edging is not allowed, we should look for options without PVC edging.

### Final Review:
- **Core Material**: NAUF PB Core.
- **Fronts Material**: 3mm High Pressure Laminate (HPL).
- **Ends Material**: 3mm High Pressure Laminate (HPL).
- **Fronts Edging**: 3mm Radius Edge.
- **Cabinet Edgebanding**: Options without PVC edging.

Based on the steps and the filtered options, the correct series option is:

**RESULT: 1200-N - 3mm HPL Frts & HPL Ends NAUF PB Core**
```

## 8. Decomposing Complex Tasks in GPT: A Recommended Approach

One of the key recommendations in the GPT documentation is to decompose complex tasks into simpler, more manageable steps. This method significantly enhances performance and reduces the likelihood of the model making mistakes by handling more digestible components of a task one by one. GPT excels when provided with specific instructions in a sequence, allowing it to focus on a single objective at a time.

For example, when working on determining the correct Series option that represents cabinet materials and thickness from a PDF document, a sequence of chain-of-calls (or sequential prompts) could simplify the task. This approach reduces cognitive overload for the model, ensuring more accurate and reliable outputs.

### Here’s how this decomposition would look:
- **First prompt**: Extract all relevant information about cabinet materials and thickness from the provided document.  
  *This step isolates data extraction from interpretation, ensuring GPT focuses solely on identifying and retrieving the relevant details.*

- **Second prompt**: Based on the extracted information, determine the correct Series option that represents the cabinet materials and thickness using the provided instructions.  
  *Here, the model is now tasked with processing the extracted data, interpreting it according to specific criteria, and generating a decision.*

By breaking down the task into these two steps, we reduce the complexity for the model, minimizing the chances of misinterpretation or errors. This method also makes it easier to troubleshoot and refine individual steps, should the need arise.

#### Example on Claude:
![img_6.png](/dont_trust_ai/posts/difference_in_gpt_claude_prompting/img_6.png)

#### Example GPT:
![img_8.png](/dont_trust_ai/posts/difference_in_gpt_claude_prompting/img_8.png)

In general, this strategy of decomposing tasks into smaller, sequential prompts is especially useful in GPT’s chain of thought framework, where the model benefits from clear and distinct steps. When a PDF file is loaded into GPT for processing, the pricing is calculated based on the total word count of the entire PDF, which can become expensive, especially with large documents. But in my opinion, this method is one of the best ways to minimize hallucinations, and make the model's responses more deterministic by extracting relevant sections before submitting them to another prompt to GPT. This strategy allows for a focused query, ensuring the model processes only the necessary information, leading to more reliable answers. However, in our specific test case, it might be more cost-efficient to develop an algorithm that automatically identifies and extracts only "Part 2 products," instead of processing the entire document with GPT, making it a cheaper and more targeted solution.

### 9. Roleplay Models vs. GPT: Following Instructions and Logical Compliance

Roleplay models like Claude are more rigid in following instructions, making them ideal for tasks requiring strict adherence to step-by-step guidelines. In contrast, GPT models often rely on their own internal logic, which can lead to creative and effective problem-solving but may deviate from precise instructions. This flexibility is beneficial for open-ended tasks but requires additional review when strict accuracy is needed.

From our experience with Claude and GPT on similar prompts, we observe that Claude tends to follow a more structured, step-by-step approach to instructions, while GPT’s outputs often involve more improvisation, making it necessary to monitor tasks for precise compliance.

### TESTCASE-3 (2800-C 3mm Frts & TF Color Throughout IPB CARB Compliant Core)

#### GPT OUTPUT:

```xml
Let's follow the steps outlined in the instructions to determine the correct series option.

### Step 1: Material Requirements
- The specification mentions that the basis for the specification is Stevens Advantage 2800 Designer Series.

### Step 2: Core Material Selection
- The core material should be Industrial Particleboard CARB Compliant unless adhesives with urea formaldehyde are prohibited.
- There is no mention of prohibiting adhesives with urea formaldehyde, so we will use Industrial Particleboard CARB Compliant.

### Step 3: Fronts Material Selection
- The specification states that door and drawer fronts must be matching high pressure laminate (HPL) on both sides.
- Therefore, the fronts material should be High Pressure Laminate (HPL).

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

### Step 7: Cabinet Edgebanding Selection
- The specification states that cabinet sides, top, bottom, adjustable shelves, and other interior components shall be edged with (.020") flat edge extrusion.
- Therefore, the cabinet edgebanding style should be Flat (.020") PVC Cabinet Edgebanding.

### Step 8: Final Review
- Ensure all selections are compatible with each other.
- Verify that all requirements from the original specification have been addressed.

Based on the above steps, the correct series option is:

**RESULT: 2800-C - 3mm Frts & TF Color Throughout IPB CARB Compliant Core**
```


Here **GPT**’s outputs involved more improvisation, looking through documentations, it incorrectly determined the HPL for fronts material, but chose 2800-C, because found the sentence “_the basis for the specification is Stevens Advantage 2800 Designer Series_”. **Claude** adheres to the instructions more strictly and rarely uses such tricks.

## 10. Conclusion
In summary, the differences between **Claude** and **GPT** in terms of prompt engineering highlight the importance of understanding each model's strengths and limitations. **Claude** excels in handling large context windows, making it suitable for processing extensive documents and generating detailed responses, while **GPT** shines in more focused tasks, particularly when instructions are clear and precise.

When constructing prompts, **Claude** benefits from separated system and user inputs and XML-based formatting, while **GPT** works best when instructions are combined in a single, well-structured prompt without unnecessary formatting. **The Chain of Thought (CoT)** technique and task decomposition are highly recommended for both models but are executed slightly differently. GPT, for instance, performs better when complex tasks are broken down into simpler, sequential steps, which enhances clarity and reduces errors.
Ultimately, prompt engineering is about leveraging the specific capabilities of each model to improve task efficiency and accuracy. By tailoring your approach to the strengths of **Claude** or **GPT**, you can maximize the potential of each model to achieve high-quality results.

## 11. References

[**Claude Prompting Guide**](https://docs.google.com/spreadsheets/d/1jIxjzUWG-6xBVIa2ay6yDpLyeuOh_hR_ZB75a47KX_E/edit?gid=869808629#gid=869808629)

[**GPT Prompting Guide**](https://platform.openai.com/docs/guides/prompt-engineering)
