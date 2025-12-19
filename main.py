from typing import Any, List

def isList(l: List[Any]) -> bool:
    if not isinstance(l, list):
        return False
    if not l:
        return False
    else: return True

print(isList([]))
