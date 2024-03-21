def get_evil(n):
    evil_count = 0
    num = 0
    while True:
        binary = bin(num)[2:]
        ones_counter = binary.count('1')
        if ones_counter % 2 == 0:
            evil_count += 1
        if ones_counter == n:
            return num
        num += 1

get_evil(8)