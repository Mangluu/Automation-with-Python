import csv
f = open("hosts.csv")
csv_f = csv.reader(f)
for row in csv_f:
    host, address = row
    print("Host: {}, Address: {}".format(host, address))
f.close()
