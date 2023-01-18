from typing import List

from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def trans_ini_a(s: str) -> str:
            trans_ini = ord(s[0]) - ord("a")
            trans_s = ""
            for c in s:
                if ord(c) -trans_ini < ord("a"):
                    trans_c = chr(ord(c) -trans_ini + 26)
                else:
                    trans_c = chr(ord(c) -trans_ini)
                trans_s = trans_s + trans_c
            return trans_s
    
        memo = defaultdict(list)
        for word in strings:
                memo[trans_ini_a(word)].append(word)
        return memo.values()