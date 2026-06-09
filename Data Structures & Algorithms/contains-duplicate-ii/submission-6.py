class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time: O(n)
        # Space: O(k)
        if k == 0:
            return False

        sett = set()
        n = len(nums)
        for i in range(min(k + 1, n)):
            if nums[i] in sett:
                return True
            sett.add(nums[i])

        #print("start", sett)

        for i in range(k + 1, n):
            #print(i, sett, i-k)
            if nums[i - k - 1] in sett:
                sett.remove(nums[i - k - 1])
            if nums[i] in sett:
                return True
            
            sett.add(nums[i])

        return False