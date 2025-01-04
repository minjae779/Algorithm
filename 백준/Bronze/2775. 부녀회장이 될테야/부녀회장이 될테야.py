T = int(input())

for i in range(T):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    k = int(input())
    n = int(input())

    for j in range(k):
        for z in range(1, n):
            A[z] += A[z-1]
    print(A[n-1])