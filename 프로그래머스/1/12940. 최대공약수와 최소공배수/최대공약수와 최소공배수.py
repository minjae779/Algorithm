def solution(n, m):
    answer = []
    a = [i for i in range(1,n+1) if n%i==0]
    b = [j for j in range(1,m+1) if m%j==0]
    answer.append(max(k for k in a if k in b))
    answer.append(n*m//answer[0])
    return answer