#sum of first 2000 prime numbers
i=2
a=1
sum=0
while a<=2000:
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1
            i+=1
            break
    if count==0:
        a+=1
        sum+=i
        i+=1
print(sum)