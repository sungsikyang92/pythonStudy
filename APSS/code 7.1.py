def fastSum(n: int):
    if(n == 1):
        return 1;
    elif(n % 2 == 1):
        return fastSum(n-1)+n;
    else:
        return 2*fastSum(n/2) + (n/2)*(n/2);

x = int(input())
print(fastSum(x))