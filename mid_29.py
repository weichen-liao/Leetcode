# -*- coding: utf-8 -*-
# Author: Weichen Liao
'''
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # ans = int(dividend/divisor)
        # if ans<0:
        #     return max(ans, -2**31)
        # elif ans>0:
        #     return min(ans,2**31-1)
        # else:
        #     return ans

        if dividend == 0:
            return 0
        elif (dividend > 0 and divisor > 0) or (dividend<0 and divisor<0):
            sign = 1
        else:
            sign = -1

        res = 0
        count = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        for i in range(dividend):
            count += 1
            if count == divisor:
                res += 1
                count = 0
        res = sign * res
        if res<0:
            return max(res, -2147483648)
        else:
            return min(res,2147483647)

dividend = -2147483648
divisor = -1
s = Solution()
res = s.divide(dividend, divisor)
print(res)
