def 더하기범위(m,n):
    def 반복(m,total):
        if m <= n:
            return 반복(m+1,total + m)
        else:
            return total
    return 반복(m,0)

def sumarage(m,n):
    total = 0
    while m <= n:
        total += m
        m += 1
    return total

print(더하기범위(1,8))
print(sumarage(1,8))