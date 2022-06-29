n=int(input())
r=0
temp=n
while n:
    rem=n%10
    r=r*10+rem
    n=n//10
if r==temp:
    print("True")
else:
    print("False")