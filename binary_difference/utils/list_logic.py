from typing import List


def list_and(l: List[bool]) -> bool:
    ans = True
    for x in l:
        ans = ans and x
    return ans
