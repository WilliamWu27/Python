def isPrime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
            
    return True
            
            
if __name__ == '__main__':
    n = 29
    print(isPrime(29))

    n = 25
    print(isPrime(25))

    n = 1
    print(isPrime(n))