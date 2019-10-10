#  Задача Дан список стран и городов каждой страны.
#  Затем даны названия городов. Для каждого города укажите,
#  в какой стране он находится.
num_countries = int(input("Enter № country: "))
dict_countries = {}

for i in range(num_countries):
    (country, *city) = input("Enter the country, and located cities: ").split()

    for j in city:
        dict_countries[j] = country
print(dict_countries)

num_city = int(input("Enter number of cities: "))
list_city = []
print("Cities: ")
for i in range(num_city):
    list_city.append(input("Enter n city: "))
for i in list_city:
    print(dict_countries.get(i, "Not in database"))




