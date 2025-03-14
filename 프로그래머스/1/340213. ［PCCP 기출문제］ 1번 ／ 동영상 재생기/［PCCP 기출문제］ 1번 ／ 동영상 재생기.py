import datetime

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    current = datetime.datetime.strptime(pos, '%M:%S')
    length = datetime.datetime.strptime(video_len, '%M:%S')
    ops = datetime.datetime.strptime(op_start, '%M:%S')
    ope = datetime.datetime.strptime(op_end, '%M:%S')

    if current >= ops and current <= ope:
        current = ope
        
    for i in commands:
        if i == "next":
            current = current + datetime.timedelta(seconds=10)
            if current > length:
                current = length
            elif current >= ops and current <= ope:
                current = ope
        elif i == "prev":
            current = current - datetime.timedelta(seconds=10)
            if current < datetime.datetime.strptime('00:00', '%M:%S'):
                current = datetime.datetime.strptime('00:00', '%M:%S')
                if current >= ops and current <= ope:
                    current = ope
            elif current >= ops and current <= ope:
                current = ope
    
    answer = current.strftime('%M:%S')
    return answer