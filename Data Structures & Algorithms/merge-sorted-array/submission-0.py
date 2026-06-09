class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # shift the elemes from nums1 to the end
        if n != 0:
            for i in range(m - 1, -1, -1):
                offset = len(nums1) - m
                nums1[i], nums1[i + offset] = nums1[i + offset], nums1[i]

        l = len(nums1) - m
        r = 0
        place_idx = 0
        while l < len(nums1) and r < n:
            if nums1[l] <= nums2[r]:
                nums1[place_idx] = nums1[l]
                l += 1
            else:
                nums1[place_idx] = nums2[r]
                r += 1
            place_idx += 1

        while l < len(nums1):
            nums1[place_idx] = nums1[l]
            l += 1
            place_idx += 1
        while r < n:
            nums1[place_idx] = nums2[r]
            r += 1
            place_idx += 1

            
