def solution(arr):
    answer = 0
    while True:
        x = []  
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i]%2==0:
                x.append(arr[i]//2)
            elif arr[i] < 50 and arr[i]%2!=0:
                x.append(arr[i]*2+1)
                
        if arr == x:
            return answer-1
        elif arr != x:
            answer += 1
            arr = x