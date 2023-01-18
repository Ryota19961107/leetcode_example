from typing import List

import collections

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootY] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        groups = collections.defaultdict(list)
        uf = UnionFind(len(s))
        for child, parent in pairs:
            uf.union(child, parent)
        for i in range(len(s)):
            groups[uf.find(i)].append(s[i])
        for key in groups.keys():
            groups[key].sort(reverse=True)
        
        res = []
        for i in range(len(s)):
            res.append(groups[uf.find(i)].pop())
        return "".join(res)