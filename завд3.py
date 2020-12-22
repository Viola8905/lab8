def recursia(n):
    if n == 0:
        return 1
    elif n==1:
        return 1
  
    else:
        return ( recursia(n - 1) +  recursia(n - 2))


num = int(input(" введіть значення n:"))
print(recursia(num))
