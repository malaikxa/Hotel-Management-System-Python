def prime(*check):
    num=[]
    count=0
    for i in check:
        if i>1:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                 num.append(i)
                 count+=1

    print(count)
    return num

print(prime(6,9,4,2,5,7))
