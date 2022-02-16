import random

for i in range(20):
    arr = []
    length = random.randint(4,12)
    for i in range(length):
        n = random.randint(0,1)
        arr.append('(' if n == 0 else ')')
    print('"' + ''.join(arr) + '"')
