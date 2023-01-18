class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        ans = 1
        prev, preprev = 2, 1  
        k = 3
        while k < n + 1:
            ans = prev + preprev
            prev, preprev = ans, prev
            k += 1
        return ans