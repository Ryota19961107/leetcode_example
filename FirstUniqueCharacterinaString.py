class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        words = []
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
                words.append(s[i])
            else:
                if s[i] in words:
                    words.remove(s[i])
        return seen[words[0]] if words else -1