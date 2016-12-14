A = [3,4,3,2,3,-1,3,3]

def solution(A):
    stack = []
    for a in A:
        if stack and stack[-1] != a:
            stack.pop()
        else:
            stack.append(a)

    if not stack:
        return -1

    candidate = stack[0]

    counter = 0
    for idx, a in enumerate(A):
        if a == candidate:
            counter += 1
            if counter > int(len(A)/2):
                return idx

    return -1


print(solution(A))
