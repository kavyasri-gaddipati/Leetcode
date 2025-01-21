class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Create a memoization dictionary to store results of subproblems
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):  # If pattern is exhausted
                result = i == len(s)  # Match only if string is also exhausted
            else:
                # Check if first character matches
                first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                
                # Handle '*' in the pattern
                if j + 1 < len(p) and p[j + 1] == '*':
                    # '*' can either match zero occurrences or at least one
                    result = dp(i, j + 2) or (first_match and dp(i + 1, j))
                else:
                    # Regular match for one character
                    result = first_match and dp(i + 1, j + 1)
            
            # Store the result in memo
            memo[(i, j)] = result
            return result

        return dp(0, 0)
