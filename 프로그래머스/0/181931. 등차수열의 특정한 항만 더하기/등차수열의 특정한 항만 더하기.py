def solution(a, d, included):
    answer = 0
    x = a
    y = []
    for i in range(len(included)):
        if included[i] == True:
            y.append(x)
        x += d
    answer = sum(y)
    return answer