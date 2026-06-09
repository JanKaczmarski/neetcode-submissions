class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        res = float('inf')
        l = 0

        for r in range(len(nums)):
            cur_sum += nums[r]
            
            # shrink the window so sum < target
            while l <= r and cur_sum >= target:
                res = min(res, r - l + 1)
                cur_sum -= nums[l]
                l += 1

        if res == float('inf'):
            return 0

        return res

        #
            