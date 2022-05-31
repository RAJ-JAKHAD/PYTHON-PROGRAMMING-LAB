def perfect(x):
    s=0
    for i in range(1,x):
        if x%i==0:
            s=s+i
    return s==x
    
a=int(input("enter the number"))
n=perfect(a)
print(n)
