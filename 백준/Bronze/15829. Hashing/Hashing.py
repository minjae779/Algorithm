L = int(input())
S = input()
A = 0

for i in range(L):
    A += (ord(S[i])-96)*(31**i)

print(A)
