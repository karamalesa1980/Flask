def fact(x):
    return 1 if x==0 else reduce(lambda x,y:x*y,xrange(1,x+1))


c=fact(5)
print(c)