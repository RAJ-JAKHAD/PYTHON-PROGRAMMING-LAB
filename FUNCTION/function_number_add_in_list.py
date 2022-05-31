def add(lst,a):
    n=[]
    for i in lst:
        d=i+a
        n.append(d)
    print(n)
a=[1,2,3,4]
b=2
add(a,b)


or


#by lambda function

a=[1,2,3,4]
result=map(lambda x:x+3,a)
print(list(result))
