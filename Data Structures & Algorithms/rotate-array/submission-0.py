class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotated = [-1 for _ in range(len(nums))]

        for i in range(len(nums)):
            new_idx = (i + k) % len(nums)
            rotated[new_idx] = nums[i]

        for i in range(len(nums)):
            nums[i] = rotated[i]