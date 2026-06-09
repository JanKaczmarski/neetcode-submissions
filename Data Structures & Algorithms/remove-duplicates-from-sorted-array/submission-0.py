class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        valid_id = 1
        last = nums[0]
        for i in range(1, len(nums)):
            # skip duplicates
            if last == nums[i]:
                continue
            
            nums[valid_id] = nums[i]
            valid_id += 1
            
            last = nums[i]

        return valid_id