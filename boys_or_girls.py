

def general_list():
    lines = []
    with open('births.csv', 'r') as data:
        next(data)
        for line in data:
            line = line[:len(line)-1].split(',')
            lines.append(line)
    return lines


def girls_and_boys():
    lines = general_list()
    global country_boys
    global country_girls
    country_boys = {}
    country_girls = {}
    for each in lines:
        country = str(each[1][1:-1])
        quantity = int(each[3])
        gender = str(each[2][1:-1])
        if gender == 'boy':
            boys(country, quantity)
        else:
            girls(country, quantity)
    and_the_winner_is()


def boys(country, quantity):
    if country not in country_boys.keys():
        country_boys[country] = []
    country_boys[country].append(quantity)
    return country_boys


def girls(country,quantity):
    if country not in country_girls.keys():
        country_girls[country] = []
    country_girls[country].append(quantity)
    return country_girls


def altogether(gender_list):
    altogether_list = {}
    for k, v in gender_list.items():
        altogether_list[k] = sum(v)
    return altogether_list


def and_the_winner_is():
    boys = altogether(country_boys)
    girls = altogether(country_girls)
    for k, v in boys.items():
        for key,value in girls.items():
            if k == key:
                if v > value:
                    print("More {} were born in {} in the years 1981-2006.".format("boys", k))
                else:
                    print("More {} were born in {} in the years 1981-2006.".format("boys", k))


if __name__ == "__main__":
    girls_and_boys()
