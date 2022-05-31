f=open("file1.txt")
count=0
d=0
a=f.read()
for i in a:
    if i.isupper():
        count+=1
    elif i.isdigit():
        d+=1
print(count)
print(d)
