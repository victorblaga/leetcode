from typing import List
import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_max_sum = -sys.maxsize
        res = -sys.maxsize
        for i in range(len(nums)):
            elem = nums[i]
            candidate_sum = prev_max_sum + elem
            prev_max_sum = max(candidate_sum, elem)
            res = max(res, prev_max_sum)

        return res


if __name__ == "__main__":
    Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
