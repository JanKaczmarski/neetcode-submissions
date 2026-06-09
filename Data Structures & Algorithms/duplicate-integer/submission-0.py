class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        met = set()
        for val in nums:
            if val in met:
                return True
            met.add(val)

        return False