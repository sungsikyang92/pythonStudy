def binsearch(A, x):
    n = len(A)
    lo = -1
    hi = n

    while (lo + 1 < hi):
        mid = (lo + hi) / 2
        if A[mid] < x:
            lo = mid
        else:
            hi = mid

    return hi

A = [1,2,3,4,10]
a = 12
print(binsearch(A, a))