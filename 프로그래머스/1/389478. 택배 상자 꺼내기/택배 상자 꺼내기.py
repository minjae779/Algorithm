def solution(n, w, num):
    answer = 0
    floor = []
    h = n//w+1
    x = 1

    for i in range(h):
        parcel = []
        for j in range(w):
            if x <= n:
                parcel.append(x)
                x+=1
            else:
                parcel.append(0)
        if i%2==0:
            floor.append(parcel)
        else:
            parcel.reverse()
            floor.append(parcel)
            
    for k in range(h):
        for m in range(w):
            if floor[k][m] == num:
                if floor[h-1][m] != 0:
                    answer = h-k
                else:
                    answer = h-1-k
    return answer