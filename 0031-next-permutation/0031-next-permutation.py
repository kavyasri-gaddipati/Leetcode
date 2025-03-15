class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None (Modifies nums in-place)
        """
        # Step 1: Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If found, swap it with the next larger element from the right
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # Swap

        # Step 3: Reverse the remaining right part to get the next smallest permutation
        nums[i + 1:] = reversed(nums[i + 1:])
