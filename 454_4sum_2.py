'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
'''

from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        '''
        brutal force
        O(n^4)
        
        ans = 0
        length = len(nums1)
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    for l in range(length):
                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
                            ans += 1
        return ans
        '''
        
        '''
        two sum + two sum strategy
        '''
        ans = 0
        length = len(nums1)
        cache = defaultdict(int)
        
        for i in range(length):
            for j in range(length):
                cache[nums1[i] + nums2[j]] += 1
        
        for k in range(length):
            for l in range(length):
                ans += cache[-(nums3[k] + nums4[l])]
        
        return ans