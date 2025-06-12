def solution(sizes):
    answer = 0
    x = []
    y = []
    for i in range(len(sizes)):
        sizes[i].sort()
        x.append(sizes[i][0])
        y.append(sizes[i][1])
    answer = max(x)*max(y)
    return answer