import random
def generate_numbers(n):
    return [random.randint(-100, 100) for i in range(n)]
