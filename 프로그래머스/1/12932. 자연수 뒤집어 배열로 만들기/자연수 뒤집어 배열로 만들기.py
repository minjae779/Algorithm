def solution(n):
    answer = []
    for i in range(len(str(n))):
        answer.insert(0,int(str(n)[i]))
    return answer