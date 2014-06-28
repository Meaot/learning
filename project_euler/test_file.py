#
# This is a testing file. To test small bits of code.
#
multFive = [5, 10, 15]
for k in multFive:
    if k%3 == 0:
        del multFive[multFive.index(k)]

print multFive