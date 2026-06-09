class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # skip values <= 0
        start_idx = 0
        for num in nums:
            if num <= 0:
                start_idx += 1

        if start_idx == len(nums):
            return 1
    
        #print(nums, start_idx)
        i = 0
        while i < len(nums):
            num = nums[i]
            if num <= 0:
                i += 1
                continue
            
            # do swap if valid
            if num <= len(nums) - start_idx and nums[start_idx + num - 1] != num:
                #print(nums, num)
                nums[start_idx + num - 1], nums[i] = nums[i], nums[start_idx + num - 1]
            else:
                i += 1 # already valid or can't swap

        #print(nums)

        cnt = 0
        for i in range(start_idx, len(nums)):
            #print(i, nums[i], cnt)
            if nums[i] != cnt + 1:
                return cnt + 1
            cnt += 1

        return len(nums) - start_idx + 1
        
        