N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))
happiness = [[None for c in range(101)] for r in range(N)]
max_happiness = 0
def say_goodbye(i, health):
    global max_happiness
    if i == N:
        return 0
    if happiness[i][health] is not None:
        return happiness[i][health]
    h1 = 0
    if health - L[i] > 0:
        h1 = say_goodbye(i + 1, health - L[i]) + J[i]
    h2 = say_goodbye(i + 1, health)
    max_happiness = max(h1, h2)
    return max_happiness
print(say_goodbye(0, 100))
