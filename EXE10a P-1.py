import csv

with open("C:\\Users\\lab\\Desktop\\mahir.csv","a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Roll No", "CP2"])
    writer.writerow(["Mahir", "24BIT036","10"])
    
