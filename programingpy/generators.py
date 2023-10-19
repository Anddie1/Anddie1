def mygenerator(x):
    for x in range(1,x):
        yield x ** 3

values = mygenerator(100)
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

for x in values:
    print(x)

def infinite_sequance():
    result = 1
    while True:
        yield result
        result *= 5