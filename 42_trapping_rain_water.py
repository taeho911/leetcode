# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Brutal Force
class Solution:
    def trap(self, height) -> int:
        max_h = max(height)
        w = len(height)
        waters = 0
        
        for h in range(max_h, 0, -1):
            layer = []
            end = 0
            for j in range(w):
                if height[j] >= h:
                    layer.append(0)
                    end = len(layer)
                elif layer:
                    layer.append(1)
            waters += sum(layer[:end])
        
        return waters

# DP Two Pointers
class Solution:
    def trap(self, height) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        l_max = r_max = 0
        
        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max < r_max:
                ans += l_max - height[left]
                left += 1
            else:
                ans += r_max - height[right]
                right -= 1
        
        return ans
