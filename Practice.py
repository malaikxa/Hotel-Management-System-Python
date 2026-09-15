# num=[3,6,8,4,7]
# def reverse(list):
#     new=[]
#     for i in range(len(list)-1,-1,-1):
#         new.append(list[i])
#     return new
# print(reverse(num))
from _ast import pattern

# word="hi im a student and i hate everything"
# count=0
# for i in word:
#  if i=='a'or i=='e' or i=='i'or i=='o'or i=='u':
#     count+=1
#
# print(count)
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def is_variable(pattern):
    return(type(pattern) is str and
           len(pattern)>1
           and pattern[0]=='?'
           and pattern[1] in letters
           and pattern[1]!='*'
           and ' ' not in pattern)



def match_var(var,replacement,bindings):
    binding=bindings.get(var)
    if not binding:
        bindings.update({var:replacement})
        return bindings
    if replacement==bindings[var]:
        return bindings
    return False
# print(match_var('?a',12,bindings={'?a':12}))
# print(match_var('?a',12,bindings={'?a':12}))
# print(match_var('?b',30,bindings={'?b':30}))
# print(match_var('?b',40,bindings={'?b':40}))
# print(match_var('?c',40,bindings={'?c':40}))


def contains_tokens(pattern):
    return type(pattern) is list and len(pattern)>0


def match_pattern(pattern,input,bindings=None):
    if bindings is False:
        return False
    if pattern==input:
        return bindings
    bindings=bindings or {}
    if is_variable(pattern):
        var=pattern[1:]
        return match_var(pattern,[input],bindings)
    elif contains_tokens(pattern) and contains_tokens(input):
           return match_pattern(pattern[1:],input[1:],
                   match_pattern(pattern[0],input[0],bindings))
    else:
        return False
print(match_pattern(['Ali','?a','sushi'],['Ali','Loves','sushi']))


def match(pattern,input):
    return match_pattern(pattern.split(), input.split())
print(match("hello ?a My name is ?d" , "hello boiss My name is vecna"))

def is_segment(pattern):
    return(type(pattern) is list and len(pattern[0])>2
           and pattern[0][0]=='?' and pattern[0][1]=='*'
           and pattern[0][2] in letters and ' 'not in pattern[0])

def match_seg(var, pattern, input,bindings):
    if not pattern:
        return match_var(var,input,bindings)
    word=pattern[0]
    try:
        pos=input[0:].index(word)
    except ValueError:
        return False
    var_match= match_var(var,input[:pos],dict(bindings))
    match= match_pattern(pattern,input[pos:],var_match)
    return match
print(match_seg('?*a',['hello','?a','whats up'],['hello','malaika','whats up'],bindings={}))
