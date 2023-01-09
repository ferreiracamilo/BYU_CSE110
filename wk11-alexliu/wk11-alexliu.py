max_expectancy = 0
min_expectancy = 3000
max_country = ""
min_country = ""
max_year = ""
min_year = ""
interest_year_count = 0
interest_total_expectancy = 0
oldest_year = 3000
newest_year = 0
display_year_or_country = ""
country_code = ""
keep_using = "yes"
print("Welcome to the expectancy searching system!")
while keep_using == "yes":
    #D:\Programacion\Proyectos\Programacion PC101 Python\wk11-alexliu\life-expectancy.csv
    with open("D:\Programacion\Proyectos\Programacion PC101 Python\wk11-alexliu\life-expectancy.csv") as unsort_data:
        next(unsort_data)
        interest_year_country = input("Please enter the year or name of the country of interest: ").capitalize()
        for line in unsort_data:
            sort_data = line.strip().split(",")
            countries = sort_data[0]
            code = sort_data[1]
            year = sort_data[2]
            life_expectancy = float(sort_data[3])
            for i, country in enumerate(countries):
                if interest_year_country == year:
                    interest_year_count += 1
                    display_year_or_country = "year"
                    interest_total_expectancy += life_expectancy
                    if life_expectancy > max_expectancy:
                        max_expectancy = life_expectancy
                        max_country = countries
                    elif life_expectancy < min_expectancy:
                        min_expectancy = life_expectancy
                        min_country = countries
                if interest_year_country.lower() == countries.lower():
                    interest_year_count += 1
                    interest_total_expectancy += life_expectancy
                    display_year_or_country = "country"
                    country_code = code
                    for time in year:
                        if int(year) > int(newest_year):
                            newest_year = year
                        elif int(year) < int(oldest_year):
                            oldest_year = year
                    if life_expectancy > max_expectancy:
                        max_expectancy = life_expectancy
                        max_year = year
                    elif life_expectancy < min_expectancy:
                        min_expectancy = life_expectancy
                        min_year = year
                
    if interest_year_count == 0:
        print(f"{interest_year_country} is not in the dataset to show year statistics.")
    elif display_year_or_country == "year":
        interest_year_average_expectancy = interest_total_expectancy / interest_year_count
        print(f"For the year {interest_year_country}:")
        print(f"The average life expectancy across all countries was {round(interest_year_average_expectancy,2)}")
        print(f"The max life expectancy was in {max_country} with {max_expectancy}")
        print(f"The min life expectancy was in {min_country} with {min_expectancy}")
    elif display_year_or_country == "country":
        interest_year_average_expectancy = interest_total_expectancy / interest_year_count
        print(f"For {interest_year_country}({country_code}):")
        print(f"The average life exoectancy recorded from {oldest_year} to {newest_year} was {round(interest_year_average_expectancy,2)}")
        print(f"The max life expectancy of {interest_year_country} is {max_expectancy} in {max_year}")
        print(f"The min life expectancy of {interest_year_country} is {min_expectancy} in {min_year}")
        # print(max_expectancy, min_expectancy, interest_year_country, max_country, min_country, round(interest_year_average_expectancy,2))
        # print(max_year, min_year, newest_year, oldest_year)
    reuse = input("Do you want to search again(Yes/No)? ").lower()
    while reuse != "yes" and reuse != "no":
        reuse = input("I beg your pardon(Yes/No)? ").lower()
    if reuse == "no":
        keep_using = False
        print("Thank you for using the searching system. Bye.")