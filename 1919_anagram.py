# https://www.acmicpc.net/problem/1919

def make_anagram(S, T):
    S.sort()
    T.sort()
    i = 0
    for s in S:
        if s in T:
            T.remove(s)
        else:
            i += 1
    return len(T) + i

S = list(input())
T = list(input())
print(make_anagram(S, T))
