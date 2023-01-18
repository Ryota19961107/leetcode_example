class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n: int) -> int:
            total_sum = 0
            while n > 0:
                n, num = divmod(n, 10)
                total_sum += num ** 2
            return total_sum
        
        hashset = set()
        candidate = n
        while candidate != 1:
            candidate = get_next(candidate)
            if candidate not in hashset:
                hashset.add(candidate)
            else:
                return False
        return True