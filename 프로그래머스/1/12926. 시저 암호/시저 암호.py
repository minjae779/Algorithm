def solution(s, n):
    answer = ''
    for i in range(len(s)):
        x = ord(s[i])
        for j in range(n):
            if x == 32:
                break
            x += 1
            if x == 123:
                x = 97
            elif x == 91:
                x = 65
        answer += chr(x)
    return answer