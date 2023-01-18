import collections

class Solution:
    def findpoworder(self, order: int) -> int:
        k = 0
        while pow(2, k) < pow(10, order):
            k += 1
        return k

    def reorderedPowerOf2(self, n: int) -> bool:
        count = collections.Counter(str(n))
        return any(count == collections.Counter(str(1 << b))
                   for b in range(31))