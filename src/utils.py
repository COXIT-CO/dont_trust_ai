import asyncio

from openai import AsyncOpenAI

from config import PRICES_PER_1000_TOKEN, OPENROUTER_BASE_URL, OPENROUTER_API_KEY


def run_async_in_sync(function, *args, **kwargs):
    """
    Function to run the async code within the synchronous context
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(function(*args, **kwargs))


def get_openai_client() -> AsyncOpenAI:
    """
    Function for getting async OpenAI client
    """
    return AsyncOpenAI(
        base_url=OPENROUTER_BASE_URL,
        api_key=OPENROUTER_API_KEY,
    )


def calculate_llm_call_cost(model_name, input_tokens, output_tokens):
    """
       Calculates the total cost of an LLM API call based on token usage.

       Args:
           model_name (str): The name of the model being used.
           input_tokens (int): The number of input tokens.
           output_tokens (int): The number of output tokens.

       Returns:
           float: The total cost of the API call, rounded to four decimal places.
           Returns 0 if the model name is not found in the pricing dictionary.
       """
    if model_name not in PRICES_PER_1000_TOKEN:
        return 0

    input_price_per_1000 = PRICES_PER_1000_TOKEN[model_name]["input"]
    output_price_per_1000 = PRICES_PER_1000_TOKEN[model_name]["output"]

    input_cost = (input_tokens / 1000) * input_price_per_1000
    output_cost = (output_tokens / 1000) * output_price_per_1000
    total_cost = input_cost + output_cost

    return round(total_cost, 4)
