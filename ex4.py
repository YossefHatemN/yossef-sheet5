def apply(lst, fn):
    result = []
    for elem in lst:
        result.append(fn(elem))
    return result

# Using a lambda function
r = apply([1, 2, 3], lambda num: num + 1)
print(r)
