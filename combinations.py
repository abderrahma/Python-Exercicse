def factorial(num):    
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)
def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
 