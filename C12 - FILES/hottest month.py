import csv
def max_city_temp(csv_filename, city):
    #read from csv
    fp = open(csv_filename)
    data = csv.reader(fp)
    header = next(data)    
    content = list(data)
    for i in range(0,len(content)):
        for j in range(1,len(content[i])):
            content[i][j] = float(content[i][j])
    for i in range (0, len(content)):
        if content[i][0] == city:
            maxtemp = max(content[i][1:])
            return maxtemp
    fp.close()
    