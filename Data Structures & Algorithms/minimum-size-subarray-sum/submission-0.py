class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # brute force - i-th num check every j >= i subarray if it eq target
        # if j - i + 1 < cur_min than store it 

        cur_min = float('inf')
        n = len(nums)

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s >= target:
                    cur_min = min(cur_min, j - i + 1)
                    break

        if cur_min == float('inf'):
            return 0

        return cur_min