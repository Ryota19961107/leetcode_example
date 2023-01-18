from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def closest(num, target):
            num.sort()
            nearest = num[0] + num[1] + num[2]
            for i in range(len(num)-2):
                if i > 0 and num[i] == num[i - 1]:
                    continue
                left = i + 1
                right = len(num) - 1
                while (left < right):
                    three_sum = num[left] + num[right] + num[i]
                    if three_sum == target:
                        return three_sum
                    if abs(three_sum - target) < abs(nearest - target):
                        nearest = three_sum
                    
                    if three_sum < target:
                        while(left < right and num[left] == num[left + 1]):
                            left += 1
                        left += 1
                    elif three_sum > target:
                        while(left < right and num[right] == num[right - 1]):
                            right -= 1
                        right -= 1
            return nearest
        return closest(nums, target)
        