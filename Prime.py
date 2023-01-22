# find prime numbers in a range
# Take a value from user, until which the prime numbers will be given
n = int(input("Enter the number: "))
for u in range(1, n+1):
    if u > 1:
        for i in range(2, u):
            if (u % i) == 0:
                break
        else:
            print(u)