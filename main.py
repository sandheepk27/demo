from typing import Any, List

def isList(nums: List[Any]) -> bool:
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return [nums, k]

print(isList([1,1,2,3,3,4,5,6]))
