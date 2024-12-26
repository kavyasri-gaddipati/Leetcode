class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Function to expand around the center and find the palindrome
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Return the palindromic substring

        if not s or len(s) == 1:
            return s

        longest = ""
        for i in range(len(s)):
            # Odd-length palindromes (single character center)
            pal1 = expandAroundCenter(i, i)
            # Even-length palindromes (two-character center)
            pal2 = expandAroundCenter(i, i + 1)

            # Update the longest palindrome found
            if len(pal1) > len(longest):
                longest = pal1
            if len(pal2) > len(longest):
                longest = pal2

        return longest
