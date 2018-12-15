a=input("Enter the number \t")

def rev(n):
    if(n <10) :
        print n;
    else :
        print n%10
        rev(n/10)
        
rev(a)