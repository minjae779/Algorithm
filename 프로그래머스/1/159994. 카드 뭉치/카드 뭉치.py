def solution(cards1, cards2, goal):
    answer = ''
    for i in range(len(goal)):
        if cards1 != []:
            if goal[i] == cards1[0]:
                del cards1[0]
        if cards2 != []:
            if goal[i] == cards2[0]:
                del cards2[0]
        if goal[i] in cards1 or goal[i] in cards2:
            break
    if goal[-1] not in cards1 and goal[-1] not in cards2:
        answer = 'Yes'
    else:
        answer = 'No'
    return answer