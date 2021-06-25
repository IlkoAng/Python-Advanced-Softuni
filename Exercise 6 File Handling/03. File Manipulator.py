from os import remove
command = input()


def create_file(file_name):
    with open(file_name, "w"):
        pass


def add_content(file_name, content):
    try:
        with open(file_name, "a") as file:
            file.write(content + "\n")

    except FileNotFoundError:
        with open(file_name, "w") as file:
            file.write(content + "\n")


def replace_content(file_name, old, new):
    try:
        with open(file_name) as file:
            content = file.read()

        with open(file_name, "w") as file:
            content = content.replace(old, new)
            file.write(content)

    except FileNotFoundError:
        print(f"An error occurred")


def delete_file(file_name):
    try:
        remove(file_name)
    except FileNotFoundError:
        print(f"An error occurred")


while command != "End":
    func, *rest = command.split("-")

    if func == "Add":
        add_content(rest[0], rest[1])
    elif func == "Replace":
        replace_content(rest[0], rest[1], rest[2])
    elif func == "Create":
        create_file(rest[0])
    elif func == "Delete":
        delete_file(rest[0])

    command = input()
