def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0 and i%2==0 and code[i] != "1":
            answer = answer + code[i]
        elif mode == 1 and i%2!=0 and code[i] != "1":
            answer = answer + code[i]
        if mode == 0 and code[i] == "1":
            mode = 1
        elif mode == 1 and code[i] =="1":
            mode = 0
    if answer == '':
        answer = "EMPTY"
    return answer