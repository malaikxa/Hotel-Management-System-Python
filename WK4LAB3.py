#functions
def  menu(): #keyword "def" for function

    print("Press 1 to add values")
    print("Press 2 to subtract values")
    print("Press 3 to multiply values")
    print("Press 4 to divide values")
    print("Press 5 to exit")

def sum(v1,v2):
  print(v1+v2)


def sub(v1,v2):
  print(v1-v2)



def mul(v1,v2):
  print(v1*v2)

def div(v1,v2):
    print(v1/v2)

while True:
 menu()
 choice=int(input("Enter your choice: "))
 if choice==1:
    add1=int(input("Enter number "))
    add2=int(input("Enter number "))
    sum(add1,add2)
 elif choice==2:
    sub1=int(input("Enter number "))
    sub2=int(input("Enter number "))
    sub(sub1,sub2)
 elif choice==3:
    mul1=int(input("Enter number "))
    mul2=int(input("Enter number "))
    mul(mul1,mul2)
 elif choice==4:
    div1=int(input("Enter number "))
    div2=int(input("Enter number "))
    div(div1,div2)
 else:
    print("exiting")
    break