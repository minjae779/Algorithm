def solution(my_string, is_prefix):
    answer = 0
    x = []
    for i in range(len(my_string)):
        x.append(my_string[:i])
    if is_prefix in x:
        answer += 1
    return answer