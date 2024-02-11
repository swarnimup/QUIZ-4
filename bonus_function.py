from typing import List, Union

def count_lengths(elements: List[Union[str, int]]) -> List[int]:
    return [len(str(element)) for element in elements]
