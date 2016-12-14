A = [3,2,-6,4,0]
A = [-1,-2,-3]
def solution(A):
    max_slice = 0
    max_ending = 0
    max_negative = -1000000
    negative_count = 0
    for a in A:
        if(a < 0):
            max_negative = max(max_negative, a)
            negative_count += 1

        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)

    if(negative_count == len(A)): return max_negative
    return max_slice

print(solution(A))
