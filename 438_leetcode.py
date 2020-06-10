from typing import List


class Bag(object):
    def __init__(self, s):
        self.bag = {}
        for char in s:
            cnt = self.bag.get(char, 0)
            self.bag[char] = cnt + 1

    def extend(self, to_remove, to_add):
        if to_remove in self.bag:
            self.bag[to_remove] = self.bag[to_remove] - 1
            if self.bag[to_remove] == 0:
                del self.bag[to_remove]

        to_add_cnt = self.bag.get(to_add, 0)
        self.bag[to_add] = to_add_cnt + 1

    def __eq__(self, other):
        return self.bag == other.bag

    def __repr__(self):
        return repr(self.bag)


class Solution(object):
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s) or s is None or p is None:
            return []

        result = []
        len_p = len(p)
        len_s = len(s)
        init_s = s[0:len_p]
        bag_s = Bag(init_s)
        bag_p = Bag(p)
        if bag_s == bag_p:
            result.append(0)

        for i in range(1, len_s - len_p + 1):
            substr = s[i:i+len_p]
            to_remove = s[i - 1]
            to_add = s[i + len_p - 1]
            bag_s.extend(to_remove, to_add)
            if bag_s == bag_p:
                result.append(i)

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd", "abc"))