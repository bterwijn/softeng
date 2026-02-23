
def quick_sort(values, key=None):
    if len(values) <= 1:
        return values
    pivot = values[0]  # choose arbitrarily the first as pivot
    smaller = [x for x in values if x  < pivot]
    equal   = [x for x in values if x == pivot]
    larger  = [x for x in values if x  > pivot]
    return quick_sort(smaller, key) + equal + quick_sort(larger, key)

if __name__ == "__main__":
    values = [7, 4, 10, 11, 2, 6, 9, 1, 5, 3,  8, 12]
    print('unsorted values:', values)
    result = quick_sort(values, key=lambda x: -x)
    print('  sorted values:', result)
