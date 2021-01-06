import itertools

class Fibonacci:
    limit = 0
    first = 0
    second = 1
    next_term = 1

    def __init__(self, upper_limit):
        self.limit = upper_limit

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.next_term < self.limit:
            self.first = self.second
            self.second = self.next_term
            self.next_term = self.first + self.second
            return self.second
        else:
            raise StopIteration

fibonacci_iterator = iter(Fibonacci(4000000))

for i in itertools.islice(fibonacci_iterator, 10):
    print(i)

print(sum(filter(lambda x: x % 2 == 0, iter(Fibonacci(4000000)))))
