import os

#At the moment of reviewing dataset(csv) I notice there's some lines without ISO CODE (code). Those without code were actually continents/regions except for Saint Barthlemy, so I modified those lines to have iso code BLM

#### CLASS to create Custom Object -> LifeExpectancy to save information easier ####
class LifeExpectancy:
    def __init__(self, entity, code, year, years_exp):
        self.entity = entity
        self.code = code
        self.year = year
        self.years_exp = years_exp
    
    def __str__(self):
        return f"Life expectancy from {self.entity}{'('+self.code+')' if len(self.code) > 1 else ''} at {self.year} was {self.years_exp}" #It is redefined the equivalent to toString method from java so there's a specific template to print the objects
        #it is review within the text returned if code has more than char of length. Cause all the ones that have code will count at least with 3 chars

    def getEntity(self):
        return self.entity
    
    def getCode(self):
        return self.code
    
    def getYear(self):
        return self.year
    
    def getYearExp(self):
        return self.years_exp
#### CLASS to create Custom Object -> LifeExpectancy to save information easier ####

#### CUSTOM FUNCTIONS ####
def min_expectancy(inputList):
    return min(inputList,key=lambda lifeexpectancy: lifeexpectancy.years_exp)
    #It is define/specified what MIN function needs to refer about to do the comparison

def max_expectancy(inputList):
    return max(inputList,key=lambda lifeexpectancy: lifeexpectancy.years_exp)
    #It is define/specified what MAX function needs to refer about to do the comparison

def average_from_list(inputList):
    return sum(dataLine.years_exp for dataLine in inputList) / len(inputList)
    #Average is equal to SUM of all elements (on this case we're interested on attribute years_exp) divided by quantity of elements, therefore list size

def filter_by_year(inputList, inputYear):
    return list(filter(lambda oneLineInfo: oneLineInfo.year == inputYear, inputList))
    #If there's no cast will return an object type FILTER which won't work for looking max, min, etc

def filter_by_countries_only(inputList):
    return list(filter(lambda oneLineInfo: oneLineInfo.code != "", inputList))

def filter_by_continents_only(inputList):
    return list(filter(lambda oneLineInfo: oneLineInfo.code == "", inputList))

def filter_by_one_country(inputList, inputCountry):
    return list(filter(lambda oneLineInfo: oneLineInfo.entity.lower() == inputCountry.lower(), inputList))
#### CUSTOM FUNCTIONS ####

### GLOBAL VARIABLES ###
list_life_expectancy = []
input_option = 0
iterator_qty = 0
### GLOBAL VARIABLES ###

### LOAD FILE BEFORE ASKING INPUT - DONE JUST ONCE ###
dir_path = os.path.dirname(os.path.realpath(__file__)) #retrieve root folder for py file
file_name = "life-expectancy.csv"
final_path = ""

#REVIEW THE DIR PATH TO DECIDE WHAT CHAIN CHARS or CHAR TO PLACE so can be executed on different operative systems
if dir_path.find("/") != -1:
    final_path = dir_path + "/" + file_name
elif dir_path.find("//") != -1:
    final_path = dir_path + "//" + file_name
elif dir_path.find("\\") != -1:
    final_path = dir_path + "\\" + file_name

with open(final_path) as data_file:
    for line in data_file:
        line = line.strip().split(",")
        if iterator_qty != 0:
            line_expectancy = LifeExpectancy(line[0],line[1],int(line[2]),float(line[3]))
            list_life_expectancy.append(line_expectancy)
        iterator_qty += 1 #It is ensured it is avoided the first line that are the headers cause'otherwise numbers won't be able to be casted to number for later comparison into the class
### LOAD FILE BEFORE ASKING INPUT - DONE JUST ONCE ###

### DEFINE THE LIST CONTAINING ONLY COUNTRIES AND CONTINENTS APART ###
list_life_expectancy_continents = filter_by_continents_only(list_life_expectancy)
list_life_expectancy_countries = filter_by_countries_only(list_life_expectancy)
### DEFINE THE LIST CONTAINING ONLY COUNTRIES AND CONTINENTS APART ###

