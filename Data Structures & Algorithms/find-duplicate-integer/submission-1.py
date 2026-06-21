class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. with hash map O(n) both mem and time

        # 2. move m to m-1 idx in nums - if the value m already in that place and curr idx of m
        # != m-1 then return m. O(n) time, O(1) space with nums modificaiton

        for i in range(len(nums)):
            while nums[i] != i + 1:
                val = nums[i]

                if val == nums[val - 1]:
                    return val

                nums[i], nums[val - 1] = nums[val-1], nums[i]

        return -1