N = int(input())
l = [list(map(int, input().split())) for l in range(N)]
answer = []

for i in range(N):
    answer.append(l[i][0] + l[i][1])

for i in range(N):
    print(answer[i])
