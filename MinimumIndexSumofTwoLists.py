from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        from collections import defaultdict
        common_word = set(list1) & set(list2)
        memo = defaultdict(list)
        minimum = float("inf")
        for word in common_word:
            l1_idx, l2_idx = list1.index(word), list2.index(word)
            memo[l1_idx + l2_idx].append(word)
            if minimum > l1_idx + l2_idx:
                minimum = l1_idx + l2_idx
        return memo[minimum]