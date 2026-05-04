def 나눠풀기(m,n):
    배수 = 1
    def 짝수(n):
        return n % 2 == 0
    def 홀수(n):
        return n % 2 == 1

    while not (m == 0 or n == 0):
        if 짝수(m) and 짝수(n):
            m , n, 배수 = m//2, n//2, 배수 *2
        elif 짝수(m) and 홀수(n):
            m = m//2
        elif 홀수(m) and 짝수(n):
            n = n//2
        elif m <= n:
            m, n, 배수 = m, (n-m)//2, 배수
        else:
            m, n, 배수 = (m-n)//2, n, 배수
    
    if 배수 == 1:
        print("배수가 없습니다.(최대공약수는 1입니다.)")

    if m == 0:
        return 배수 * n
    else:
        return 배수 * m

print(나눠풀기(10,10))
print(나눠풀기(10,11))
print(나눠풀기(11,11))