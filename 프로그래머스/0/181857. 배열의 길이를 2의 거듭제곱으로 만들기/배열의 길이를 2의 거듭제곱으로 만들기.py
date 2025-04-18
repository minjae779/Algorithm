def solution(arr):
    answer = []
    x = 1
    while True:
        if len(arr) > x:
            x *= 2
        else:
            for i in range(len(arr), x):
                arr.append(0)
            break
    answer = arr
    return answer