total_sum = 0
try:
    with open('numbers.txt', 'r') as input_file:
        for line in input_file:
            try:
                number = int(line.strip())
                total_sum += number
            except ValueError:
                pass
except FileNotFoundError:
    exit()
print(total_sum)
try:
    with open('sum_numbers.txt', 'w') as output_file:
        output_file.write((str(total_sum)) + '\n')
except IOError:
    pass