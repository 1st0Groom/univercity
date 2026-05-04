def power(b,n):
    def 반복(b,n,곱결과):
        if n > 0:
            return 반복(b,n-1,곱결과*b)
        else:
            return 곱결과
    return 반복(b,n,1)

print(power(2,10))   