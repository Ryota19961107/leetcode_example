class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_word = {}
        map_s = {}
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        for w, c in zip(words, pattern):
            if c not in map_s:
                if w in map_word:
                    return False
                else:
                    map_s[c] = w
                    map_word[w] = c
            else:
                if map_s[c] != w:
                    return False
        return True