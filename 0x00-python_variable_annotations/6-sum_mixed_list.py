#!/usr/bin/env python3
'''6-sum_mixed_list.py
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Computes the sum of a list with both int and float values.
    '''
    return float(sum(mxd_lst)
