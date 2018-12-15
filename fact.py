def fact(n):
    if n == 0: 
        return 1
    else:
        return n* fact(n-1)

a=input("Enter the number to be factorial \n")
print "Factorial value:",fact(a)