Fooditemswithprice=[
    ('maggi', 10),
    ('pasta',20),
    ('biscuits',5),
   ]
import operator
Fooditemswithprice.sort(key=operator.itemgetter(1), reverse=True)
for item in Fooditemswithprice:
       print(item)
