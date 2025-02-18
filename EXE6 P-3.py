from datetime import date

date1=(18,2,2025)
date2=(13,7,2023)

d1=date(date1[2],date1[1],date1[0])
d2=date(date2[2],date2[1],date2[0])
days=abs((d2-d1).days)

print(days)
