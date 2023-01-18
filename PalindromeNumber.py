class Solution:
    def isPalindrome(self, x: int) -> bool:
        target = str(x)
        left, right = 0, len(target) - 1
        while left < right:
            if not target[left] == target[right]:
                return False
            left += 1
            right -= 1
        return True