# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        sb = []
        depth = min([len(s) for s in strs])
        pivot = strs[0]
        for i in range(depth):
            for s in strs:
                if s[i] != pivot[i]:
                    return ''.join(sb)
            sb.append(pivot[i])
        return ''.join(sb)