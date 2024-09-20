def prime_factorization(n):
    i = 2
    factors = []
    
    # Checking for each number from 2 to sqrt(n)
    while i * i <= n:
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            factors.append((i, count))
        i += 1
    
    # If there's any prime factor greater than sqrt(n)
    if n > 1:
        factors.append((n, 1))

    return factors

# Example usage:
print(prime_factorization(60))  # Output: [(2, 2), (3, 1), (5, 1)]
