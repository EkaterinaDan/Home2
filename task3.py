def transform(list_numbers):
    result = []
    for element in list_numbers:
        result.append(element)
        if element < 0:
            result.append(0)
    return result


print(transform([10, 11, 12, -11, 56, -100]))