import math

def f(x):

    if x>3:
        s=0
        for i in range (1,18,2):
            s=s+(math.sin(x))**i

        return s
    else:
        s=15
        d=math.tan(x)
        for i in range(5):
            s=s+d
            d=math.tan(d)
        return s

a=float(input('a='))
b=float(input('b='))
print("f(a)=",f(a))
print("f(b)=",f(b))
u=max(f(a),f(b))
print ("U=",u)
