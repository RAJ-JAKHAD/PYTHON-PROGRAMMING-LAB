def area(l,b):
    n=l*b
    return n
def perimeter(l,b):
    f=2*(l+b)
    return f
n1=int(input("enter length"))
n2=int(input("enter the breadth"))
d,f=area(n1,n2),perimeter(n1,n2)
print('area of rectangle=',d)
print("arae of perimeetr=",f)
