A = 6
B = 11
K = 2

def solution(A, B, K):
    return B//K - A//K + int(A%K == 0)

print(solution(A, B, K))
