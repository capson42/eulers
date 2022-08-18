num=600851475143
count=[]
def mul(count):
    mul=1
    for i in count:
        mul=mul*i
    return mul

for i in range(2,600851475143):
    if(num%i==0):
        count.append(i)
        if mul(count)==num:
            break

print(max(count))
