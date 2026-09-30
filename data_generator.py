import random
def generate_numbers(n):
    return [random.randint(-100, 100) for _ in range(n)]
def dice(sides, count=1):
    rolls = [random.randint(1, sides) for _ in range(count)]
    return rolls[0] if count == 1 else rolls