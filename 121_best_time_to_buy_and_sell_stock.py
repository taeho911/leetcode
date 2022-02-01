# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

import sys

class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        
        ans = 0
        min_p = prices[0]
        
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - min_p)
            min_p = min(min_p, prices[i])
        
        return ans

class Solution_0:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        
        ans = 0
        pre = sys.maxsize
        for i in range(len(prices)-1):
            if prices[i] < pre:
                ans = max(ans, max(prices[i+1:]) - prices[i])
                pre = prices[i]
        
        return ans

class Solution_1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell, ans = prices[0], prices[0], 0
        
        for price in prices:
            if price < buy:
                buy = price
                sell = price
                continue
            if price > sell:
                if price - buy > ans:
                    ans = price - buy
                    sell = price
        
        return ans
