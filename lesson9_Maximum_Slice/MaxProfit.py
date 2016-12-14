A = [23171,21011,21123,21366,21013,21367]

def solution(A):
    if not A: return 0
    max_profit = 0
    min_ending = A[0]
    for i in range(1,len(A)):
        if (i == 0): continue

        profit = A[i] - min_ending
        if(profit < 0): min_ending = A[i]
        max_profit = max(max_profit, profit)

    if(max_profit < 0): return 0
    return max_profit

print(solution(A))
