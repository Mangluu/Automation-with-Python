import csv

l = [["local","192.168.25.46"],["cloud","10.2.5.6"]]

with open("hosts.csv","w") as hf:
    writer = csv.writer(hf)
    writer.writerows(l)
