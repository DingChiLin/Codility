import sys

N = 30
N = 36
def solution(N):
    result = 0
    i = 1

    min_area = sys.maxint
    while i*i <= N:
        if N%i == 0:
           min_area = min(min_area, (N/i)*2 + i*2)
        i += 1

    return min_area

print(solution(N))
