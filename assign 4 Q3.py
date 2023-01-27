import random
for i in range(1,10):
    x1=random.randint(1,10)
    x2=random.randint(1,10)
    x=x1*x2
    print(x1,'x',x2,"=")
    y=int(input("enter your answer"))
    if x==y:
        print('correct')
    else:
        print('wrong,'+'the answer is-',x)
    i=i+1
