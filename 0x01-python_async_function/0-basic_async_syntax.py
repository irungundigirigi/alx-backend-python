#!/usr/bin/env python3
"""an async coroutine that takes an int argument(max delay) and waits for random delay between 0 and max_delay seconds and returns it.
"""

import random 
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """ wait for wait_durations seconds """
    wait_duration = random.random() * max_delay
    await asyncio.sleep(wait_duration)
    return wait_duration
