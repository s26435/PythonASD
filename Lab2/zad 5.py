def binary(num):
    if num == 0:
        return '0'

    binary_num = ''
    while num > 0:
        r = num % 2
        binary_num = str(r) + binary_num
        num //= 2
    
    return binary_num

print(binary(10))