def quick_sort(ls):
    if len(ls) <= 1:
        return ls
    pivot = ls[0]
    left = []
    equal = []
    right = []
    
    for i in range(len(ls)):
        if ls[i] > pivot:
            right.append(ls[i])
        elif ls[i] < pivot:
            left.append(ls[i])
        else:
            equal.append(ls[i])
    
    return quick_sort(left) + equal + quick_sort(right)

print(quick_sort([13,13,12,26,1,55,2,3,679,4,26,2,1]))
