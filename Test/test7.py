x = 2
a = int("%s" %x)
b = int("%s%s" %(x,x))
c = int("%s%s%s" %(x,x,x))
d = int("%s%s%s%s" %(x,x,x,x))
print(a+b+c+d)