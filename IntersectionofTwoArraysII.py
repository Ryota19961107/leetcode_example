class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        memo = Counter(nums1)
        ans =[]
        for num2 in nums2:
            if num2 in memo and memo[num2] != 0:
                ans.append(num2)
                memo[num2] -= 1
        return ans