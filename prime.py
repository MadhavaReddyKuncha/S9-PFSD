num = int(input("entre number to check prime or not"))
sum=0
i=1
for i in range(i, num):
    if num%i == 0:
        sum=sum+1
if sum<=2:
    print("prime")
else :
    print("not prime")