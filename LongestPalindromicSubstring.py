class Solution:
    def longestPalindrome(self, s: str) -> str:
        def center_expand(s: str, idx1: int, idx2: int):
            while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
                idx1 -= 1
                idx2 += 1 
            start = idx1 + 1
            end = idx2 - 1 + 1
            return s[start:end]
        
        
        if s == '':
            return ''
        elif len(s) ==1:
            return s
        else:
            res = ''
            for i in range (len(s)):
                pal_odd = center_expand(s, i, i)
                pal_even = center_expand(s, i, i + 1)
                pal_longer = max(pal_odd, pal_even, key=len)
                if len(res) < len(pal_longer):
                    res = pal_longer
            return res             