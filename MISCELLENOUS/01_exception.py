a=6
b='d'
try:
    print(a+b)
except TypeError:
    print("hello everyone")
else:
    print("it exicute when no exception raised in try block")
finally:
    print("it exicute when exception occur or not ")
