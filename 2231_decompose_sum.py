N = int(input())
for i in range(N + 1):
    if i + sum([int(j) for j in str(i)]) == N:
        print (i)
        break
    if i == N:
        print (0)