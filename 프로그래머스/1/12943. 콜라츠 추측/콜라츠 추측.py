def solution(num):
    answer = 0
    while answer < 500 and num != 1:
        if num%2==0:
            num = num/2
        else:
            num = num*3 + 1
        answer+=1
    if answer == 500:
        answer = -1
    return answer