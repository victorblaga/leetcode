from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None or len(height) == 0:
            return 0

        len_h = len(height)
        left_heights = [0] * len_h
        left_heights[0] = height[0]
        right_heights = [0] * len_h
        right_heights[len_h - 1] = height[len_h - 1]
        for i in range(1, len_h):
            left_heights[i] = max(height[i], left_heights[i - 1])
            j = len_h - i - 1
            right_heights[j] = max(height[j], right_heights[j + 1])

        result = 0
        for i in range(len_h):
            result += min(left_heights[i], right_heights[i]) - height[i]

        return result


if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
