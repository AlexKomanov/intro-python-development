def hello_world():
    print("Hello, World!")


def print_name(name):
    print(f"Hello, {name}")


def sum_2_numbers(num1, num2):
    return num1 + num2


def contact_card(name, age, car_model, driving_experience=10):
    print(f"The name is {name}, and the age is {age}, and a car model is {car_model}, and driving experience is {driving_experience}")


print(hello_world)
hello_world()

print_name("Alex")

result = sum_2_numbers(5, 10)
print(result)

contact_card("Alex", 35, "Seat Leon")
contact_card("Alex", car_model="Seat Leon", age=35, driving_experience=15)

פככדגכגדכ


