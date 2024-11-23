class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # If the needle is an empty string, return 0
        if not needle:
            return 0
        
        # Loop through the haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring matches the needle
            if haystack[i:i+len(needle)] == needle:
                return i  # Return the starting index of the first occurrence
        
        return -1  # If needle is not found, return -1
