from math import gcd
def solution(numer1, denom1, numer2, denom2):
    a = numer1 * denom2 + numer2 * denom1
    b = denom1 * denom2
    ans = lambda a,b : (a // gcd(a,b), b // gcd(a,b))
    return list(ans(a,b))

print(solution(1,2,3,4))