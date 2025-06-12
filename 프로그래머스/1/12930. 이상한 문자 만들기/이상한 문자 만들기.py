def solution(s):
    answer = ''
    x = s.split(" ")
    for i in x:
        for j in range(len(i)):
            if j%2==0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    answer = answer[:-1]
    return answer