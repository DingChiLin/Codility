A = [10,2,5,1,8,20]

def solution(A):
    a = sorted(A)
    for i in range(0, len(a)-2):
        p = a[i]
        q = a[i+1]
        r = a[i+2]
        if p + q > r:
            return 1

    return 0

print(solution(A))
