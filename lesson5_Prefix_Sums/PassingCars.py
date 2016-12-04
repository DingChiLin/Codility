A = [0,1,0,1,1]

def solution(A):
    zero_sum = 0
    pass_sum = 0
    for a in A:
        if a == 0:
            zero_sum += 1
        else:
            pass_sum += zero_sum
            if pass_sum > 1000000000: return -1

    return pass_sum

print(solution(A))
