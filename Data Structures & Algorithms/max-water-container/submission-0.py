class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        res = -1

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            res = max(res, height * width)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res
