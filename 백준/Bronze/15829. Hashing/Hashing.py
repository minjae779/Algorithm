L = int(input())
S = input()
A = 0
M = 1234567891

for i in range(L):
    A += (ord(S[i])-96)*(31**i)

print(A%M)
