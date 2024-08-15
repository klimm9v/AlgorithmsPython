from typing import List

def binary_search(nums: List[int], target: int) -> int | None:

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1


nums = [22, 33, 45, 46, 57] 
target = 22
print(binary_search(nums, target))