def solution(s):
    answer = []
    x = set()
    for i in range(len(s)):
        if s[i] not in x:
            x.add(s[i])
            answer.append(-1)
        else:
            answer.append(s[:i+1].rindex(s[i])-s[:i].rindex(s[i]))
    return answer