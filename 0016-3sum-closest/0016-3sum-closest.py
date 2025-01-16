class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Sort the array to use two-pointer technique
        nums.sort()
        # Initialize the result with a large number
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on the comparison with target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If current_sum is exactly equal to target, return immediately
                    return current_sum
        
        return closest_sum
