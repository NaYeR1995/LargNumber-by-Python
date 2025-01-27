def largeNum1():
    a = input('Pleas input the 1Th Number: ')
    b = input('Pleas input the 2nd Number: ')
    c = input('Pleas input the 3rd Number: ')
    if a > b:
        if a >= c:
            print(a) 
        else:
            print(c)
    else:
        if b >= c:
            print(b)
        else:
            print(c)

largeNum1()



def largeNum2():
    a = input('Pleas input the 1Th Number: ')
    b = input('Pleas input the 2nd Number: ')
    c = input('Pleas input the 3rd Number: ')

    if (a >= b) and (a >= c):
        print(a)
    elif (b >= a) and (b >= c):
        print(b)
    else:
        print(c)

largeNum2()

