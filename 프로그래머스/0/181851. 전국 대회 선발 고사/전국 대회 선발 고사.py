def solution(rank, attendance):
    answer = 0
    x = []
    for i in range(len(rank)):
        if attendance[i] == True:
            x.append([i,rank[i]])
    x.sort(key=lambda x:x[1])
    for j in range(3):
        if j == 0:
            answer += x[j][0]*10000
        elif j == 1:
            answer += x[j][0]*100
        elif j == 2:
            answer += x[j][0]
    return answer