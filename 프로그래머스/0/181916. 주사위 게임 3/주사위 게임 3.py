def solution(a, b, c, d):
    answer = 0
    x = [a, b, c, d]
    y = []
    for i in range(4):
        if x[i] not in y:
            y.append(x[i])
    if len(y)==1:
        answer = y[0]*1111
    elif len(y)==2:
        if x.count(y[0]) > x.count(y[1]):
            answer = (10*y[0]+y[1])**2
        elif x.count(y[0]) < x.count(y[1]):
            answer = (10*y[1]+y[0])**2
        elif x.count(y[0]) == x.count(y[1]):
            answer = (y[0]+y[1])*abs(y[0]-y[1])
    elif len(y)==3:
        if x.count(y[0]) > x.count(y[1]) and x.count(y[0]) > x.count(y[2]):
            answer = y[1]*y[2]
        elif x.count(y[1]) > x.count(y[0]) and x.count(y[1]) > x.count(y[2]):
            answer = y[0]*y[2]
        elif x.count(y[2]) > x.count(y[0]) and x.count(y[2]) > x.count(y[1]):
            answer = y[0]*y[1]
    elif len(y)==4:
        answer = min(y)
    return answer