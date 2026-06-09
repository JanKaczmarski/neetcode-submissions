class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 goes to the start, 2 goes to the end
        # 1 will be in correct place when 0 and 2 will be sorted

        zero_ptr, two_ptr = 0, len(nums) - 1

        i = 0
        while i < len(nums):
            if nums[i] == 0 and i > zero_ptr:
                nums[i], nums[zero_ptr] = nums[zero_ptr], nums[i]
                zero_ptr += 1
            elif nums[i] == 2 and i < two_ptr:
                nums[i], nums[two_ptr] = nums[two_ptr], nums[i]
                two_ptr -= 1
            else: # the value is 1 or is in correct place
                i += 1

        return nums
                