from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = {}
        for num1 in nums1:
            for num2 in nums2:
                if num1 + num2 in hashmap:
                    hashmap[num1+num2] += 1
                else:
                    hashmap[num1+num2] = 1
        
        cnt = 0
        for num3 in nums3:
            for num4 in nums4:
                if -(num3 + num4) in hashmap:
                    cnt += hashmap[-(num3 + num4)]
        return cnt