f=open('file1.txt')
v=0
a=f.read()
for i in a:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        v=v+1
print(v)
