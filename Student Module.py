def unknown(eqs):
    for eq in eqs:
        ans=unknown2(eq)
        count=ans[1]
        var=ans[0]
        if count==1:
          return var,eq
    return None,[]
def reverse(op):
    if op=='+':
        return '-'
    elif op=='-':
        return '+'
    elif op=='*':
        return '/'
    elif op=='/':
        return '*'



letters=['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz']
def unknown2(eqs):
    c=0
    var=None
    for item in eqs:
        if type(item) is list:
            ans=unknown2(item)
            c+=ans[1]
            if ans[1]!=0:
                var=ans[0]
        else:
            flag=False
    for ch in item:
                if ch in letters:
                    flag=True
                if flag==True:
                    c+=1
                    var=item
    return var,c
print(unknown([['a','=','33','+','20'],['b','=','30','-','22']]))
print(reverse('*'))
print(unknown2(['x','=','45','+','2']))