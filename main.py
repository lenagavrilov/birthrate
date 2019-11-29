import max_births
import boys_or_girls


def choice():
    user_choice = ""
    try:
        user_choice = int(input("Press 1 to see the country with highest birth rate.\n"
                                "Press 2 to see if there were more girls or boys born.\n"))
    except ValueError:
        print("Enter numbers only!!!")
        exit(0)
    do_choice(user_choice)
    return user_choice


def do_choice(user_choice):
    if user_choice == 1:
        max_births.count_children()
    elif user_choice == 2:
        boys_or_girls.girls_and_boys()
    else:
        print("The choice is not valid. You should press 1 or 2 only.")


if __name__ == "__main__":
    choice()

"""def general():
    global general_list
    general_list = {}
    with open('births.csv') as data:
        next(data)
        row = 1
        for line in data:
            line = line[:len(line)-1]
            general_list[row] = line.split(',')
            row +=1
        for k,v in general_list.items():
            k = int(k)
            v[0]= int(v[0])
            v[1]=str(v[1][1:-1])
            v[2]=str(v[2][1:-1])
            v[3]=int(v[3])
        print(general_list)
        return general_list


def years_data_general():
    global years_data
    years_data = {}
    for k,v in general().items():
        year = v[0]
        if year not in years_data.keys():
            years_data[year]= []
        years_data[year].append([v[1],v[2],v[3]])
    #print (years_data)
    return years_data

def countries(data):
    countries = set()
    for v in data.values():
        for each in v:
            countries.add(each[0])
    print(sorted(countries))
    return sorted(countries)

#countries()

def years(data):
    years = []
    for k in data.keys():
        years.append(k)
    print (years)
    return years
#years()

def country_per_year():
    years_data = years_data_general()
    countries_data = countries(years_data)
    years_data = years(years_data)
    year_per_country = {}
    for v in years_data.values():
        for year in years_data:
            for country in countries_data:
                if year not in year_per_country.keys():
                    year_per_country[year] =[]
                year_per_country[year].append([country, v[2]])
    print(year_per_country)

country_per_year()"""

"""def year_per_country(countries):
    year_per_country = {}
    for k, v in years_data.items():
        for country in countries:
            sum = 0
            for each in v:
                if each[0] == country:
                    sum += int(each[2])
                    if k not in year_per_country.keys():
                       year_per_country[k] = []

                    year_per_country[k]= [country,sum]
                    #year_per_country[k].append([country,sum])


    #sum_births_per_country_all_years(year_per_country)
    print(year_per_country)
    return year_per_country


def sum_births_per_country_all_years(year_per_country):
    sum_all = 0
    for each in year_per_country.values():
        sum_all += each[1]
    print("In the state of {} between years 1981 and 2006 there were born {} children.".format(each[0], sum_all))

year_per_country(countries(years()))
#sum_births_per_country_all_years(year_per_country())"""
