def solution(schedules, timelogs, startday):
    answer = 0
    new_schedules = [k + 10 for k in schedules]
    for m in range(len(new_schedules)):
        for n in range(len(str(new_schedules[m]))):
            if len(str(new_schedules[m])) == 3:
                if n==1 and str(new_schedules[m])[1]=="6":
                    new_schedules[m] += 100
                    new_schedules[m] -= 60 
            elif len(str(new_schedules[m])) == 4:
                if n==2 and str(new_schedules[m])[2]=="6":
                    new_schedules[m] += 100
                    new_schedules[m] -= 60
    x = 0
    for i in range(len(schedules)):
        for j in range(7):
            if new_schedules[i] >= timelogs[i][j] and startday != 6 and startday != 7:
                x += 1
            if startday == 7:
                startday = 0
            startday += 1
        if x == 5:
            answer += 1
        x = 0
    return answer