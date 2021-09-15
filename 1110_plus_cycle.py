N = M = int(input())
i = 0
while True:
    i += 1
    j = M // 10
    k = M % 10
    M = k * 10 + (j + k) % 10
    if N == M: break
print(i)