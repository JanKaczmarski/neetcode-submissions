class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l < r:
            m = (l + r) // 2
            if m**2 == x or (m * m < x and (m + 1)**2 > x):
                return m
            elif m**2 < x:
                l = m + 1
            else:
                r = m - 1

        return l
