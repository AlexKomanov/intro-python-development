counter = 0

while counter <= 10:
    if counter % 2 == 0:
        counter += 1
        continue
    if counter == 9:
        break
    print(f"Counter number is: {counter}")
    counter += 1

