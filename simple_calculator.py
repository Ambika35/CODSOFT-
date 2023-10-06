#TASK -1 To make simple calculator by taking choice of no.s and operation from user and displaying the result
#@codsoft intership opportunity
a=float(input("enter first no. for operation:"));
b=float(input("enter second no. for operation:"));
symbol=input("enter operator of your choice from[+,-,*,/,%]:");
result=0;
if symbol=='+':
    result=a+b;
elif symbol=='-':
    result=a-b;
elif symbol=='*':
    result=a*b;
elif symbol=='/':
    result=a/b;
elif symbol=='%':
    result=a%b;
else:
    print("enter a valid choice");
print(a,symbol,b,'=',result);
print("the result for the operation is",result);


    
    
