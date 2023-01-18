from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                count -= 1
        
        rows, cols = len(grid), len(grid[0])
        parent = [i for i in range(rows * cols)]
        count = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    index = i * cols + j
                    parent[index] = index
                    count += 1
                if j + 1 < cols and grid[i][j] == "1" and grid[i][j + 1] == "1":
                    union(i * cols + j, i * cols + j + 1)
                if i + 1 < rows and grid[i][j] == "1" and grid[i + 1][j] == "1":
                    union(i * cols + j, (i + 1) * cols + j)
        
        return count