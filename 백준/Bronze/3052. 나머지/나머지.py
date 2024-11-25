i = 0
a = []
while i<10:
    T = int(input())
    if T%42 not in a:
        a.append(T%42)
    i+=1
print(len(a))