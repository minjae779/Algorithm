T = int(input())

for i in range(T):
    S, R = input().split()

    for j in range(len(R)):
        print(R[j]*int(S), end='')
    print()