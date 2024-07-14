def fact(n):
    if n==0 or n==1:
        return n
    else:
        print(n)
        return n* fact(n-1)
    
n=int(input("number "))
print(fact(n))