# You have a long flowerbed in which some of the plots are planted, and some are not. 
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
# and an integer n, return if n new flowers can be planted in the flowerbed 
# without violating the no-adjacent-flowers rule.

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        
        try:
            start = flowerbed.index(1)
        except ValueError:
            if (len(flowerbed)+1)//2 >= n:
                return True
            else:
                return False
        
        if start > 1:
            n -= start//2
            if n <= 0:
                return True
        
        anchor = -1
        for i in range(start, len(flowerbed)):
            # 0 start
            if anchor == -1 and flowerbed[i] == 0:
                anchor = i
            # 1 start
            elif anchor != -1 and flowerbed[i] == 1:
                n -= (i-anchor-1)//2
                if n <= 0:
                    return True
                anchor = -1
            # last processing
            elif anchor != -1 and i == len(flowerbed)-1:
                n -= (i-anchor+1)//2
                if n <= 0:
                    return True
        return False

class Solution_0:
    def canPlaceFlowers(self, flowerbed, n):
        for i, flower in enumerate(flowerbed):
            if flower == 0 and (i == 0 or flowerbed[i - 1] == 0) \
            and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True

        return False
