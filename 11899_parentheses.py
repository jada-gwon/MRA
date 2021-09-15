# https://www.acmicpc.net/problem/11899

def parentheses(S):
    stack = []
    count = 0;
    for s in S:
        if s == '(':
            stack.append(s)
        elif len(stack) == 0:
            count += 1
        else:
            stack.pop()
    return count + len(stack)

S = input()
print(parentheses(S))
