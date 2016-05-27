def mul_table(num,N):
    n=0
    while n<N:
        result = (n+1)*num            
        print_result = str(n+1) + " * " + str(num)+ " = "+ str(result)
        n = n+1
        print(print_result)

num=input("Enter the number for 'num': ")
N=input("Enter the number for 'N': ")

if not num.isdigit() or not N.isdigit() or int(num) < 0 or int(N) < 0 or int(num)==0:
    print("Invalid input")
else:
    num = int(num)
    N = int(N)
    mul_table(num,N)

