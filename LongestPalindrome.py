class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import defaultdict
        num, max_odd = 0, 0
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        for cha in d:
            if d[cha] // 2 > 0:
                num += d[cha] //2 * 2
            if d[cha] % 2 == 1 and d[cha] > max_odd:
                max_odd = d[cha]
        return num + 1 if max_odd != 0 else num