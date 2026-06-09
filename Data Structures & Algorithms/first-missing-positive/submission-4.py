class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:    
        i = 0
        while i < len(nums):
            num = nums[i]
            if num <= 0:
                i += 1
                continue
            
            # do swap if valid
            if num > 0 and num <= len(nums) and nums[num - 1] != num:
                #print(nums, num)
                nums[num - 1], nums[i] = nums[i], nums[num - 1]
            else:
                i += 1 # already valid or can't swap
                
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != cnt + 1:
                return cnt + 1
            cnt += 1

        return len(nums) + 1
        
        