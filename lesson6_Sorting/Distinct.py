A = [2,1,1,2,3,1]

def solution(A):
    sorted_a = sorted(A)
    distinct = 0
    tmp_value = -1
    for num in sorted_a:
        if num != tmp_value:
            distinct += 1
            tmp_value = num

    return distinct

print(solution(A))
