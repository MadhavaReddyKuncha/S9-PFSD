import datetime

num = int(input("entre a number a"))
sum = 0
n = num

while n != 0:
    sum = sum * 10 + n % 10
    n = n // 10

if sum == num:
    print("panlidrome")
else:
    print("not")

print(datetime.datetime.now())

