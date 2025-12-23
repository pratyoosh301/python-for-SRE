with open('error_log.txt', 'r') as file:
    error_count = 0
    for line in file:
        if 'ERROR' in line:
            error_count += 1
print(f'Total number of errors: {error_count}')