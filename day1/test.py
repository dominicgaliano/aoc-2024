a = []
b = []

result2 = 0
try:
    while True:
        left, right = map(int, input().split())
        a.append(left)
        b.append(right)
        result2 += (left - right)
except EOFError:
    pass

a.sort()
b.sort()

result = 0
for i in range(len(a)):
    result += a[i] - b[i]

print(result)
print(result2)
