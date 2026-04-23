def 나눠풀기(m,n):

    def 짝수(n):
        return n % 2 == 0
    def 홀수(n):
        return n % 2 == 1

    def 반복(m,n,배수):
        if not (m == 0 or n == 0):
            if 짝수(m) and 짝수(n):
                return 반복(m//2,n//2, 배수*2)
            elif 짝수(m) and 홀수(n):
                return 반복(m//2,n, 배수)
            elif 홀수(m) and 짝수(n):
                return 반복(m,n//2, 배수)
            elif m <= n:
                return 반복(m, (n-m)//2, 배수)
            else:
                return 반복((m-n)//2, n, 배수)
        else:
            if m == 0:
                return 배수 * n
            else:
                return 배수 * m
    
    return 반복(m,n,1)

print(나눠풀기(10,10))
print(나눠풀기(10,11))
print(나눠풀기(11,11))
            