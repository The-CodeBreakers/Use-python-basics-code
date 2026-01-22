a=int(input("Enter the 1st number = "))
b=int(input("Enter the 2nd number = "))
c=int(input("Enter the number 3rd = "))
d=int(input("Enter the 4th number = "))

if(a>b)and (a>c) and (a>d):
    print("A is bigest number ")
elif(b>a) and (b>c)  and (b>d):
    print("B is bigest number ")
elif(c>b)and (c>a) and (c>d):
    print("C is biggest number ")
else:
    print("D id bigest number ")