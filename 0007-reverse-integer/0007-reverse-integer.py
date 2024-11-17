class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        is_negative = x < 0 
        x = abs(x)
        while x!=0:
            last_digit=x%10 
            rev=rev*10+last_digit 
            x=x//10
        if is_negative:
            rev = -rev
        
        
        if rev < -2**31 or rev > 2**31 - 1:
            return 0    
        return rev    