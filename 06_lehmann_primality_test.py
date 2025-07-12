import random

def lehmann_primality_test(P, k=20):
    
    if P == 1:
        return False
    if P == 2:
        return P == 2

    if P % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, P - 2)
        r = pow(a, (P - 1) // 2, P)

        # r must be either 1 or P-1 modulo P
        if r != 1 and r != P - 1:
            print(f"Composite witness found: a = {a}, r = {r}")
            return False 

    return True

P = int(input("Enter a number to test for primality: "))

if lehmann_primality_test(P, k=20):
    print(f"{P} is probably prime.")
else:
    print(f"{P} is composite.")
