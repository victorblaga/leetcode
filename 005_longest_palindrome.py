class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        max_length_i = -1
        max_length_j = -1
        for length in range(1, len(s) + 1):
            for i in range(len(s) - length + 1):
                found_something = False

                if length == 1:
                    memo[(i, i)] = True
                    found_something = True
                elif length == 2:
                    res = (s[i] == s[i + 1])
                    memo[(i, i + 1)] = res
                    found_something = res
                else:
                    j = i + length - 1
                    res = memo[(i + 1, j - 1)] and s[i] == s[j]
                    found_something = res
                    memo[(i, j)] = res

                if found_something:
                    max_length_i = i
                    max_length_j = i + length

        return s[max_length_i:max_length_j]


if __name__ == '__main__':
    Solution().longestPalindrome("babad")