N,K = map(int, input().split())
S = list(input())
count = 0

for i in range(N):
    if S[i] == 'o':
        count += 1
    if count > K:
        S[i] = 'x'

print("".join(S))


