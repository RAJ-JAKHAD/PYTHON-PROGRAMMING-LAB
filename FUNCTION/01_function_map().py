# map function work on function,iteration and iteration will give in form tuple, list, and map print in tuple,set,list form. 
def add(x):
    return x
n=map(add,[1,2,3])
print(tuple(n))


# we perform map function as follows:-
def function(x,y):
    return x+y
n=map(function,('ayush','aman','jatin'),(' pandey',' tripathi',' gupta'))
print(list(n))

# map() with lambda function.

a=[1,2,3,4,5,6]
n=map(lambda x:x+3,a)
print(list(n))

# map() return none if given conditon not follow in given list,tuple,set.
def function(x):
    if x>2:                                    
        return x
n=map(function,(1,2,3,4))             
print(list(n))


# map() return true false if condition given in return if condtion true it give true and if false it give false in list,tuple.
def function(a):
    return a>2
n=map(function,(1,2,3,4))
print(tuple(n))
