height = input("Enter height: ")
h = int(height)

for i in range(1,h+1):
    triangle = '*'
    padding = '{:>{b}}'
    print(padding.format(triangle*i,b=h))
    