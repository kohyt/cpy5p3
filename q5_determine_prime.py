# q5_determine_prime.py
# determine whether an integer is a prime number

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n > 2:
        for i in range(2,n):
            if n % i == 0:
                return False
            if i == n - 1:
                return True


n = 2
for i in range(100):
    for h in range(10):
        while is_prime(n) == False:
            n = n + 1
        print("{0:<8}".format(n), end = "")
        n = n + 1
    print("")



