import json
from datetime import datetime,date
list_of_dates,list_of_rates=[],[]
with open("data.json") as f:
    data=json.load(f)
print("Enter the currency symbol")
currency_symbol=input()
print("Enter the starting date in formate YY/MM/DD")
year,month,day=(map(int,input().split("-")))
starting_date=date(year,month,day)
print(starting_date)
print("Enter the ending date in formate YY/MM/DD")
year,month,day=(map(int,input().split("-")))
ending_date=date(year,month,day)
print(ending_date)
for i in data['rates']:
    current_year,current_month,current_day=map(int,i.split("-"))
    current_date=date(current_year,current_month,current_day)
    if current_date>starting_date and current_date<ending_date:
        list_of_dates.append(str(current_date))
list_of_dates=sorted(list_of_dates)
for i in list_of_dates:
    list_of_rates.append(data['rates'][i][currency_symbol])
print(str(list_of_dates))
print(str(list_of_rates))
maximum_rate,minimum_rate = max(list_of_rates),min(list_of_rates)
file = open('svg_file.svg','w')
file.write('''<svg width="1000" height="1000" xmlns="http://www.w3.org/2000/svg">\n''')
file.write('''<rect width="100%" height="100%" fill="white" />\n''')
file.write("<line x1=\"100"  "\" y1=\"440" "\" x2=\"" +str(120 + len(list_of_rates) * 15) + "\" y2=\" 440" + "\" stroke=\"" + str("mediumorchid") + "\" />\n")
file.write("<line x1=\"100"  "\" y1=\"440" "\" x2=\"100" + "\" y2=\"" +str(400 - 200 * (maximum_rate - minimum_rate) / (maximum_rate - minimum_rate))+ "\" stroke=\"" + str("mediumorchid") + "\" />\n")
x=[] 
y=[]
for i in range(len(list_of_rates)):
    cx = 120 + i * 15 
    cy = 400 - 200 * (list_of_rates[i] - minimum_rate)/(maximum_rate - minimum_rate)
    x.append(cx)
    y.append(cy)
    file.write('''<circle cx=''' + '''"'''+str(cx)+'''"''' + ''' cy=''' + '''"'''+str(cy) + '''"''' + ''' r="3"/> ''')
    file.write("<text x=\"" + str(cx-5) + "\" y=\"450\" fill=\"darkmagenta\" style=\"font: 12px sans-serif;\" transform=\"rotate(90," + str(cx-5) + ",450)\">" + list_of_dates[i] + "</text>\n")

a=(maximum_rate-minimum_rate)/5
new=minimum_rate
list_of_rates=sorted(list_of_rates)
for i in range(len(list_of_rates)):
    if list_of_rates[i]>=new:
        cy=400 - 200 * (list_of_rates[i] - minimum_rate)/(maximum_rate - minimum_rate)
        file.write('''<text x=\"40\" y="'''+str(cy+4)+'''" fill=\"darkmagenta\">'''+str(list_of_rates[i])+'''</text>\n''')
        new=list_of_rates[i]+a
file.write("<text x=\"100\" y=\"570\" fill=\"darkmagenta\" style=\"font:24px sans-serif\">""INR Exchange rates"+"</text>\n")
file.write("<text x=\"100\" y=\"600\" fill=\"darkgoldenrod\">"+"Start Date: "+str(starting_date)[:11]+"</text>\n")
file.write("<text x=\"300\" y=\"600\" fill=\"darkgoldenrod\">"+"End Date: "+str(ending_date)[:11]+"</text>\n")
file.write("<text x=\""+str(120 + len(list_of_rates) * 15)+"\" y=\"460\" fill=\"darkmagenta\" >"+"Dates "+"</text>\n")
file.write("<text x=\"40\" y=\"" +str(400 - 200 * (maximum_rate - minimum_rate) / (maximum_rate - minimum_rate)) + "\" fill=\"darkmagenta\" >"+"Rates "+"</text>\n")
file.write("</svg>\n")
file.close()
f.close()