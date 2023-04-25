import csv

rowCount = 69

f = open("export.csv", "w")
writer = csv.writer(f)
writer.writerow(row)
f.close()
