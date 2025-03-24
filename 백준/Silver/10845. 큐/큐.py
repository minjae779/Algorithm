N = int(input())
x = [list(input().split()) for _ in range(N)]
y = []

for i in range(N):
    if x[i][0] == 'push':
        y.append(int(x[i][1]))
    elif x[i][0] == 'front':
        if y == []:
            print(-1)
        else:
            print(y[0])
    elif x[i][0] == 'back':
        if y == []:
            print(-1)
        else:
            print(y[-1])
    elif x[i][0] == 'size':
        print(len(y))
    elif x[i][0] == 'empty':
        if y == []:
            print(1)
        else:
            print(0)
    elif x[i][0] == 'pop':
        if y == []:
            print(-1)
        else:
            print(y[0])
            del y[0]