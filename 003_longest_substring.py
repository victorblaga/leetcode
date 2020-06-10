class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        max_last_seen_index = -1
        ans = 0

        last_seen = {}
        for index, char in enumerate(s):
            last_seen_index = max(last_seen.get(char, -1), max_last_seen_index)
            candidate_max = index - last_seen_index
            ans = max(ans, candidate_max)
            last_seen[char] = index
            max_last_seen_index = max(last_seen_index, max_last_seen_index)

        return ans


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcababcabba"))