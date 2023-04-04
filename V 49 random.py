import random

for number in range(0, 10):
    print(random.randint(30, 50))

for number in range(0, 5):
    print(roun6d(random.uniform(1, 10)))

for number in range(0, 7):
    print(random.gauss(50, 25))

numbers = (1, 2, 3, 5, 10)
times = 2
print(random.sample(numbers, times))