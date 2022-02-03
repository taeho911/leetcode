course_map = {
    4: {1,2},
    1: {3},
    2: {3},
    3: {4}
}

def dfs(k, stack, res):
    print(k, stack, res)
    if k in stack:
        res[0] = False
        return
    stack.append(k)
    if k in course_map:
        for next_k in course_map[k]:
            dfs(next_k, stack, res)
            if not res[0]:
                return
    stack.pop()

res = [True]
dfs(4, [], res)
print(res)
