N, M = map(int, input().split())
A = [[] for i in range(N + 1)]
d_count = [[N] * (N + 1) for i in range(N + 1)]
min_decomposition = N;
for i in range(N - 1):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

def decompose(atom, parent):
    global min_decomposition
    d_count[atom][1] = 0
    for child in A[atom]:
        if child == parent:
            continue
        decompose(child, atom)
        i = N
        while i > 0:
            d_count[atom][i] += 1
            j = 1
            while j < i:
                d_count[atom][i] = min(d_count[atom][i], d_count[atom][j] + d_count[child][i - j])
                j += 1
            i -= 1
    if parent == 0:
        min_decomposition = min(min_decomposition, d_count[atom][M])
    else:
        print('🌚',atom, parent, d_count[atom][M] + 1, min_decomposition)
        min_decomposition = min(min_decomposition, d_count[atom][M] + 1)
for d in d_count:
    print(d)
print(min_decomposition)

