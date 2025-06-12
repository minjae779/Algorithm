def solution(t, p):
    answer = 0
    x = []
    for i in range(len(t)-len(p)+1):
        x.append(t[i:i+len(p)])
    for j in x:
        if int(j) <= int(p):
            answer += 1
    return answer