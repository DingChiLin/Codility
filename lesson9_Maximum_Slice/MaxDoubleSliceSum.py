A = [3,2,6,-1,4,5,-1,2]
#A = [5,5,5]
def solution(A):
    length = len(A)
    left_max_slices = [None]*length
    right_max_slices = [None]*length

    for i in range(0, length):
        if i < 2:
            left_max_slices[i] = 0
            continue
        left_max_slices[i] = max(0, left_max_slices[i-1] + A[i-1])

    for i in range(length-1, -1, -1):
        if i > length-3:
            right_max_slices[i] = 0
            continue
        right_max_slices[i] = max(0, right_max_slices[i+1] + A[i+1])

    max_slice = 0
    for i in range(1, length-1):
        max_slice = max(max_slice, left_max_slices[i] + right_max_slices[i])

    return max_slice


print(solution(A))
