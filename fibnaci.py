a,b,c=0,1,0
print "Fibonaci series:\n",a,"\n",b
l=10
while(l>1):
    c=a+b
    a=b;
    b=c;
    l=l-1
    print "\n",c
