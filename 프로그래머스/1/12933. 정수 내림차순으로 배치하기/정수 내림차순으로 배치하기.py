def solution(n):
    answer = 0
    x = []
    for i in range(len(str(n))):
        x.append(str(n)[i])
    x.sort(reverse=True)
    answer = int(''.join(x))
    return answer