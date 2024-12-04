a = []
b = []

try:
    while True:
        left, right =  map(int, input().split())
        a.append(left)
        b.append(right)
except EOFError:
    pass
    
a.sort()
b.sort()

print(sum(map(lambda pair: abs(pair[0] - pair[1]), zip(a,b))))
