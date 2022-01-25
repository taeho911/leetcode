# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:
#   - arr.length >= 3
#   - There exists some i with 0 < i < arr.length - 1 such that:
#     - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#     - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

class Solution:
    def validMountainArray(self, arr) -> bool:
        if len(arr) < 3:
            return False
        
        if arr[1] <= arr[0]:
            return False
        
        decrease_flag = 0
        for i in range(2, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            if decrease_flag == 0 and arr[i] < arr[i-1]:
                decrease_flag = 1
                continue
            if decrease_flag == 0 and arr[i] < arr[i-1]:
                return False
            if decrease_flag == 1 and arr[i] > arr[i-1]:
                return False
        
        return decrease_flag == 1

class Solution_0:
    def validMountainArray(self, arr) -> bool:
        # at least 3 elements for a chance of returning true
        if len(arr) < 3:
            return False
        
        # strictly increasing/decreasing sequence: any elements within the increasing/decreasing trend are equal
        i, j = 0, len(arr) - 1
        while i < len(arr) - 1 and arr[i] < arr[i + 1]:
            i += 1
        while j >= 0 and arr[j] < arr[j - 1]:
            j -= 1
            
        # at least both an increasing trend and a decreasing trend
        return i == j and i != 0 and j != len(arr) - 1
