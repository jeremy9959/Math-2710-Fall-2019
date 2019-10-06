
def next_row(row0,row1):
    q = row0[2]//row1[2]
    r = row0[2]-q*row1[2]
    x = row0[0]-q*row1[0]
    y = row0[1]-q*row1[1]
    return [x,y,r,q]

def print_row(x):
    print('|{:15}|{:15}|{:15}|{:15}|'.format(*x))

print('Euclidean Algorithm')
a = int(input('Enter a: '))
b=-1
while b<0:
    b = int(input('Enter b>0: ')) 


row0 = [1,0,a,0]
row1 = [0,1,b,0]


print('|{:15}|{:15}|{:15}|{:15}|'.format('a','b','r','q'))
print('|'+'-'*15+'|'+'-'*15+'|'+'-'*15+'|'+'-'*15+'|')
print_row(row0)
print_row(row1)
while True:
    row = next_row(row0,row1)
    if row[2]==0:
        break
    print_row(row)
    row1,row0 = row, row1

      
      
