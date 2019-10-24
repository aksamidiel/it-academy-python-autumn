with open("ratings.list", encoding="ISO-8859-1") as film_rating_list:
    film = []
    first_pos = int(input("Enter first pars position: "))
    last_pos = int(input("Enter last position: "))
    line_list = [elem for elem in range(first_pos, last_pos)]
    i = 0
    for line in film_rating_list:
        if i in line_list:
            film.append(line.strip())
            i += 1
        else:
            i += 1

    film_list = [elem.split(" ") for elem in film]
    film_year = [elem[-1].strip('()/I') for elem in film_list]   # year
    film_year = list(map(int, film_year))
    print(film_year)

    film_list = [elem.split("  ") for elem in film]
    film_description = [elem[-1] for elem in film_list]   # description(name+year)
    print(film_description)

    film_name = [elem[-1].strip('(1234567890)/I ') for elem in film_list]  # description
    print(film_name)

    film_rang = [elem[-2].strip() for elem in film_list]
    film_rang = list(map(float, film_rang))   # rang
    print(film_rang)

    film_votes = [elem[-3].strip() for elem in film_list]   # votes
    film_votes = list(map(int, film_votes))
    print(film_votes)

with open('top250.txt', 'w', encoding='UTF-8') as top_films:
    data = '\n'.join(film_description)
    top_films.write(data)

with open('rating.txt', 'w', encoding='UTF-8') as rate_films:
    for elem in film_rang:
        rate = ''
        rating = elem
        while rating > 7:
            rate += '#'
            rating -= 0.1
        rate_films.write(rate + '\n')

with open('years.txt', 'w', encoding='UTF-8') as years_films:
    for elem in film_year:
        year = ''
        t_year = elem
        while t_year > 1900:
            year += '*'
            t_year -= 1
        years_films.write(year + '\n')









