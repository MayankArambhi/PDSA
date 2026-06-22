# suppose n does not divide m
# m = qn + r
# d divides both m and n
# m = ad, n = bd
# m = qn+r => ad = q(bd) + r
# r must be form of cd

def gcd(m,n):
    a, b = (max(m,n),min(m,n))
    if a%b == 0:
        return b
    return gcd(b,a%b)

print(gcd(79124374,28714921412))