def solution(x1, x2, x3, x4):
    answer = True
    A = (x1 or x2) and (x3 or x4)
    answer = A
    return answer