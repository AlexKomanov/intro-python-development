with open('automation.txt', 'w+') as my_file:
    my_file.write('Playwright\n')
    my_file.writelines([
        'Cypress\n',
        'WebDriver.IO\n'
        'Selenium\n',
        'TestCafe\n'
    ])

# my_file.close()

print('Reading a file...\n')
file_to_read = open('automation.txt', 'r')

with file_to_read:
    print(file_to_read.read())

    print('\nReading again...\n')
    print(file_to_read.read())

    print('\nReading again with seek...\n')
    file_to_read.seek(0)
    print(file_to_read.read())
# file_to_read.close()


