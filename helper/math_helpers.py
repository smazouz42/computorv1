def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def _sqrt(n, precision=1e-10):
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if n == 0 or n == 1:
        return n
    
    low, high = 0, n
    while high - low > precision:
        mid = (low + high) / 2
        if mid * mid > n:
            high = mid
        else:
            low = mid
    return (low + high) / 2