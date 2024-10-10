import logging
import deepeval

from time import time
from uuid import UUID
from json import JSONDecodeError
from deepeval.tracing import Tracer, TraceType, LlmAttributes
from openai import APIError, AsyncClient
from openai.types.chat import ChatCompletion
from langsmith import traceable, get_current_run_tree
from langsmith.wrappers import wrap_openai

from utils import calculate_llm_call_cost, get_openai_client


async def base_llm_call(
    client: AsyncClient,
    prompt_template: str,
    llm_model: str,
    options: str,
    instruction: str,
    input_text: str,
) -> ChatCompletion:
    """
    Base LLM call that generates responses from the model based on input data.

    Args:
        client (AsyncClient): OpenAI client.
        prompt_template (str): Template for the system message.
        llm_model (str): Name of the LLM model to call.
        options (str): Additional options for the request.
        instruction (str): Instructions to the model.
        input_text (str): Specification of cabinet input text passed to the model.

    Returns:
        ChatCompletion: Response from the model.
    """
    return await client.chat.completions.create(
        model=llm_model,
        temperature=0,
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
            },
        ],
    )


async def llm_call_with_logging_and_cost_calculating(
    client: AsyncClient,
    prompt_template: str,
    llm_model: str,
    options: str,
    instruction: str,
    input_text: str,
    index_of_testcase: str | None = None,
) -> tuple[str, str, float, float]:
    """
    LLM call with logging and cost calculation.

    Args:
        client (AsyncClient): OpenAI client.
        prompt_template (str): Template for the system message.
        llm_model (str): Name of the LLM model to call.
        options (str): Additional options for the request.
        instruction (str): Instructions to the model.
        input_text (str): Specification of cabinet input text passed to the model.
        index_of_testcase (str): Index of the test case.

    Returns:
        tuple: Test case index, LLM response, completion time, and total cost.
    """
    logging.info(f"🟡 TESTCASE-{index_of_testcase}: Sending request to {llm_model}")

    start_time = time()

    try:
        completion = await base_llm_call(
            client=client,
            prompt_template=prompt_template,
            llm_model=llm_model,
            options=options,
            instruction=instruction,
            input_text=input_text,
        )
    except (APIError, JSONDecodeError) as e:
        logging.exception(e)
        return index_of_testcase, f":red[Caught an ERROR: {e}]", 0.0, 0.0

    completion_time = time() - start_time
    llm_response = completion.choices[0].message.content

    token_usage = completion.model_dump().get("usage", {})
    input_tokens = token_usage.get("prompt_tokens", 0)
    output_tokens = token_usage.get("completion_tokens", 0)
    total_cost = calculate_llm_call_cost(llm_model, input_tokens, output_tokens)

    logging.info(
        f"✅ TESTCASE-{index_of_testcase}: Received LLM response in {completion_time:.2f}s"
    )
    logging.info(
        f"🟢 Cost: {total_cost:.4f}$ | Input tokens: {input_tokens}, Output tokens: {output_tokens}"
    )

    return index_of_testcase, llm_response, completion_time, total_cost


async def call_llm_with_deepeval_monitoring(
    prompt_template: str,
    llm_model: str,
    options: str,
    instruction: str,
    input_text: str,
    index_of_testcase: str | None = None,
) -> tuple[str, str, float, float, str]:
    """
    LLM call with logging, cost calculation, and sending data to deepeval for monitoring.

    Args:
        prompt_template (str): Template for the system message.
        llm_model (str): Name of the LLM model to call.
        options (str): Additional options for the request.
        instruction (str): Instructions to the model.
        input_text (str): Specification of cabinet input text passed to the model.
        index_of_testcase (str): Index of the test case.

    Returns:
        tuple: Test case index, LLM response, deepeval monitoring ID.
    """
    client = get_openai_client()
    with Tracer(trace_type=TraceType.LLM) as llm_trace:
        index_of_testcase, llm_response, completion_time, total_cost = (
            await llm_call_with_logging_and_cost_calculating(
                client=client,
                llm_model=llm_model,
                prompt_template=prompt_template,
                instruction=instruction,
                options=options,
                input_text=input_text,
                index_of_testcase=index_of_testcase,
            )
        )
        attributes = LlmAttributes(
            input_str=input_text,
            output_str=llm_response,
            model=llm_model,
            total_cost=total_cost
        )
        llm_trace.set_attributes(attributes)

    response_id = deepeval.monitor(
        event_name="Stevens Agent",
        model=llm_model,
        input=input_text,
        response=llm_response,
        token_cost=total_cost,
        completion_time=completion_time,
    )

    return index_of_testcase, llm_response, completion_time, total_cost, response_id


@traceable
async def call_llm_with_langsmith_monitoring(
    prompt_template: str,
    llm_model: str,
    options: str,
    instruction: str,
    input_text: str,
    index_of_testcase: str | None = None,
) -> tuple[str, str, float, float, UUID]:
    """
    LLM call with LangSmith monitoring.

    Args:
        prompt_template (str): Template for the system message.
        llm_model (str): Name of the LLM model to call.
        options (str): Additional options for the request.
        instruction (str): Instructions to the model.
        input_text (str): Specification of cabinet input text passed to the model.
        index_of_testcase (str): Index of the test case.

    Returns:
        tuple: Test case index, LLM response, completion time, and total cost.
    """
    client = wrap_openai(get_openai_client())
    index_of_testcase, llm_response, completion_time, total_cost = (
        await llm_call_with_logging_and_cost_calculating(
            client=client,
            prompt_template=prompt_template,
            llm_model=llm_model,
            options=options,
            instruction=instruction,
            input_text=input_text,
            index_of_testcase=index_of_testcase,
        )
    )
    run = get_current_run_tree()

    return index_of_testcase, llm_response, completion_time, total_cost, run.id
