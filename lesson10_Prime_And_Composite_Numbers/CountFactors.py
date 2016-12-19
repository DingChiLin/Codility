N = 24
def solution(A):
    result = 0
    i = 1
    while i*i < N:
        if N%i == 0:
            result += 2
        i += 1

    if i*i == N:
        result += 1

    return result

print(solution(A))
