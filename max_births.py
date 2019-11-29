def general():
    lines = []
    try:
        with open('births.csv', 'r') as data:
            next(data)
            for line in data:
                line = line[:len(line) - 1].split(',')
                if int(line[0]) > 1985:
                    lines.append(line)
    except FileNotFoundError:
        print("File doesn't exist in the specified path or the name spelled incorrectly")
    return lines


def country_quantity_list():
    country_quantity = {}
    lines = general()
    for each in lines:
        country = str(each[1][1:-1])
        quantity = int(each[3])
        if country not in country_quantity.keys():
            country_quantity[country] = []
        country_quantity[country].append(quantity)
    return country_quantity


def count_children():
    country_quantity = country_quantity_list()
    altogether = {}
    for k, v in country_quantity.items():
        altogether[k] = sum(v)
    try:
        country_with_max_births = max(altogether, key=altogether.get)
        max_births = max(altogether.values())
        print("In the years of 1986-2006 the country with the highest birthrate was {}, counting {} births."
              .format(country_with_max_births, "{:,}".format(max_births)))
    except ValueError:
        exit(0)


if __name__ == "__main__":
    count_children()

"""for k,v in general_list.items():
        k = int(k)
        v[0]= int(v[0])
        v[1]=str(v[1][1:-1])
        v[2]=str(v[2][1:-1])
        v[3]=int(v[3])
        print(general_list)
        return general_list"""

"""def year_per_country():
    year_country_quantity = {}
    data = general()
    print(data)
    for v in data.values():
        sum = 0
        if v[1] not in year_country_quantity.keys():
            sum = v[3]
            year_country_quantity[v[1]]=[]
        year_country_quantity[v[1]].append([v[0],sum])

    print(year_country_quantity)
    return year_per_country()

year_per_country()"""
