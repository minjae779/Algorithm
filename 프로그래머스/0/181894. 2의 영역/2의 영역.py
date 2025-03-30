def solution(arr):
    answer = []
    x = []
    for i in range(len(arr)):
        if arr[i] == 2:
            x.append(i)
    if x == []:
        answer.append(-1)
    else:
        a = min(x)
        b = max(x)
        answer += arr[a:b+1]
    return answer