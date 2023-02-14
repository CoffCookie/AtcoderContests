N,K = map(int, input().split())
S = [input() for _ in range(N)]

l = []
for i in range(K):
    l.append(S[i])

l.sort()
for i in range(K):
    print(l[i])