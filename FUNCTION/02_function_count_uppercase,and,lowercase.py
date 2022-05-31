def string(x):
    upr=0
    lwr=0
    d=0
    for i in x:
        if i.isupper():
            upr=upr+1
        elif i.islower():
            lwr=lwr+1
        elif i.isdigit():
            d=d+1
    print("upper",upr)
    print("lwr",lwr)
    print("digit",d)
n=input("enter the string")
string(n)
