def create_phone_book():
    command = input()
    book = {}
    while not command.isdigit():
        name, number = command.split("-")
        book[name] = number
        command = input()
    return book, int(command)


def searching(contact_name, phone_book):
    if phone_book.get(contact_name):
        print(f"{name} -> {phone_book[contact_name]}")
    else:
        print(f"Contact {name} does not exist.")


phone_book, iterations = create_phone_book()
for _ in range(int(iterations)):
        name = input()
        searching(name, phone_book)

