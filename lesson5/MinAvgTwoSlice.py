A = [4,2,2,5,1,5,8]

def solution(A):

    min_mean = 10000
    min_index = 0
    total_mean = A[0]
    total_len = 1

    for i in range(0, len(A)-1):
        a = float(A[i])
        b = float(A[i+1])
        tmp_mean = (a+b)/2
        total_mean = (total_mean*total_len + b) / (total_len + 1)

        if tmp_mean < total_mean:
            total_mean = tmp_mean
            total_len = 2
            if tmp_mean < min_mean:
                min_mean = tmp_mean
                min_index = i
        else:
            if total_mean < min_mean:
                min_mean = total_mean
                min_index = i - total_len + 1

            total_len += 1

    return min_index


print(solution(A))
