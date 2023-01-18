class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping_s_t, mapping_t_s = {}, {}
        for i, j in zip(s, t):
            if not i in mapping_s_t:
                mapping_s_t[i] = j
            if not j in mapping_t_s:
                mapping_t_s[j] = i
            if  mapping_s_t[i] != j or mapping_t_s[j] != i:
                return False
        return True