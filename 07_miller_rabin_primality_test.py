
import random

def is_prime(n, k=5):  # k = number of testing rounds
    # Step 1: Handle small numbers
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Step 2: Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Step 3: Test k times
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # compute (a^d) % n

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # composite

    return True  # probably prime


P = int(input("Enter a number to check if it is prime: "))
if is_prime(P):
    print(f"{P} is probably a prime number.")
else:
    print(f"{P} is not a prime number.")
