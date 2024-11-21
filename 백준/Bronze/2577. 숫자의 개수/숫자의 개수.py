A = int(input())
B = int(input())
C = int(input())

X = A*B*C
i = 0

while i<10:
    print(str(X).count(str(i)))
    i+=1