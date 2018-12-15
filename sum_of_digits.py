count = 0
def countdigit(n):
    if n<10 :
        return n;
    else:
        count=n%10+countdigit(n/10)
        return count
a=input("Enter the number \t")
print "output is :\n",countdigit(a)

