+++
title = 'Experiments with Different LLMs'
date = 2024-10-11T14:06:39+03:00
draft = false
author = "Yaroslav Biziuk"
+++

In this series of tests, we conducted experiments with various large language models (LLMs) to assess their ability to follow complex instructions, reason through problems, and handle multi-step tasks. Below is a summary of the models tested, the outputs they produced, and a brief evaluation of their performance.

## 1. MythoMax 13B (Nitro)
- **Code**: `gryphe/mythomax-l2-13b:nitro`
- **Description**: MythoMax is a popular fine-tune of Llama 2 13B, known for its descriptive output and roleplay capabilities. However, its performance in reasoning-based tasks is underwhelming.

### Results:
- **GPT prompt output**: 
![img.png](/dont_trust_ai/posts/experiments_with_different_llms/img.png)
- **Claude prompt output**: 
![img_1.png](/dont_trust_ai/posts/experiments_with_different_llms/img_1.png)
- **Conclusion**: MythoMax provided unsatisfactory results, failing to engage in any meaningful chain of thought (CoT) reasoning and producing very short, incomplete answers.

---

## 2. Reflection 70B (Free)
- **Code**: `mattshumer/reflection-70b:free`
- **Description**: This model, based on Llama 3.1 70B, uses a unique "Reflection-Tuning" technique to detect and correct mistakes in reasoning. It was trained on synthetic data.

