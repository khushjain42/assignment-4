x=int(input('enter year no'))
y=x%4
z=x%100
a=x%400
if y==0:
    if z==0:
        if a==0:
            print('leap year')
        else:
            print('not a leap year')
else:
    print('not a leap year')
