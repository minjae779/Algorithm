def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if myString[i].isupper()==True:
            if myString[i] == 'A':
                answer += myString[i]
            else:
                answer += myString[i].lower()
        else:
            if myString[i] == 'a':
                answer += 'A'
            else:
                answer += myString[i]
    return answer