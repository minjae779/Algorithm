T = list(map(int, input().split()))
i=0
if T[0]==1:
    while i<7:
        if T[i]+1==T[i+1]:
            if T[i+1]==8:
                print('ascending')
                break
            i+=1
            continue
        else:
            print('mixed')
            break
elif T[0]==8:
    while i<7:
        if T[i]-1==T[i+1]:
            if T[i+1]==1:
                print('descending')
                break
            i+=1
            continue
        else:
            print('mixed')
            break
else:
    print('mixed')