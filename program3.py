#sum of first 2000 odd numbers
a=1
i=1
sum=0
while a<=2000:
    if i%2!=0:
        sum+=i
        a+=1
    i+=1
print(sum)