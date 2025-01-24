class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize a stack with -1 to handle edge cases
        stack = [-1]
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                # Push the index of the '(' onto the stack
                stack.append(i)
            else:
                # Pop the top index for a matching ')'
                stack.pop()
                
                if not stack:
                    # If stack is empty, push the current index as the base for the next valid substring
                    stack.append(i)
                else:
                    # Calculate the length of the valid substring
                    max_length = max(max_length, i - stack[-1])
        
        return max_length
