def solution(myString, pat):
    count = 0
    for i in range(len(myString)) :
        if pat in myString :
            count += 1
            myString = myString[myString.find(pat)+1:]
    return count