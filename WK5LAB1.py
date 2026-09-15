#Arbitary arguments
#keyword arguments
#arbitary keyword arguments


# def add(*args):
#
#     result=args[0]
#     for i in range(1,len(args)):
#         result+=args[i]
#
#     print(result)
#
#
# add(20,5)
# add(11,9)
#
#
# def sub(*values):
#     result=values[0]
#     for i in range(1,len(values)):
#         result-=values[i]
#
#     print(result)
#
# sub(20,8)
# sub(11,9)

def add(*args):
    total=0
    for i in args:
     total=total+i
     print("sum=", total)
add(1,2,79,98,89)
add(68,38,4,648,84,8794)

