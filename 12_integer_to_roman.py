# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 
# 12 is written as XII, which is simply X + II. 
# The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. 
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ls = [
            (1000, 'M'),
            (500, 'D'),
            (100, 'C'),
            (50, 'L'),
            (10, 'X'),
            (5, 'V'),
            (1, 'I')
        ]
        stack = []
        for i in range(0, len(ls), 2):
            r = num // ls[i][0]
            if r < 4:
                stack.append(ls[i][1] * r)
                num -= ls[i][0] * r
            elif r == 4:
                stack.append(ls[i][1])
                stack.append(ls[i-1][1])
                num -= ls[i][0] * r
            elif r > 4 and r < 9:
                stack.append(ls[i-1][1])
                stack.append(ls[i][1] * (r - 5))
                num -= ls[i][0] * r
            elif r == 9:
                stack.append(ls[i][1])
                stack.append(ls[i-2][1])
                num -= ls[i][0] * r
            else:
                print('hoho')
        return ''.join(stack)
