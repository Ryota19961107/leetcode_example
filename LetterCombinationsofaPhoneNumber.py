from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cash = []
        ans = []
        phone = ('', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')
        for digit in digits:
            res = []
            word = phone[int(digit)]
            if len(word) == 0:
                continue

            if cash == []:
                for i in range(len(word)):
                    cash.append(word[i])
            else:
                for i in range(len(cash)):
                    for j in range(len(word)):
                        res.append(cash[i] + word[j])
                cash = res  
        ans = cash
        return ans