from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def BinarySearch(nums: List[list], target) ->bool:
            left, right = -1, len(nums)
            while right - left > 1:
                mid = left + (right - left) //2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid
            return left
        
        n = len(matrix)
        for i in range(n):
            index = BinarySearch(nums=matrix[i], target=target)
            pur = matrix[i][index]
            if pur == target:
                return True
        return False