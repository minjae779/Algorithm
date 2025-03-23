from collections import deque

N = int(input())
x = deque()
for i in range(1, N+1):
    x.append(i)

while len(x)!=1:
    del x[0]
    x.rotate(-1)
print(x[0])