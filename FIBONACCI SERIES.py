n=int(input()) # takes integer type input from user

a=0 #initialising first and
b=1 #second numbers in the series

if n==1:# for printing only first number in series
    print(a)
    
elif n>1: # for printing numbers greater than 1 in series
    
    #printing 0 and 1 as these are always the starting values
    print(a,end=' ')
    print(b,end=' ')
    
    for i in range(3,n+1):#printing from third number to the given range
        
        c=a+b #adding the last two numbers in the series and storing result in c
        
        print(c,end=' ') # printing contents in c

        #swapping numbers to update the new last two numbers
        a=b
        b=c
