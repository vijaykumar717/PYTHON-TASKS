number=int(input("enter a number"))
sum=0
while(0<number):
    remainder=number%10
    sum=sum+remainder
    number=number//10
print(sum)
   
