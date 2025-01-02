N = int(input())

for i in range(1,N+1):
    s = i
    A = str(i)
    for k in range(len(A)):
        s += int(A[k])
    if s == N:
        print(i)
        break
    elif i == N:
        print(0)