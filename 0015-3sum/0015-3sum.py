class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the input array
        nums.sort()
        result = []

        # Iterate through the array
        for i in range(len(nums)):
            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two-pointer approach
            target = -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move pointers
                    left += 1
                    right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
