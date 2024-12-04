from collections import defaultdict

lst = []
counter = defaultdict(int)

try:
    while True:
        l, r = map(int, input().split())
        lst.append(l)
        counter[r] += 1

except EOFError:
    pass
    
print(sum(map(lambda x: x * counter[x], lst)))
