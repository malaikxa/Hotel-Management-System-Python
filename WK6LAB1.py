# def r_func(a):
#     if a==1:
#      return 1
#     else:
#      return a*r_func(a-1)
# print(r_func(5))

# num=int(input("Enter a number"))
# print(num)
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)
#     i+1



def table(num, i=1):
    if i > 10:
        return
    print(num, "x", i, "=", num * i)
    table(num, i + 1)
n = int(input("Enter a number: "))
table(n)