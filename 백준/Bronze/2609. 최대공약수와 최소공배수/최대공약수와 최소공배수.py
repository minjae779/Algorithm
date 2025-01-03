A, B = map(int, input().split())
a = 0
b = 0

for i in range(1, max(A,B)+1):
    if A%i==0:
        if B%i==0:
            a = i

b = int(A*B/a)

print(a)
print(b)