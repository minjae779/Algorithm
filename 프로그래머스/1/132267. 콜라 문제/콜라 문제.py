def solution(a, b, n):
    answer = 0
    while n >= a:
        x = (n//a)*b
        answer += x
        n = n%a+x
    return answer