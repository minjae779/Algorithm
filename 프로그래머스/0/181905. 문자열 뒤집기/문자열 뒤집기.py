def solution(my_string, s, e):
    answer = ''
    x = list(my_string)
    y = []
    for j in range(s,e+1):
        y.insert(0,x[j])
        if j == e:
            x[s:e+1] = y
            y.clear()
    answer = ''.join(x)
    return answer