def getOccurrence(ls):
    res = [0] * 10
    prev = 0
    pos = 0
    for i in range(9,-1,-1):
        if i in ls:
            next_pos = ls.index(i)
            res[prev] = next_pos - pos
            prev = i
            pos = next_pos
        else:
            res[i] = 0
    res[prev] = len(ls) - pos
    return res

def solution(l):
    if len(l) == 0:
        return 0
    
    sorted_l = sorted(l, reverse=True)
    surplus = sum(sorted_l) % 3
    
    if surplus == 0:
        return int(''.join([str(n) for n in sorted_l]))
    
    elif len(sorted_l) > 1 and surplus == 1:
        occurrence = getOccurrence(sorted_l)
        
        # remove 1 element
        for num in [1, 4, 7]:
            if occurrence[num] != 0:
                i = sorted_l.index(num)
                return int(''.join([str(n) for n in sorted_l[:i] + sorted_l[i+1:]]))
        
        # remove 2 elements
        for num in [4, 7]:
            if occurrence[2] >= 2:
                i = sorted_l.index(2)
                return int(''.join([str(n) for n in sorted_l[:i] + sorted_l[i+2:]]))
            elif occurrence[2] == 1 and occurrence[5] != 0:
                i5 = sorted_l.index(5)
                i2 = sorted_l.index(2)
                return int(''.join([str(n) for n in sorted_l[:i5] + sorted_l[i5+1:i2] + sorted_l[i2+1:]]))
    
    elif len(sorted_l) > 1 and surplus == 2:
        occurrence = getOccurrence(sorted_l)
        
        # remove 1 element
        for num in [2, 5, 8]:
            if occurrence[num] != 0:
                i = sorted_l.index(num)
                return int(''.join([str(n) for n in sorted_l[:i] + sorted_l[i+1:]]))
        
        # remove 2 elements
        for num in [2, 5, 8]:
            if occurrence[1] >= 2:
                i = sorted_l.index(1)
                return int(''.join([str(n) for n in sorted_l[:i] + sorted_l[i+2:]]))
            elif occurrence[1] != 0 and occurrence[4] != 0:
                i4 = sorted_l.index(4)
                i1 = sorted_l.index(1)
                return int(''.join([str(n) for n in sorted_l[:i4] + sorted_l[i4+1:i1] + sorted_l[i1+1:]]))
            elif occurrence[4] >= 2:
                i = sorted_l.index(4)
                return int(''.join([str(n) for n in sorted_l[:i] + sorted_l[i+2:]]))
            elif occurrence[1] != 0 and occurrence[7] != 0:
                i7 = sorted_l.index(7)
                i1 = sorted_l.index(1)
                return int(''.join([str(n) for n in sorted_l[:i7] + sorted_l[i7+1:i1] + sorted_l[i1+1:]]))
        
        # remove 3 elements
        if occurrence[1] != 0 and occurrence[3] != 0 and occurrence[4] != 0:
            i4 = sorted_l.index(4)
            i3 = sorted_l.index(3)
            i1 = sorted_l.index(1)
            return int(''.join([str(n) for n in sorted_l[:i4] + sorted_l[i4+1:i3] + sorted_l[i3+1:i1] + sorted_l[i1+1:]]))
    
    return 0


print(solution( [0, 2, 7] ))
print(solution( [4, 6, 0] ))
print(solution( [2, 2, 5] ))
print(solution( [1, 1, 8] ))
print(solution( [7, 2, 1] ))
print(solution( [9, 0, 3] ))
print(solution( [8, 4, 8] ))
print(solution( [7, 6, 9] ))
print(solution( [9, 3, 2] ))
print(solution( [7, 8, 6] ))
print(solution( [6, 9, 4] ))
print(solution( [8, 6, 5] ))
print(solution( [7, 6, 9] ))
print(solution( [6, 8, 7] ))
print(solution( [0, 8, 2] ))
print(solution( [1, 1, 7] ))
print(solution( [6, 8, 4] ))
print(solution( [1, 9, 7] ))
print(solution( [1, 9, 3] ))
print(solution( [0, 8, 4] ))