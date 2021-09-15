N = int(input())
H = [list(map(int, input().split())) for i in range(N)]
DP = [[None for j in range(3)] for i in range(N)]
for i in range(1, N):
    DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + H[i][0];
    DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + H[i][1];
    DP[i][2] = min(DP[i - 1][0], DP[i - 1][1]) + H[i][2];
print(min(DP[-1][0], DP[-1][1], DP[-1][2]))