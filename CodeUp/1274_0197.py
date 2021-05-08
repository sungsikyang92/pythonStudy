num = int(input())
isPrime = "prime"

for x in range(2, num):
    if num % x == 0:
        isPrime = "not prime"
        break
print(isPrime)