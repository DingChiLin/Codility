A = [-9,-8,1,2,8,9]

def solution(A):
    a = sorted(A)
    first = a[0]*a[1]*a[-1]
    second = a[-1]*a[-2]*a[-3]
    return max(first, second)

print(solution(A))
