i = 0
c = 0

while True:
    N = int(input())
    A = str(N)
    for j in range(len(A)):
        if A[j]==A[len(A)-1-j]:
            c = 1
        else:
            c = 0
            break
        
    if N == 0:
        break
    elif c == 1:
        print('yes')
    elif c == 0:
        print('no')
    i+=1