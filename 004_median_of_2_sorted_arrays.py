from typing import List
import sys


def select(array, cut):
    if cut % 2 == 1:
        idx = cut // 2
        return array[idx], array[idx]
    elif cut == 0:
        return (-sys.maxsize - 1), array[0]
    elif cut == 2 * len(array):
        return array[-1], sys.maxsize
    else:
        idx = cut // 2
        return array[idx - 1], array[idx]


def compute_median(array):
    if len(array) % 2 == 1:
        return array[len(array) // 2]
    else:
        idx = len(array) // 2
        first = array[idx - 1]
        second = array[idx]
        return (first + second) / 2.0


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1 is None or nums2 is None:
            raise Exception("Invalid input")
        if len(nums1) == 0 and len(nums2) == 0:
            raise Exception("Invalid input")
        if len(nums1) == 0:
            return compute_median(nums2)
        if len(nums2) == 0:
            return compute_median(nums1)

        smaller, larger = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        len_smaller = len(smaller)
        len_larger = len(larger)
        start = 0
        end = len_smaller * 2

        while True:
            cut_smaller = (end + start) // 2
            left_smaller, right_smaller = select(smaller, cut_smaller)
            cut_larger = len_smaller + len_larger - cut_smaller
            left_larger, right_larger = select(larger, cut_larger)
            if left_smaller <= right_larger and left_larger <= right_smaller:
                # invariant holds
                break
            elif left_smaller > right_larger:
                # move end to the left
                end = (end + start) // 2
            elif left_larger > right_smaller:
                # move start to the right
                start = (end + start + 1) // 2

        res = (max(left_smaller, left_larger) + min(right_smaller, right_larger)) / 2.0
        return res


if __name__ == '__main__':
    # nums1 = [1, 3, 5, 7, 9, 12]
    # nums2 = [4, 6, 8, 11, 21, 29, 31]
    # print(Solution().findMedianSortedArrays(nums1, nums2))

    # nums1 = [1, 3]
    # nums2 = [2]
    # print(Solution().findMedianSortedArrays(nums1, nums2))

    # nums1 = [1, 2]
    # nums2 = [3, 4]
    # print(Solution().findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4, 5]
    print(Solution().findMedianSortedArrays(nums1, nums2))
