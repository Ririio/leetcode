from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iterate = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in iterate:
                return [iterate[complement], i]
            iterate[num] = i
            