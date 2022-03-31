def is_power_of_four(number: int) -> bool:
    n = 0
    while True:
        if 4**n == number:
            return True
        
        if 4**n >= 10000 or 4**n > number:
            return False

        n += 1


print(is_power_of_four(int(input())))
