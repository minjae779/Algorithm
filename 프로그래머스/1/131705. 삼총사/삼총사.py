def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(1,len(number)-1):
            for k in range(2,len(number)):
                if i<j and j<k and i<k:
                    if (number[i]+number[j]+number[k])==0:
                        answer+=1
    return answer