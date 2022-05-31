try:
    n={1:2,4:5,7:9}
    print(n[3])
except KeyError:
    print("exception raised in try block")
finally:
    print("it exicute every condition")
