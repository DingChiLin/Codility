A = [1,3,2,4]
B = [1,4,3]
C = [1,2,5]

def run(A):
    length = len(A)
    expect_sum = length * (length + 1) / 2
    list = [0]*(length + 1)

    sum = 0
    for a in A:
        sum += a
        if a > length:
            return 0

        if list[a] == 1: #duplicate
            return 0

        list[a] = 1

    if sum != expect_sum:
        return 0

    return 1

print(run(A))
print(run(B))


