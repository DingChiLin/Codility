A = [1,3,1,4,2,3,5,4]
X = 5

def run(A, X):
    list = [0]*X

    step = 0
    for idx, a in enumerate(A):
        if list[a-1] == 0:
            step += 1

        list[a-1] = 1

        if step == X:
            return idx

    return -1

print(run(A, X))

