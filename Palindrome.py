num=int(input())
temp=num
res=0
i=0
while num:
    r=num%10
    num=num//10
    res=res*10+r
if res==temp:
    print("It Is Palindrome")
else:
    print("It Is Not Palindrome")
