# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        total_len = len(nums1) + len(nums2)
        end = total_len // 2 + 1
        arr = [0] * end
        p1 = p2 = 0
        
        for i in range(end):
            if p1 >= len(nums1):
                arr = arr[:i] + nums2[p2:(p2 + end - i)]
                break
            elif p2 >= len(nums2):
                arr = arr[:i] + nums1[p1:(p1 + end - i)]
                break
            elif nums1[p1] <= nums2[p2]:
                arr[i] = nums1[p1]
                p1 += 1
            else:
                arr[i] = nums2[p2]
                p2 += 1
        
        if total_len % 2 == 1:
            return arr[-1]
        else:
            return (arr[-1] + arr[-2]) / 2

class Solution_0:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = nums1+nums2
        nums.sort()
        k = len(nums)
        p = k//2
        print(p)
        if( k%2 != 0):
            return float(nums[p])
        else:
            return (nums[p]+nums[p-1])/2
