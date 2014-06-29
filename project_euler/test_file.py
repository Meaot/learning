#
# This is a testing file. To test small bits of code.
#
# def isprime(n):
#     i = 2
#     while i < n:
#         if n%i == 0:
#             return False
#         else:
#             i += 1
#     if n == i:
#         return True
            
# print isprime(9)

def isprime(n):
    for i in range(2, (n-1)):
        if n % i == 0:
            return False
    return True

print isprime(9)