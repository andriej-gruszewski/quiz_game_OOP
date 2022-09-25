def recursive(number):
    if number == 20:
        return True
    else:
        new_number = number + 1
        return recursive(new_number)

print(recursive(1))