n = 0.45
while n != int(n):
    n *= 10
print(n)
 
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)