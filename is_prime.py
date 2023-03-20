def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))

if __name__ == "__main__":
    n = 200
    primes = [i for i in range(n) if is_prime(i)]
    print(primes)