class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Edge case: If the list is empty, return an empty string
        if not strs:
            return ""
        
        # Assume the first string is the common prefix
        prefix = strs[0]
        
        # Compare the assumed prefix with each string in the array
        for s in strs[1:]:
            # Check if the current prefix matches the start of the string `s`
            while not s.startswith(prefix):
                # If not, shorten the prefix by removing the last character
                prefix = prefix[:-1]
                
                # If the prefix becomes empty, return an empty string
                if not prefix:
                    return ""
        
        return prefix
