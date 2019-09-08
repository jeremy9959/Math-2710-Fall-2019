print('Euclidean Algorithm')
a = int(input('Enter a: '))
b=-1
while b<0:
    b = int(input('Enter b>0: ')) 

q =  a//b
r = a-b*q

print('{:>20}={:>20}*{:>20} + {:>20}'.format(a,q,b,r))
while r>0:
    a, b = b, r
    q = a//b
    r = a - b*q
    print('{:>20}={:>20}*{:>20} + {:>20}'.format(a,q,b,r))

print('GCD = {}'.format(b))
