'''
x = int(input("Enter a number"))
i = 1; count=0;
while(i<=x):
    if(x%i==0):
       count+=1;
    i+=1;
if(count==2):
    print("Prime")
else:
    print("not prime")
    
    
x = int(input("Enter a number"))
i = 2; count=0;
while(i<x):
    if(x%i==0):
       count+=1;
    i+=1;
if(count==0):
    print("Prime")
else:
    print("not prime")'''
    
x = int(input("Enter a number"))
i = 2; count=0;
while(i<x/2):
    if(x%i==0):
       count+=1;
    i+=1;
if(count==0):
    print("Prime")
else:
    print("not prime")
    
    