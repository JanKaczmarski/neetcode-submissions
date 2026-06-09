class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        valid_id = 1
        
        for i in range(1, len(nums)):
            # skip duplicates
            if nums[i] == nums[i - 1]:
                continue
            
            nums[valid_id] = nums[i]
            valid_id += 1

        return valid_id