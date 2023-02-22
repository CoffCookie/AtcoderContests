N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Answer = 0

for i in range(N):
    for j in range(M):
        if B[j] == (i+1):
            Answer += A[i]

print(Answer)
