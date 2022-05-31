def char(x):
    vow=0
    conso=0
    for i in range(len(x)):
        if x[i] in ['a','e','i','o','u']:
            vow=vow+1
        else:
            conso=conso+1
    
    print("vowel",vow)
    print("consonent=",conso)
a=input("enter the word")
char(a)
