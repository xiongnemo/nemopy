from typing import Iterable


def get_element_by_batch_of(data: Iterable, n: int):
    for i in range(0, len(data), n):
        yield data[i:i+n]
