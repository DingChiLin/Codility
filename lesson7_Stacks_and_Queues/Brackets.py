S = "{[()()]}"
#S = "([)()]"

def solution(S):
    stack = []
    for s in S:
        if stack and \
           ((stack[-1] == '(' and s == ')' ) or \
            (stack[-1] == '[' and s == ']' ) or \
            (stack[-1] == '{' and s == '}' )):
            stack.pop()
            continue

        stack.append(s)

    return 0 if stack else 1

print(solution(S))
