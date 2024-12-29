class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def find_kth_element(arr1, arr2, k):
            len1, len2 = len(arr1), len(arr2)
            if len1 > len2:
                return find_kth_element(arr2, arr1, k)
            if len1 == 0:
                return arr2[k - 1]
            if k == 1:
                return min(arr1[0], arr2[0])

            i = min(len1, k // 2)
            j = k - i

            if arr1[i - 1] <= arr2[j - 1]:
                return find_kth_element(arr1[i:], arr2, k - i)
            else:
                return find_kth_element(arr1, arr2[j:], k - j)

        total_length = len(nums1) + len(nums2)

        if total_length % 2 == 1:
            return find_kth_element(nums1, nums2, total_length // 2 + 1)
        else:
            mid1 = find_kth_element(nums1, nums2, total_length // 2)
            mid2 = find_kth_element(nums1, nums2, total_length // 2 + 1)
            return (mid1 + mid2) / 2.0

# Example usage:
solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
print(solution.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
