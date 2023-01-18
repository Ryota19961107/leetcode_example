class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(":")", "{":"}", "[":"]"}
        open_blackets = set(["(", "{", "["])
        stack = []
        for char in s:
            if char in open_blackets:
                stack.append(char)
            elif stack and char == hashmap[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []