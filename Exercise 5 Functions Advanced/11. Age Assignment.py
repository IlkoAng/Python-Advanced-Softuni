def age_assignment(*args, **kwargs):
    result = {name: 0 for name in args}

    for first_letter, age in kwargs.items():
        for name in result:
            if name.startswith(first_letter):
                result[name] = age
    return result


print(age_assignment("Peter", "George", G=26, P=19))