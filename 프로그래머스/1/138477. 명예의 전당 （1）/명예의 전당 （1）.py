def solution(k, score):
    answer = []
    x = []
    for i in range(len(score)):
        if len(answer) < k:
            x.append(score[i])
            answer.append(min(x))
        else:
            if score[i] > min(x):
                x.remove(min(x))
                x.append(score[i])
                answer.append(min(x))
            else:
                answer.append(min(x))
    return answer