import os.path

filename = input("Enter shopping list name: ")
shopping_list = []

if os.path.isfile(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

        for line in lines:
            shopping_list.append(line.strip("\n"))
else:
    print("Creating new shopping list...")

    with open(filename, "w") as file:
        file.write("")


def print_list():
    for i in range(len(shopping_list)):
        print(f"{i + 1}. {shopping_list[i]}")
        print()


def save_list():
    with open(filename, "w") as file:
        for item in shopping_list:
            file.write(item + "\n")


while True:
    print("1. Print list")
    print("2. Add item to list")
    print("3. Remove item from list")
    print("4. Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        print_list()

    elif option == 2:
        shopping_list.append(input("Item: "))
        save_list()

    elif option == 3:
        print_list()

        num = int(input("Enter number to remove: "))
        shopping_list.pop(num - 1)

        save_list()