while(input_option!=7):
    print("Please select one of the following:")
    print("1. What is the year and country that has the lowest life expectancy in the dataset?")
    print("2. What is the year and country that has the highest life expectancy in the dataset?")
    print("3. Get an expectancy life average from a specific year for countries only")
    print("4. List all dataset (countries and continents")
    print("5. Get an expectancy life average from a specific country")
    print("6. Get an expectancy life average from a specific continent")
    print("7. Quit")
    input_option = int(input("Please enter an action: "))
    if input_option == 1: #lowest
        lowest_life_expect_line = min_expectancy(list_life_expectancy_countries)
        print(f"The overall min life expectancy is: {lowest_life_expect_line.getYearExp()} from {lowest_life_expect_line.getEntity()} in {lowest_life_expect_line.getYear()}")
    elif input_option == 2: #highest
        highest_life_expect_line = max_expectancy(list_life_expectancy_countries)
        print(f"The overall max life expectancy is: {highest_life_expect_line.getYearExp()} from {highest_life_expect_line.getEntity()} in {highest_life_expect_line.getYear()}")
    elif input_option == 3: #Filter by year and provide data
        year_of_interest = int(input("Please enter year of interest: "))
        filtered = filter_by_year(list_life_expectancy_countries, year_of_interest)
        min_filter = min_expectancy(filtered) #Returns a LifeExpectancy object
        max_filter = max_expectancy(filtered) #Returns a LifeExpectancy object
        avg_filter = average_from_list(filtered) #Returns an actual number cause it was not needed to have more information
        print(f"\nFor the year {year_of_interest}:")
        print(f"The average life expectancy across all countries was {avg_filter:.3f}")
        print(f"The max life expectancy was in {min_filter.getEntity()} with {min_filter.getYearExp()}")
        print(f"The min life expectancy was in {max_filter.getEntity()} with {max_filter.getYearExp()}")
    elif input_option == 4: #list all
        for country_line in list_life_expectancy: #here is utilized the list without filter
            print(country_line)
    elif input_option == 5: #Filter by country and provide data
        country_of_interest = input("Please enter a country of interest: ")
        lines_of_country_interest = filter_by_one_country(list_life_expectancy_countries, country_of_interest)
        if len(lines_of_country_interest) == 0:
            print("You have selected a country which is not present in dataset, you'll be redirected to menu")
            input_option = 7 #force the option to be out of scope to print the menu again
        else:
            min_filter = min_expectancy(lines_of_country_interest) #Returns a LifeExpectancy object
            max_filter = max_expectancy(lines_of_country_interest) #Returns a LifeExpectancy object
            avg_filter = average_from_list(lines_of_country_interest) #Returns an actual number cause it was not needed to have more information
            print(f"\nFor the country {country_of_interest}:")
            print(f"The average life expectancy across the country was {avg_filter:.3f}")
            print(f"The max life expectancy was in {min_filter.getEntity()} with {min_filter.getYearExp()}")
            print(f"The min life expectancy was in {max_filter.getEntity()} with {max_filter.getYearExp()}")
    elif input_option == 6: #Filter by country and provide data
        continent_of_interest = input("Please enter a continent of interest: ")
        lines_of_continent_interest = filter_by_one_country(list_life_expectancy_continents, continent_of_interest)
        if len(lines_of_continent_interest) == 0:
            print("You have selected a country which is not present in dataset, you'll be redirected to menu")
            input_option = 7 #force the option to be out of scope to print the menu again
        else:
            min_filter = min_expectancy(lines_of_continent_interest) #Returns a LifeExpectancy object
            max_filter = max_expectancy(lines_of_continent_interest) #Returns a LifeExpectancy object
            avg_filter = average_from_list(lines_of_continent_interest) #Returns an actual number cause it was not needed to have more information
            print(f"\nFor the continent {continent_of_interest}:")
            print(f"The average life expectancy across all the continent was {avg_filter:.3f}")
            print(f"The max life expectancy was in {min_filter.getEntity()} with {min_filter.getYearExp()}")
            print(f"The min life expectancy was in {max_filter.getEntity()} with {max_filter.getYearExp()}")
    elif input_option != 7:
        print("\nPlease select one of the following:")
        print("1. What is the year and country that has the lowest life expectancy in the dataset?")
        print("2. What is the year and country that has the highest life expectancy in the dataset?")
        print("3. Get an expectancy life average from a specific year")
        print("4. List all dataset")
        print("5. Get an expectancy life average from a specific country")
        print("6. Get an expectancy life average from a specific continent")
        print("7. Quit")
        input_option = int(input("Please enter a valid action: "))
    print() #line between menu prints