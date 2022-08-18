num= 600851475143
count=[]
def mul(count):
    mul=1
    for i in count:
        mul=mul*i
    return mul

for i in range(2,111):
    if(num%i==0 and mul(count)!=num):
        count.append(i)
        print(i)