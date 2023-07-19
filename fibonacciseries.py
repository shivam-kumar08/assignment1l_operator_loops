n=int(input("enter the number : "))
a = 0
b = 1
if n<0:
    print("invalid number ")
elif n==0:
    print(a)
elif n==1:
    print(b)

else:
    print(b)
    for i in range(n):
        c=a+b
        a=b
        b= c
        print(b)