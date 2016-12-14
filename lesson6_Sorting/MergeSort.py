from collections import deque

A = [1,7,3,2,4,5,9,8,6]

def solution(A):
    return list(merge_sort(A))

def merge_sort(A):
    length = len(A)
    if length == 1:
        return deque(A)
    else:
        a_left = merge_sort(A[0:length//2])
        a_right = merge_sort(A[length//2:])
        result = deque()
        while len(a_left) != 0 and len(a_right) != 0:
            if a_left[0] <= a_right[0]:
                result.append(a_left.popleft())
            else:
                result.append(a_right.popleft())

        if len(a_left) == 0:
            result += a_right
        elif len(a_right) == 0:
            result += a_left

        return result

print(solution(A))