### Results:
- **GPT prompt output**: 
![img_2.png](/dont_trust_ai/posts/experiments_with_different_llms/img_2.png)
### Testcase 3 Detail GPT resolving:
- **Output**:
  ```xml
    <thinking>
    To solve this problem, I'll follow these steps:
    Identify key information in the specification related to cabinet materials and thickness.
    Compare this information to the criteria outlined in the instruction.
    Match the identified information with the available Series options.
    Eliminate options that do not meet the criteria.
    Select the most appropriate Series option based on the analysis.
    Let's go through this process:
    Key information from the specification:
    Cabinet ends: 3/4" thick
    Cabinet backs: 1/4" prefinished Medium Density Fiberboard (MDF)
    Adjustable shelves: 3/4" thick
    Drawer members: 3/4" thick
    Drawer bottoms: 1/4" MDF
    Comparing to the instruction criteria:
    The instruction asks for a Series option that represents cabinet materials and thickness. We need to focus on the thickness of the cabinet ends and the material of the cabinet backs.
    Matching with available Series options:
    Looking at the options, we can see that most of them have:
    Ends: High Pressure Laminate (HPL) or Thermally Fused Laminate (TF)
    Core: Industrial Particleboard (IPB) or No Added Urea Formaldehyde Particleboard (NAUF PB)
    Edgebanding: Flat (.020") PVC Cabinet Edgebanding
    None of the options explicitly mention 3/4" thickness for ends or 1/4" MDF for backs. However, we need to find the closest match.
    Eliminating options:
    We can eliminate options that don't match the general criteria:
    Series 1600-C and 1600-N can be eliminated as they have wood veneer fronts, which is not mentioned in the specification.
    Series 1100-C, 1100-N, 1150-C, and 1150-N can be eliminated as they have square flat edge HPL fronts, which doesn't match the 3mm radius edge mentioned in the specification.
    Selecting the most appropriate option:
    After elimination, we're left with Series 1200-C, 1200-N, 1250-C, and 1250-N. These all have 3mm HPL fronts and 3mm radius edges, which seems to be the closest match to the specification.
    Among these, Series 1200-C and 1200-N have HPL ends, while Series 1250-C and 1250-N have TF ends. The specification doesn't explicitly mention the type of ends, so we can't make a distinction based on this.
    The main difference between these options is the core material:
    Series 1200-C and 1250-C have Industrial Particleboard (IPB) CARB Compliant Core
    Series 1200-N and 1250-N have No Added Urea Formaldehyde Particleboard (NAUF PB) Core
    The specification doesn't mention CARB compliance or NAUF, so we can't make a decision based on this.
    <reflection>
    Upon reflection, I realize that I may have been too quick to eliminate the 1600 series options. While they do have wood veneer fronts, the specification doesn't explicitly rule out wood veneer. Additionally, these options have 3mm wood edges, which could be considered similar to the 3mm radius edge mentioned in the specification. Let's reconsider these options.
    </reflection>
    Reconsidering the 1600 series options:
    Series 1600-C and 1600-N have wood veneer fronts with 3mm wood edges, which could be seen as similar to the 3mm radius edge mentioned in the specification.
    They also have HPL ends, which is consistent with the specification's mention of 3/4" thick ends (though the exact thickness isn't specified in the options).
    The core material is IPB CARB Compliant Core for 1600-C and NAUF PB Core for 1600-N, which is similar to the other options.
    Given this new consideration, Series 1600-C and 1600-N seem to be strong contenders. They match the 3mm edge requirement and have HPL ends, which is closer to the 3/4" thickness mentioned in the specification than the other options.
    <reflection>
    After this reflection, I believe Series 1600-C or 1600-N would be the best choice. They match the 3mm edge requirement and have HPL ends, which is closer to the 3/4" thickness mentioned in the specification than the other options. The wood veneer fronts could be seen as a minor deviation from the exact specification, but it's the closest match overall.
    </reflection> </thinking> <output>
    Based on the analysis of the specification and the available Series options, the most appropriate Series option that represents cabinet materials and thickness is either Series 1600-C or Series 1600-N.
    These options stand out for several reasons:
    Edge style: Both Series 1600-C and 1600-N have a 3mm radius wood edge, which closely matches the 3mm radius edge mentioned in the specification.
    End material: They have HPL (High Pressure Laminate) ends, which is consistent with the specification's mention of 3/4" thick ends. While the exact thickness isn't specified in the options, HPL ends are a closer match to the 3/4" thickness requirement than the other options.
    Core material: Both options have a particleboard core, with Series 1600-C having an Industrial Particleboard (IPB) CARB Compliant Core and Series 1600-N having a No Added Urea Formaldehyde Particleboard (NAUF PB) Core. This is similar to the core materials mentioned in the other options.
    Overall construction: The wood veneer fronts with 3mm wood edges in these options could be seen as a minor deviation from the exact specification, but they provide a strong and durable construction that aligns with the overall quality implied in the specification.
    While the other options (Series 1200-C, 1200-N, 1250-C, and 1250-N) have 3mm HPL fronts and 3mm radius edges, they don't match the end thickness requirement as closely as the 1600 series options. The 1100 and 1150 series options can be eliminated due to their square flat edge HPL fronts, which don't match the 3mm radius edge mentioned in the specification.
    Therefore, between Series 1600-C and 1600-N, the choice would depend on whether CARB compliance (1600-C) or NAUF (1600-N) is preferred or required for the project. Both options represent the cabinet materials and thickness most closely based on the provided specification and available Series options.
    </output>
    ```
**Expected Response**: 2800-C - 3mm Frts & TF Color Throughout IPB CARB Compliant Core
  
- **Result**: Reflection LLMs aim to explain each step of the instructions comprehensively but face significant challenges in executing nearly every step. This difficulty might stem from the specific synthetic data on which the model was trained. Despite its structured approach, the model often fails to accurately address key details outlined in the instructions. Notably, the model exhibits high determinism, consistently providing the same result across multiple prompts with zero temperature. 

### Claude prompt output:
![img_3.png](/dont_trust_ai/posts/experiments_with_different_llms/img_3.png)

