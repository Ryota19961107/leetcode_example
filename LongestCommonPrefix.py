from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        flag = True
        for i in range(len(min(strs))):
            for j in range(len(strs)):
                count = 0
                if strs[j][i] != strs[0][i]:
                    flag = False
                    break
                else:
                    continue
            if flag == True:
                ans.append(strs[0][i])
            if flag == False:
                break            
        return ''.join(ans)    