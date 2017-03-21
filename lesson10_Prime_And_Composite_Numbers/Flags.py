A = [1,5,3,4,3,4,1,2,3,4,6,2]
A = [5,1,5,1,5,1,5,1]

def create_peaks(A):
    peak = [False]*len(A)
    for idx, a in enumerate(A):
        if idx == 0:
            if a > A[idx+1]:
                peak[idx] = True
        elif idx == len(A)-1:
            if a > A[idx-1]:
                peak[idx] = True
        else:
            if a > A[idx-1] and a > A[idx+1]:
                peak[idx] = True
    return peak

