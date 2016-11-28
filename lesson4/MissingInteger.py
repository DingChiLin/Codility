A = [1,3,6,4,1,2]

def run(A):
    length = len(A)
    list = [0]*(length+1)

    for a in A:
        if a > length or a < 1:
            continue;

        list[a] = 1

    for idx, val in enumerate(list):
        if idx != 0 and val == 0:
            return idx;

    return length + 1

print(run(A))
