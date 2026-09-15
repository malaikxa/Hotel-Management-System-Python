main=input("enter main string")
sub=input("enter substring")
if main.__contains__(sub):
# # if sub in main: (you can write it like this too)
    print("yes")
else:
    print("no")

    print(range(9))
num=int(input("Enter a number: "))
print(num)
for i in range(1,11):
    print(num*i) #prints table

for i in range(10,1,-1):
    print(i) #reverse order

num=input("enter a number")
for k in range(1,11):
    print(num) #prints number
num = int(input("Enter a number: "))
rno = num
sum = 0

while num != 0:
    rem = num % 10
    sum = sum + (rem ** 3)
    num = num // 10 #armstrong numbers

sum=0
for x in range (1,11):
    sum+=x
    print(sum) #Adds digits
num=int(input("Enter a number: "))
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)  #reverse