import csv
def sort_records(csv_filename, new_filename):
    #read from csv
    fp = open(csv_filename)
    data = csv.reader(fp)
    header = next(data)
    header_list = [header]
    #extract and sort the data
    data2 = list(data)
    content = data2[:]
    sorted_content = sorted(content)
    sorted_content = header_list + sorted_content
    fp.close()
    #write to csv
    csv_file = open(new_filename,'w')
    writer = csv.writer(csv_file)
    writer.writerows(sorted_content)
    csv_file.close()
    