import random as r
#the sample() method returns a list with a randomly selection of a specified number of items from a sequnce.
#This method does not change the original sequence.
# we can not give the size greater than orginal size.
a=[1,'ayush',9]
n=r.sample(a,k=3)
print(n)
