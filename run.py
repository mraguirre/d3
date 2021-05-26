import csv

a3 = []

bool = True

while bool:

    fname = input('File name: ')
    with open(fname) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'{row[1]}')
                if row[1] != '':
                    a3.append(int(row[1]))
                line_count += 1
        print(f'Processed {line_count} lines.')

        user_input = input('Would you like to quit? (y/n) ')
        if user_input == 'y':
            bool = False

print(a3)
