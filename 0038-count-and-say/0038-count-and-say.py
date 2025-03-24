class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        result = "1"
        
        for i in range(2, n + 1):
            current = ""
            count = 1
            # Loop through the previous result to generate the next term
            for j in range(1, len(result)):
                if result[j] == result[j - 1]:
                    count += 1
                else:
                    current += str(count) + result[j - 1]
                    count = 1
            
            # Add the last group
            current += str(count) + result[-1]
            
            # Update result to the next term
            result = current
        
        return result
