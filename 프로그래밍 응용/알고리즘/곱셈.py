def 곱셈(m,n):
    if n > 0:
        return m+곱셈(m,n-1)
    else:
        return 0

print(곱셈(3,6))