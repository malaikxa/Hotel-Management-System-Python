letter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def variable(pattern):
    return (type(pattern) is str
            and pattern[0]=="?"
            and pattern[1]!="*"
            and pattern[1] in letter
            and len(pattern)>1 and " "
            not in pattern)
print(variable("?abc"))
print(variable("?h?i?oo"))
print(variable("???????????????"))
print(variable("?kk c??"))
print(variable("null"))
print(variable(0))
print(variable(" "))
print(variable("ininin"))
print(variable("?ii"))
print(variable("??99"))
print(variable("?whereeeee"))
print(variable(899))
print(variable("?kiki"))
print(variable("jiji"))
print(variable("?i?*"))
print(variable("?*ii"))
print(variable("*?pp"))
print(variable("hehehe"))
print(variable("?jkjen"))
print(variable("?9?k"))
print(variable("?kk"))
print(variable("?lijis"))
print(variable("?98yjn''"))