### Testcase 1 Detail Claude resolving:
- **Output**:
```xml
<thinking>
To solve this problem, I'll follow these steps:
Analyze the specification to identify key information about cabinet materials and thickness.
Compare this information with the criteria in the instruction.
Match the identified information with the available Series options.
Eliminate options that don't meet the criteria.
Select the most appropriate Series option.
Let's go through this process:
Analyzing the specification:
Cabinet construction: Particleboard, plywood, hardwood lumber, or high-density fiber board.
Thickness: Minimum 1/2-inch for sides, back, and sub-front of drawers.
Bottoms: Minimum 1/4-inch tempered hardboard.
Drawer bottoms: Minimum 1/2-inch thick particleboard.
Comparing with the instruction criteria:
The instruction asks for a Series option that represents cabinet materials and thickness.
We need to find an option that matches the materials and thicknesses specified.
Matching with available Series options:
The options mention various materials like HPL (High Pressure Laminate), TF (Thermally Fused Laminate), and wood veneer.
Thicknesses mentioned include 3mm (which is approximately 1/8 inch) and no specific thickness for wood veneer.
Eliminating options:
Options with 3mm thickness (1100-C, 1100-N, 1150-C, 1150-N, 1200-C, 1200-N, 1250-C, 1250-N) can be eliminated as they don't meet the minimum 1/2-inch thickness requirement.
Options with HPL or TF for all parts (1100-C, 1100-N, 1150-C, 1150-N, 1200-C, 1200-N, 1250-C, 1250-N) can be eliminated as they don't match the variety of materials specified in the instruction.
Selecting the most appropriate option:
The only option that remains is 1600-C or 1600-N, as they are the only ones that mention wood veneer and have a 3mm wood edge, which could potentially meet the thickness requirement.
<reflection>
Upon reflection, I realize that I may have been too hasty in eliminating the 3mm options. The specification mentions a minimum 1/2-inch thickness for some parts, but not all. The 3mm thickness could potentially apply to certain components. However, the main issue is that none of the 3mm options mention the variety of materials specified in the instruction. The 1600-C and 1600-N options are still the most likely candidates as they mention wood veneer and have a 3mm wood edge, which could meet the thickness requirement for some parts.
</reflection>
After careful consideration, the most appropriate Series option appears to be either 1600-C or 1600-N. Both of these options mention wood veneer with a 3mm wood edge, which could potentially meet the thickness requirement for some parts of the cabinet. They also mention HPL for the ends, which aligns with the variety of materials specified in the instruction.
</thinking> <output>
Based on the analysis of the specification and the available Series options, the most appropriate Series option that represents cabinet materials and thickness is either 1600-C or 1600-N.
These options are the best match for several reasons:
Material variety: They mention wood veneer for the fronts, which aligns with the specification's mention of various materials including wood veneer.
Thickness: While the specification mentions a minimum 1/2-inch thickness for some parts, the 3mm wood edge mentioned in these options could potentially meet this requirement for certain components.
Core material: Both options mention Industrial Particleboard CARB Compliant Core (1600-C) or No Added Urea Formaldehyde Particleboard (1600-N), which aligns with the specification's mention of particleboard as a possible material.
Edge style: The 3mm Radius Wood Edge mentioned in these options could potentially meet the thickness requirement for some parts of the cabinet.
Overall construction: These options seem to offer a more comprehensive construction method that could accommodate the various materials and thicknesses specified in the instruction.
It's important to note that while these options are the best match, they don't perfectly align with all aspects of the specification. The specification mentions a minimum 1/2-inch thickness for some parts, which is not explicitly stated in these options. However, given the available choices, 1600-C or 1600-N appear to be the most suitable options for representing cabinet materials and thickness as specified in the instruction.</output>
```
**Expected Response**: 1200-N - 3mm HPL Frts & HPL Ends NAUF PB Core

- **Result**: Reflection LLM follows the prompt structure closely, striving to execute every step of the provided instructions and guidelines. However, it often struggles with selecting the right keywords and sentences from specification and has difficulty identifying the key elements to focus on when analyzing the cabinet specification.
 
## 3. Meta: Llama 3.1 8B Instruct (Free)
- **Code**: `meta-llama/llama-3.1-8b-instruct:free`
- **Description**: Meta's Llama 3.1 series includes instruct-tuned versions aimed at high-efficiency tasks. The 8B variant is fast but falls short on more complex problem-solving tasks.

