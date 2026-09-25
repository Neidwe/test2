def mean(lst):
    return sum(lst) / len(lst)
def median(lst):
    s = sorted(lst)
    n = len(s)
    mid = n % 2
    if n % 2 == 0:
        return (s[mid-1] + s[mid]) / 2
    return s[mid]

