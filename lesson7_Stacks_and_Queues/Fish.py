A = [4,3,2,1,5]
B = [0,1,0,0,0]

def solution(A, B):
    stack = []
    direction = B[0]
    for i in range(0, len(A)):
        eated = False
        while stack and stack[-1][1] == 1 and B[i] == 0:
            if stack[-1][0] > A[i]:
               eated = True
               break
            else:
               stack.pop()

        if not eated: stack.append((A[i], B[i]))

    return len(stack)

print(solution(A, B))
