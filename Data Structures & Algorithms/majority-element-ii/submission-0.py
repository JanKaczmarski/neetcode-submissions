class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()

        want_ocur = len(nums) // 3
        res = []

        last = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != last:
                if cnt > want_ocur:
                    res.append(last)
                last = nums[i]
                cnt = 1
            else:
                cnt += 1

        if cnt > want_ocur:
            res.append(last)

        return res