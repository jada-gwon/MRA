N = int(input())
line = [int(input()) for i in range(N)]
S = set(line)
max_continuing = 0
for s in set(line):
    new_line = list(filter(lambda x:x!=s, line))
    new_line.append(-1)
    prev = -1
    continuing = 1
    for i in new_line:
        if i != prev:
            max_continuing = max(max_continuing, continuing)
            continuing = 1
        else:
            continuing += 1
        prev = i

print(max_continuing)