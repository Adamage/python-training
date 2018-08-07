with open('example.csv') as file:
    headers = file.readline().replace("\n","").split(",")
    data = []
    for line in file:
        data.append(line.replace("\n","").split(","))

    for record in data:
        record_dictionary = {k:v for k,v in zip(headers,record)}
        print(record_dictionary)
