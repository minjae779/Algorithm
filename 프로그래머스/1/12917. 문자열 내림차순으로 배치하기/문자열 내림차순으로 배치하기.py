def solution(s):
    answer = ''
    x = [s[i] for i in range(len(s))]
    x.sort(reverse=True)
    answer = ''.join(x)
    return answer