### Results:
- **GPT prompt output**: 
![img_4.png](/dont_trust_ai/posts/experiments_with_different_llms/img_4.png)
- **Claude prompt output**: 
![img_5.png](/dont_trust_ai/posts/experiments_with_different_llms/img_5.png)

- **Conclusion**: The LLaMA 3.1 8B model tends to provide very brief and short responses and struggles with effectively utilizing the "chain of thought" technique, often making non-transparent decisions that can be difficult to follow. Also LlaMA 3.1 8B has very low determinism and very often writes different solutions for the same test case.

---

## 4. Meta: Llama 3.1 405B Instruct
- **Code**: `meta-llama/llama-3.1-405b-instruct`
- **Description**: A highly anticipated 405B Llama model designed for dialogue use cases and long context processing (128k tokens). It performs well on structured dialogue tasks.

### Results:
- **GPT prompt output**: 
![img_6.png](/dont_trust_ai/posts/experiments_with_different_llms/img_6.png)
- **Claude prompt output**: 
![img_7.png](/dont_trust_ai/posts/experiments_with_different_llms/img_7.png)
- **Conclusion**: Although LLaMA 405B showcased good problem-solving structure, it was outperformed by models like GPT and Claude in terms of accuracy, especially with complex multi-step tasks.

---

## 5. Anthropic: Claude 3.5 Sonnet (Self-Moderated)
- **Code**: `anthropic/claude-3.5-sonnet:beta`
- **Description**: A self-moderated version of Claude, designed to execute complex multi-step instructions with precision and consistency.

### Results:
- **Claude prompt output**: 
![img_8.png](/dont_trust_ai/posts/experiments_with_different_llms/img_8.png)
 
### TestCase 8 resolving:
- **Output**:
  ```xml
  TESTCASE - 8 OUTPUT of Claude-3-opus:
    <thinking>
    1. Core Material Selection:
    The specification mentions particleboard core materials with a minimum density of 45-48 lb, tested under ANSI A 208.1 and/or ASTM D-1037-91A standards. It does not explicitly prohibit adhesives containing urea formaldehyde. Therefore, I will select Industrial Particleboard CARB Compliant as the core material.
    2. Fronts Material Selection:
    The specification states that door and drawer fronts must be matching high pressure laminate on both sides. Therefore, I will select 3mm High Pressure Laminate as the fronts material.
    3. Fronts Thickness Determination:
    The specification mentions that door and drawer fronts shall be 3/4" thick. This aligns with the standard thickness for 3mm High Pressure Laminate fronts.
    4. Ends Material Selection:
    The specification does not explicitly mention the material for cabinet ends. However, it states that all exposed/semi-exposed surfaces shall be color matching thermofused or high pressure laminate. Since the fronts are specified as HPL, I will select High Pressure Laminate as the ends material to maintain consistency.
    5. Fronts Edging Selection:
    The specification clearly states that door and drawer front edges shall have 3mm radius extrusion banding. Therefore, I will select 3mm Radius Edge as the fronts edging style.
    6. Cabinet Edgebanding Selection:
    The specification mentions that cabinet sides, top, bottom, adjustable shelves, and other interior components shall be edged with (.020") flat edge extrusion. This matches the default option of Flat (.020") PVC Cabinet Edgebanding.
    Based on the provided specification and the selection criteria, the most appropriate Series option is:
    5120-C - 3mm HPL Frts & Ends IPB CARB Compliant Core
    </thinking>
    
    <result>
    RESULT: 5120-C - 3mm HPL Frts & Ends IPB CARB Compliant Core
    </result>

  ```
**Expected Response**:  1250-C - 3mm HPL Frts & TF Ends IPB CARB Compliant Core

- **Conclusion**: Claude 3.5 Sonnet delivered highly accurate results with a structured, step-by-step process, excelling at complex tasks. It also exhibited a high level of determinism, consistently producing the same output across multiple prompts.

