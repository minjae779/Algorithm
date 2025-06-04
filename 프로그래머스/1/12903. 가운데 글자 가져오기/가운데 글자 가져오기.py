def solution(s):
    answer = ''
    if len(s)%2==0:
        for i in range(len(s)//2-1,len(s)//2+1):
            answer += s[i]
    else:
        answer = s[len(s)//2]
    return answer