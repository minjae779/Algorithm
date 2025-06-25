def solution(food):
    answer = ''
    a = []
    b = []
    for i in range(1,len(food)):
        if food[i]%2 != 0:
            x = food[i]-1
        else:
            x = food[i]
        for j in range(x):
            if j%2==0:
                a.append(str(i))
            else:
                b.insert(0,str(i))
    answer += ''.join(a)
    answer += '0'
    answer += ''.join(b)
    return answer