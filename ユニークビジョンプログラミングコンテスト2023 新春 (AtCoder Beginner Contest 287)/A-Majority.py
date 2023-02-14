N = int(input())
S = []
count_for = 0
count_against = 0

for _ in range(N):
    S.append(input())

for i in range(N):
    if S[i] == "For":
        count_for += 1
    else:
        count_against += 1

if (count_for + count_against) / 2 < count_for:
    print("Yes")
else:
    print("No")