### Note
- **Pricing for claude-3.5-sonnet:**

![img_9.png](/dont_trust_ai/posts/experiments_with_different_llms/img_9.png)

_Cost for 9 test cases:_ **0.32 $** | _Average cost for 1 testcase:_ **0.036 $**

- **For example pricing for gpt-4o-2024-05-13:**

![img_10.png](/dont_trust_ai/posts/experiments_with_different_llms/img_10.png)

_Cost for 9 test cases:_ **0.41 $** | _Average cost for 1 testcase:_ **0.046 $**


---

## 6. Qwen 2 72B Instruct
- **Code**: `qwen/qwen-2-72b-instruct`
- **Description**: This model from the Qwen family handled GPT-based prompts with impressive accuracy, completing most tasks successfully.

### Results:
- **GPT prompt output**: 
![img_11.png](/dont_trust_ai/posts/experiments_with_different_llms/img_11.png)
- **Claude prompt output**: 
![img_12.png](/dont_trust_ai/posts/experiments_with_different_llms/img_12.png)

### TestCase 3 resolving:
- **Output**: 

```xml
Justification:
1. Core Material Selection: The specification mentions particleboard core materials with a minimum density of 45-48 lb. Since there's no mention of adhesives containing urea formaldehyde, we default to ""Industrial Particleboard CARB Compliant.""
2. Fronts Material Selection: The specification requires door and drawer fronts to be finished entirely in matching high pressure laminate (HPL) materials on both the fronts and backs. The rest of the exposed/semi-exposed cabinet components can be either color matching thermofused (TFL) or matching HPL. Since the fronts must be HPL, we select ""3mm High Pressure Laminate.""
3. Fronts Thickness Determination: The specification indicates that door and drawer fronts shall be 3/4"" thick. This corresponds to the ""3mm"" thickness option for fronts.
4. Ends Material Selection: The specification allows for either color matching TFL or matching HPL for the rest of the exposed/semi-exposed cabinet components. Since we have already selected HPL for the fronts, we default to HPL for the ends.
5. Fronts Edging Selection: The specification requires 3mm radius extrusion banding for door and drawer fronts. This corresponds to the ""3mm Radius Edge"" style.
6. Cabinet Edgebanding Selection: The specification requires (.020"") flat edge extrusion for cabinet sides, top, bottom, adjustable shelves, and other interior components. This corresponds to the ""Flat (.020\"") PVC Cabinet Edgebanding"" option.

The ""2800-C - 3mm Frts & TF Color Throughout IPB CARB Compliant Core"" series matches all the requirements specified in the input text. It features a 3mm High Pressure Laminate for fronts, matching High Pressure Laminate for ends, an Industrial Particleboard CARB Compliant core, and a 3mm Radius Edge style for the fronts, with Flat (.020\"") PVC Cabinet Edgebanding for the cabinet edges.
```

- **Pricing for  qwen/qwen-2-72b-instruct:**

![img_13.png](/dont_trust_ai/posts/experiments_with_different_llms/img_13.png)

_Cost for 9 test cases:_ **0.04 $** | _Average cost for 1 testcase:_ **0.0045 $**

- **Conclusion**: Qwen 2 72B Instruct demonstrated solid performance, successfully completing 8 out of 9 tasks. It also maintained a relatively low cost per test case, making it a highly efficient choice.

With a cost of **$0.35/M** input tokens and **$0.4/M** output tokens (**0.04 $** for 9 test cases), Qwen-2-72B  presents itself as a viable option for further testing, when:
- **gpt-4o-2024-08-06** $2.5/M input and $10/M output (0.21 $ for 9 test cases)
- **gpt-4o-2024-05-13** $5/M input and $10/M output (0.40 $ for 9 test cases)
- **claude-3.5-sonnet** $3/M input and $15/M output (0.32 $ for 9 test cases)
---

