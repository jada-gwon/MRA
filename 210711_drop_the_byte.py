S = input(); input()
SIZE = {"char": 2, "int": 8, "long_long": 16}
i = 0
for base in input().split():
    size = SIZE[base]
    print(int(S[i:i+size], 16), end=' ')
    i += size