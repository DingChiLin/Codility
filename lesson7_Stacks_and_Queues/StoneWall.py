A = [8,8,5,7,9,8,7,4,8]

def solution(A):

    count = 0
    stack = []
    for a in A:
        while stack and a < stack[-1]:
            stack.pop()

        if stack and a == stack[-1]:
            continue
        else:
            stack.append(a)
            count += 1

    return count

print(solution(A))
