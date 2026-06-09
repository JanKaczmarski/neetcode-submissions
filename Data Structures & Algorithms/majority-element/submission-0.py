class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        want_size = len(nums) // 2

        cnt = 1
        last = nums[0]
        for num in nums[1:]:
            if cnt > want_size:
                return last

            if num == last:
                cnt += 1
            else:
                cnt = 1
                last = num
        
        # if not yet returned the last chain is desired
        return last

        

