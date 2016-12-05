A = [1,5,2,1,4,0]

def solution(A):
    uppers = []
    lowers = []
    for idx, a in enumerate(A):
        uppers.append(idx + a)
        lowers.append(idx - a)

    uppers.sort()
    lowers.sort()

    low_index = 0
    counter = 0
    intersects = 0
    for up in uppers:
        while low_index < len(lowers) and lowers[low_index] <= up:
            low_index += 1
            intersects += counter
            if(intersects > 10000000 ): return -1
            counter += 1

        counter -= 1

    return intersects

print(solution(A))
