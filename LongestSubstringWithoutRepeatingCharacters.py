class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = 1
        hashmap = {}
        i = 0
        for j, k in enumerate(s):
            if k in hashmap:
                i = max(i, hashmap[k] + 1)
            hashmap[k] = j
            longest = max(longest, j - i + 1)
        return longest