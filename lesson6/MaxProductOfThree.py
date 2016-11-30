A = [-3,1,2,-2,5,6]
A = [-5, -6, -4, -7, -10]
import itertools

def solution(A):
    a = sorted(A, key=lambda x: -abs(x))
    if len(filter(lambda x: x<0, a)) == len(a):
        last_3 = a[-3:]
        return reduce(lambda x,y :x*y, last_3)

    first_3 = a[0:3]

    num_of_neg = len(filter(lambda x: x<0, first_3))
    if num_of_neg == 1 or num_of_neg == 3:
        if len(a) == 4:
            first_3.append(a[3])
        if len(a) >= 5:
            max_pos = 0
            max_neg = 0
            for i in range(3,len(a)):
                if a[i] > 0 and max_pos == 0:
                    max_pos = a[i]
                if a[i] < 0 and max_neg == 0:
                    max_neg = a[i]
            first_3 += [max_pos, max_neg]

        max_prod = -1000**3
        for perm in itertools.combinations(first_3, 3):
            prod = reduce(lambda x,y: x*y, perm)
            if max_prod < prod:
               max_prod = prod

        return max_prod

    else:
       return reduce(lambda x, y: x*y, first_3)

print(solution(A))
