a = [2,3,1,5]

length = len(a) + 1
sum = (length+1)*length/2
for i in a:
    sum -= i

print(sum)
