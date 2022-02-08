# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        n_str = str(num)
        res = sum([int(s) for s in n_str])
        return self.addDigits(res)
