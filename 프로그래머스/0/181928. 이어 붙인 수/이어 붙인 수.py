def solution(num_list):
    answer = 0
    x = ''
    y = ''
    for i in range(len(num_list)):
        if num_list[i]%2 != 0:
            x += str(num_list[i])
        else:
            y += str(num_list[i])
    answer = int(x) + int(y)
    return answer