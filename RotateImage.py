from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return matrix
        n = len(matrix)
        q = n // 2
        for i in range(q):
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
        for i in range(n - 1):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        """
        Do not return anything, modify matrix in-place instead.
        """