from collections import deque

A = [1,7,3,2,4,5,9,8,6]

def solution(A):
    return list(quick_sort(deque(A)))

def quick_sort(A):
    if len(A) <= 1:
        return deque(A)
    else:
        pivot = A.popleft()
        a_left = deque()
        a_right = deque()
        for a in A:
            if a <= pivot:
                a_left.append(a)
            else:
                a_right.append(a)

        result = quick_sort(a_left)
        result.append(pivot)
        result.extend(quick_sort(a_right))
        return result

print(solution(A))
