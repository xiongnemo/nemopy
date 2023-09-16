from typing import Iterable
from itertools import chain


def get_element_by_batch_of(data: Iterable, n: int):
    for i in range(0, len(data), n):
        yield data[i:i+n]

def chain_iterables(*args: tuple[Iterable]):
    '''
    Usage: 
    '''
    return chain.from_iterable(args)