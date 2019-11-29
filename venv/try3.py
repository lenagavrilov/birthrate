def general():
    global general_list
    general_list = {}
    with open('births.csv') as data:
        next(data)
        row = 1
        data.readline()
        for line in data:
            line = line[:len(line)-1]
            general_list[row] = line.split(',')
            row +=1
        print(data)
