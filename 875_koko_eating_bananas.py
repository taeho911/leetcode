# Koko loves to eat bananas. 
# There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. 
# Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

class Solution:
    def minEatingSpeed(self, piles, h):
        
        if len(piles) == h:
            return max(piles)
        
        def can_eat_all(h, x):
            res = 0
            for bananas in piles:
                res += bananas // x if bananas % x == 0 else bananas // x + 1
            if res <= h:
                return True
            else:
                return False
        
        max_k = max(piles)
        min_k = sum(piles) // h if sum(piles) % h == 0 else sum(piles) // h + 1
        
        l = min_k
        r = max_k
        ans = max_k
        while l <= r:
            print([l,r])
            x = (r + l) // 2
            if can_eat_all(h, x):
                if ans == x:
                    ans = min(ans, x)
                    break
                ans = min(ans, x)
                r = x-1
            else:
                l = x+1
        return ans
