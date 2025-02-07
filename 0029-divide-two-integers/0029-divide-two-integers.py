class Solution(object):
    def divide(self, dividend, divisor):
        """
        Divide two integers without using multiplication, division, or mod operator.
        The quotient is truncated toward zero.
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Define constants for 32-bit signed integer limits.
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow: when dividend is INT_MIN and divisor is -1, the result exceeds INT_MAX.
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result: negative if dividend and divisor have different signs.
        negative = (dividend < 0) != (divisor < 0)

        # Work with the absolute values to simplify the subtraction process.
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Subtract multiples of divisor from dividend using bit shifting for efficiency.
        while dividend >= divisor:
            temp = divisor  # This is the current multiple of divisor.
            multiple = 1    # This counts how many times divisor is subtracted.
            # Double the temp value until it would exceed the dividend.
            while dividend >= (temp << 1):
                temp <<= 1        # Equivalent to temp = temp * 2.
                multiple <<= 1    # Equivalent to multiple = multiple * 2.
            # Subtract the largest found multiple of divisor.
            dividend -= temp
            quotient += multiple

        # Adjust the sign of the result.
        return -quotient if negative else quotient
