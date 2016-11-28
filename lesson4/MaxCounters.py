N = 5
A = [3,4,4,6,1,4,4]

def solution(N, A):
    counter = [0]*N
    last_max = 0
    max_value = 0

    for a in A:
        if a <= N:
            if counter[a-1] < last_max:
                counter[a-1] = last_max

            counter[a-1] += 1

            if counter[a-1] > max_value:
                max_value = counter[a-1]

        else:
            last_max = max_value

    for i in range(0, N):
        if counter[i] <= last_max:
            counter[i] = last_max

    return counter

print(solution(N, A))
