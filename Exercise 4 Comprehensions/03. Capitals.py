countries = input().split(", ")
cities = input().split(", ")

mydict = {country: city for country, city in zip(countries, cities)}

for country, city in mydict.items():
    print(f"{country} -> {city}")