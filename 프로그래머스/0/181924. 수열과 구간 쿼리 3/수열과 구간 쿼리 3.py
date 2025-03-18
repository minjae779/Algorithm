def solution(arr, queries):
    answer = []
    x = 0
    for i in range(len(queries)):
        for j in range(len(arr)):
            if queries[i][0] == j:
                x = arr[queries[i][1]]
                arr[queries[i][1]] = arr[queries[i][0]]
                arr[queries[i][0]] = x
    answer = arr
    return answer