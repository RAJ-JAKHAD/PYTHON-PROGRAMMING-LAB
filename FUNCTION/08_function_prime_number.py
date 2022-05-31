'''def prime(x):
    sum=0
    for i in range(1,x+1):
        if x%i==0:
            sum=sum+1
    return sum==2
n=int(input())
d=prime(n)
print(d)
'''
def prime(a):
    count=0
    if a>1:
        for i in range(2,a):
            if a%i==0:
                count=count+1
                print(count)
        else:
            print("false")
    else:
        print("false")
n=int(input("enter the number"))
prime(n)
