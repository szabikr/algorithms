def get_unique_digits(num):
    result = []
    while num > 0:
        digit = num % 10
        if digit not in result:
            result.append(digit)
        num //= 10
    return result