class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        p2 = len(num2) - 1
        products = []
        j = 0
        while p2 >= 0:
            n2 = ord(num2[p2]) - ord("0")
            p1 = len(num1) - 1
            carry, hold = 0, []
            i = 0
            while p1 >= 0:
                n1 = ord(num1[p1]) - ord("0")
                res = (n1 * n2 + carry) % 10
                carry = (n1 * n2 + carry) // 10
                hold.append(res * 10 ** i)
                i += 1
                p1 -= 1
            if carry:
                hold.append(carry * 10 ** i)
            products.append(sum(hold) * 10 ** j)
            p2 -= 1
            j += 1
        return str(sum(products))