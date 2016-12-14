A = [4,3,4,4,4,2]
A = [4,4,2,5,3,4,4,4]
def solution(A):
    stack = []
    for a in A:
        if stack and stack[-1] != a:
            stack.pop()
        else:
            stack.append(a)

    if not stack:
        return 0

    candidate = stack[0]
    counter = 0
    for a in A:
        if a == candidate:
            counter += 1

    leader = None
    if counter > len(A)/2:
        leader = stack[0]

    length = len(A)
    left_leader_counter = 0
    left_length = 0
    equi_leader_counter = 0
    for i in range(0,length):
        if A[i] == leader:
            left_leader_counter += 1

        left_length += 1
        right_leader_counter = counter - left_leader_counter
        right_length = length - left_length

        if (left_leader_counter > left_length/2) and \
           (right_leader_counter > right_length/2):
               equi_leader_counter += 1

    return equi_leader_counter

print(solution(A))
