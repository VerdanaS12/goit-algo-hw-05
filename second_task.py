import re
from typing import Callable

def generator_numbers(text: str):
    for match in re.findall(r'\s\d+\.\d+\s', text):
        yield float(match.strip())

def sum_profit(text: str, func: Callable):
    return sum(func(text))
