from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for word in words:
            if word not in dict:
                dict[word] = 0
            dict[word] += 1
        list = sorted(dict.items(), key=lambda item: (-item[1], item[0]))
        return [list[i][0] for i in range(k)]