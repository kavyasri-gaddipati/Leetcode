class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(s, open_count, close_count):
            # If the current string length is 2 * n, it's a valid combination
            if len(s) == 2 * n:
                result.append(s)
                return
            
            # Add an open parenthesis if there are remaining open ones
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)
            
            # Add a closing parenthesis if it does not exceed the open count
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)
        
        result = []
        backtrack("", 0, 0)
        return result
