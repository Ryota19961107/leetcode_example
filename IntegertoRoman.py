class Solution:
    def intToRoman(self, num: int) -> str:
        a = num // 1000
        b = (num - 1000 * a) // 100
        c = (num - 1000 * a - 100 * b) // 10
        d = num - 1000 * a - 100 * b - 10 * c

        def local_intRoman(N: int, X: str, Y: str, Z: str) -> str:
            if N == 0:
                return ''
            if N == 4:
                return X + Y
            if N == 9:
                return X + Z
            else:
                if N >= 5:
                    return Y + X * (N - 5)
                if N < 5:
                    return X * N
        ans = a * 'M' + local_intRoman(b, 'C', 'D', 'M') + local_intRoman(c, 'X', 'L', 'C') + local_intRoman(d, 'I', 'V', 'X')
        return ans