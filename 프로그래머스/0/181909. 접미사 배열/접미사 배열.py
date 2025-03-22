def solution(my_string):
    answer = []
    x = []
    for i in range(len(my_string)):
        x.append(my_string[i:])
    answer = sorted(x)
    return answer