class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, cur_sum = 0, 0
        pref_sums = {0 : 1}

        for num in nums:
            cur_sum += num
            want_val = cur_sum - k

            if want_val in pref_sums:
                res += pref_sums[want_val]

            if cur_sum in pref_sums:
                pref_sums[cur_sum] += 1
            else:
                pref_sums[cur_sum] = 1

        return res

