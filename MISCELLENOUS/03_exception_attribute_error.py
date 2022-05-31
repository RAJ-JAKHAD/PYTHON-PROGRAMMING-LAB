try:
    a='hello'
    print(a.n)
except AttributeError:
    print("error is raised in try block")
else:
    print("error is not raised in try")
