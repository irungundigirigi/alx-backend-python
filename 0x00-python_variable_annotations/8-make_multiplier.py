#!/usr/bin/env python3

'''
    8-make_multiplier.py
'''
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates multiplier function
    '''
    return lambda x:x * multiplier

