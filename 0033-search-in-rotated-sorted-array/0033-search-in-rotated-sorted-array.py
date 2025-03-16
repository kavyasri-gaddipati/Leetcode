class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # Finding the middle index

            if nums[mid] == target:
                return mid  # If mid element is target, return index
            
            # Checking which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:  
                    right = mid - 1  # Search in the left half
                else:
                    left = mid + 1  # Search in the right half
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  
                    left = mid + 1  # Search in the right half
                else:
                    right = mid - 1  # Search in the left half
        
        return -1  # Target not found
