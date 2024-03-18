#!/usr/bin/env python3
"""1-concurrent_coroutines.py
"""

import asyncio
from typing import List
wait_duration = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn wait_random n times """
    tasks = []
    delays = []

    for i in range(n):
        task = wait_duration(max_delay)
        tasks.append(task)
    
    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
