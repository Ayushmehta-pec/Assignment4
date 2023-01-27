n=int(input("enter no of candies"))

for n in range(1,n+1):
    if n%5==2 and n%6==3 and n%7==2:
        print(n)