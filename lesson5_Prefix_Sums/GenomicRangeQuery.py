S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]

def solution(S, P, Q):
    length = len(S)
    a_psum = [0]*(length+1) # last as -1
    c_psum = [0]*(length+1)
    g_psum = [0]*(length+1)
    t_psum = [0]*(length+1)

    for idx, s in enumerate(S):
        if idx != 0:
            a_psum[idx] = a_psum[idx-1]
            c_psum[idx] = c_psum[idx-1]
            g_psum[idx] = g_psum[idx-1]
            t_psum[idx] = t_psum[idx-1]

        if s == 'A':
            a_psum[idx] += 1
        elif s == 'C':
            c_psum[idx] += 1
        elif s == 'G':
            g_psum[idx] += 1
        elif s == 'T':
            t_psum[idx] += 1

    result = []
    for i in range(0, len(P)):
        p = P[i]
        q = Q[i]

        if (a_psum[q] - a_psum[p-1] != 0):
            result.append(1)
        elif (c_psum[q] - c_psum[p-1] != 0):
            result.append(2)
        elif (g_psum[q] - g_psum[p-1] != 0):
            result.append(3)
        elif (t_psum[q] - t_psum[p-1] != 0):
            result.append(4)

    return result

print(solution(S, P, Q))

