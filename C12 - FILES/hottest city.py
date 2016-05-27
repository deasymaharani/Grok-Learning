import csv
def hottest_city(csv_filename):
    fp = open(csv_filename)
    data = csv.reader(fp)
    header = next(data)
    content = list(data)
    for i in range(0, len(content)):
        for j in range(1, len(content[i])):
            content[i][j] = float(content[i][j])
    maxcity = []
    for i in range(0, len(content)):
        maxcity.append(max(content[i][1:]))
    maxaus= max(maxcity)
    cities=[]
    for i in range(0, len(content)):
        for j in range(1, len(content[i])):
            if maxaus == content[i][j]:
                cities.append(content[i][0])
    cities = sorted(cities)
    pair = (maxaus, cities)
    return pair