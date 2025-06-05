def solution(left, right):
    answer = 0
    x = []
    for i in range(left,right+1):
        for j in range(1,i+1):
            if i%j==0:
                x.append(j)
        if len(x)%2==0:
            answer += i
        else:
            answer -= i
        x.clear()
    return answer