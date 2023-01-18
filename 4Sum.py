from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            output = []

            if not nums:
                return output
            
            ave_num = target //  k
            if (nums[0] > ave_num) or (nums[-1] < ave_num):
                return output

            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)-k+1):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                else:
                    for subst in kSum(nums[i+1:], target-nums[i], k-1):
                        output.append([nums[i]] + subst)
            return output

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            left = 0
            right = len(nums) - 1
            while left < right: 
                sum = nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
            return res
        
        nums.sort()
        return kSum(nums, target, 4)