limit = int(input('Maximum number to factorise: '))
star = ''
for i in range(1, limit+1):
    for j in range(1, limit+1):
        if i%j == 0:
            star = star+'* '
        else:
            star = star+'- '
    if i==limit:
        break
    else:
        star = star+'\n'
print(star)