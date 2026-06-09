class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - 1):
            j = i + 1
            while j < len(nums) and j <= i + k:
                if nums[i] == nums[j]:
                    return True
                j += 1
        
        return False