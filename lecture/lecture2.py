##Expressions
a= max(2,4,3)

##非通常计算中的先乘除后加减
##按照expression tree走
from operator import add, mul
a=mul(add(2, mul(4,6)),add(3,5))
print(a)

##赋值永远可以覆盖，函数
def f(x):
    return 2+3

##types of expressions
#primitive expressions: 2, a, "hello"
#call expression: max(2,3) operator and operand

#discussion:
f=min
f=max
g,h=min,max
max=g
print(max(f(2,g(h(1,5),3)),4))

##environment diagrams
#execution rule for assignment statements
##evaluate all expressions to the right of = from left to right
##从上到下
a=1
b=2
b,a=a+b,b
print(a,b)

##call 调用
##add a local frame suqare
##bind the function's formal parameters to its arguments in that frame
##execute the body
def square(x):
    return mul(x,x)
print(square(2))

##looking up names in environments


##local frame/global frame
x=12
z=7
def f(y):
    x=3
    print(x,y,z)
print(f(7))