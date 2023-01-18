class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        ans = []
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            res = (x1 + x2 + carry) % 10 
            carry = (x1 + x2 + carry) // 10
            ans.append(res)
            p1 -= 1
            p2 -= 1
        if carry:
            ans.append(carry)
        return ''.join(str(x) for x in ans[::-1])