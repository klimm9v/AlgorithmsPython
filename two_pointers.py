x, y = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []

i, j = 0, 0
a_size = len(a)
b_size = len(b)

while i < a_size or j < b_size:
    if j == b_size or i < a_size and a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

print(*c)