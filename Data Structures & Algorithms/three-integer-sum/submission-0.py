from typing import Optional

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        last = None
        res = []
        for i in range(len(nums) - 2):
            # distinct triplets
            if i != 0 and last == nums[i]:
                continue

            j, k = i + 1, len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else: # eq
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

            last = nums[i]

        return res
            

            
