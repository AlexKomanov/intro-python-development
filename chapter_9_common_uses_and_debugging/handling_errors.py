import sys

# my_file = open('recipes.txt', 'x')
# my_file.write('Meatballs\nPizza\n')
# my_file.close()

file_name = 'recipes.txt'

try:
    my_file = open(file_name)
    my_file.write('Meatballs\nPizza\n')
    my_file.close()
except FileExistsError as err:
    print(f"The {file_name} does already exist.")
    sys.exit(1)
except:
    print(f"Unable to write to the file '{file_name}'")
    sys.exit(1)
else:
    print(f"Wrote to {file_name}")
finally:
    print("Execution completed!")



