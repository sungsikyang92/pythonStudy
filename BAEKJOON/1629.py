# A, B, C = map(int, input().split(" "))
# result1 = A ** B
# result2 = result1 % C
# print(result2)
#


def multiple(a, b):
    if b == 1:
        return a % C
    else:
        temp = multiple(a, b // 2)
        if b % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * a % C

if __name__ == '__main__':
    A, B, C = map(int, input().split())

    result = multiple(A, B)
    print(result)