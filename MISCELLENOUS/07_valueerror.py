try:
    a=3
    b=[]
    b.remove(a)
    print(b)

except ValueError:
    print("error raised in try block")
