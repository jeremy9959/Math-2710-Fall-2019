
def fermat(m):
    s=1
    k=3
    N=2**(2**m)+1
    print('{}th Fermat Number = {}' .format(m,N))
    print('k\t\t3**k mod N')
    for i in range(2**m):
        s*=2
        k=(k*k) % N
        print('{}\t\t{}'.format(s,(k % N)))
    if k!=1:
        print('Composite!')
    else:
        print('Might be prime')


m = input("Which Fermat Number do you want to test: ")
fermat(int(m))
