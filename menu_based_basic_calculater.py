n1=int(input("enter first numer :"))
n2=int(input("enter second numer :"))

print("MENU:-\n"
        "1.ADDITION\n"
        "2.SUBTRACTION\n"
        "3.MULTIPLICATION\n"
        "4.DIVISION\n"
        "5.EXIT\n")
ch=int(input("enter a number for what to do from given menu :- "))
if(ch==1):
    print("The addition of ",n1,'and',n2,'is',n1+n2)
elif(ch==2):
    print("The subtraction of ",n1,'and',n2,'is',n1-n2)
elif(ch==3):
    print("The multiplication of ",n1,'and',n2,'is',n1*n2)
elif(ch==4):
    print("The division of ",n1,'and',n2,'is',n1/n2)
elif(ch==5):
    print("EXITED")
else:
    print('INVALID INPUT')
          
