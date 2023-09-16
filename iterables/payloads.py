from typing import Iterable, Generator
from itertools import chain


def get_element_by_batch_of(data: Iterable, n: int):
    for i in range(0, len(data), n):
        yield data[i:i+n]

def chain_iterables(*args: tuple[Iterable]):
    '''
    Usage: 
    '''
    return chain.from_iterable(args)

def n_digit_suffix_generator(n: int) -> Generator[str, None, None]:
    '''Generate a sequence of n-digit suffixes.

    Yields:
        Generator[str]: generator of n-digit suffixes.

    Example:
        n = 4: 0000, 0001, 0002, ..., 9999
    '''
    
    for i in range(10 ** n):
        yield str(i).zfill(n)