


def distinct_terms(a, b):
    uniques = set()
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            num = i ** j
            uniques.add(num)
    return len(uniques)

print(distinct_terms(5, 5))
print(distinct_terms(100, 100))