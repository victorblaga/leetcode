from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complements:
                return list(sorted([i, complements[complement]]))
            complements[nums[i]] = i

        return []
