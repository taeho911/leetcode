def bin_search(ls, target):
    l = 0
    r = len(ls) - 1
    m = r // 2

    while l <= r:
        if ls[m] == target:
            return True
        elif ls[m] > target:
            r = m - 1
        else:
            l = m + 1
        m = (l + r) // 2
    
    return False
