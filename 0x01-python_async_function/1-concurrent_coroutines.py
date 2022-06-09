#!/usr/bin/env python3
""" 1. Let's execute multiple coroutines at the same time with async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Let's execute multiple coroutines at the same time with async  """
    delays: List[float] = []
    allDelays: List[float] = []

    for iter in range(n):
        delays.append(wait_random(max_delay))

    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        allDelays.append(earliest_result)
    return allDelays
