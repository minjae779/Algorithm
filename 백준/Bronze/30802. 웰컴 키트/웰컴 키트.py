N = int(input())
A = list(map(int, input().split()))
T, P = map(int, input().split())
s=0

for i in range(len(A)):
    if A[i]<=T:
        if A[i]==0:
            s+=0
        else:
            s+=1
    else:
        if A[i]%T==0:
            s+=(A[i]//T)
        else:
            s+=(A[i]//T+1)

print(s)
print(N//P, N%P)