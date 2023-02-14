N,M = map(int,input().split())
S = []
T = []
count = 0
for _ in range(N):
    S.append(input())

for _ in range(M):
    T.append(input())

T1 = list(set(T))

for i in range(N):
    for j in range(len(T1)):
        if S[i][-3:] == T1[j]:
            count += 1

print(count)

             


