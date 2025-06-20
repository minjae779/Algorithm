def solution(s):
    answer = ''
    x = ''
    for i in range(len(s)):
        if s[i].isdigit() == True:
            answer += s[i]
        else:
            x += s[i]
        if x == 'zero':
            answer += '0'
            x = ''
        elif x == 'one':
            answer += '1'
            x = ''
        elif x == 'two':
            answer += '2'
            x = ''
        elif x == 'three':
            answer += '3'
            x = ''
        elif x == 'four':
            answer += '4'
            x = ''
        elif x == 'five':
            answer += '5'
            x = ''
        elif x == 'six':
            answer += '6'
            x = ''
        elif x == 'seven':
            answer += '7'
            x = ''
        elif x == 'eight':
            answer += '8'
            x = ''
        elif x == 'nine':
            answer += '9'
            x = ''
    answer = int(answer)
    return answer