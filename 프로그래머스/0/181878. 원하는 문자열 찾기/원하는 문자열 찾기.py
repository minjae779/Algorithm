def solution(myString, pat):
    answer = 0
    if pat.casefold() in myString.casefold():
        answer = 1
    return answer