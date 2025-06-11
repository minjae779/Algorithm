def solution(n):
    answer = 0
    x = ''
    while n > 0:
        n, mod = divmod(n,3)
        x += str(mod)
    answer = int(x,3)
    return answer