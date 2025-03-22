N = int(input())
x = 1
y = 0
for i in range(1,N+1):
    x *= i
X = list(str(x))
X.reverse()
x = ''.join(X)
for j in range(len(x)):
    if x[j] != '0':
        break
    y+=1
print(y)