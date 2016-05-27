height = input('Enter triangle height: ')
h = int(height)

for i in range(h, 0, -1):
    print('*'*i + ' '*(h*2-i*2)+ '*'*i)

for i in range(2,h+1):
    print('*'*i + ' '*(h*2-i*2)+ '*'*i)
    