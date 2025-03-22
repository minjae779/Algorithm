def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        x = list(my_strings[i])
        y = []
        y += x[parts[i][0]:parts[i][1]+1]
        answer += ''.join(y)
    return answer