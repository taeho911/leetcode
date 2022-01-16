# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        res = []
        len_s = len(s)
        l = 0
        r = len_s
        
        def validate_partition(s, l, r):
            validated = set()
            for i in range(l, r):
                if s[i] not in validated:
                    for j in range(len(s), r, -1):
                        if s[j-1] == s[i]:
                            return [i, j]
                    validated.add(s[i])
            return [-1, -1]
        
        while l < len_s:
            while r > l and s[r-1] != s[l]:
                r -= 1
            
            i, j = validate_partition(s, l, r)
            if i != -1:
                l = i
                r = j
            else:
                if len(res) == 0:
                    res.append(r)
                else:
                    res.append(r - sum(res))
                l = r
                r = len_s
            
        return res

class Solution_0:
    def partitionLabels(self, s: str) -> list[int]:
        # 각 문자의 최대 인덱스를 저장
        last = {c: i for i, c in enumerate(s)}
        j = 0
        anchor = 0
        ans = []
        for i, c in enumerate(s):
            # 문자의 최대 인덱스를 구함
            j = max(j, last[c])
            # 왼쪽 포인터와 오른쪽 포인터가 만날때까지 지속
            if i == j:
                ans.append(i - anchor + 1)
                # 다음 덩어리의 시작점을 저장
                anchor = i + 1
            
        return ans
