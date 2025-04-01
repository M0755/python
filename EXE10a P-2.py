import csv
f = open("C:\\Users\\lab\\Desktop\\mahir.csv","r")
reader = csv.DictReader(f)
for row in reader:
    print(row)
    
f.close()
