import json
import requests
from datetime import timedelta, date
print("Enter the currency symbol1")
currency_symbol1=input()
print("Enter the currency symbol2")
currency_symbol2=input()
print("Enter the starting date in formate YY/MM/DD")
year,month,day=(map(int,input().split("-")))
starting_date=date(year,month,day)
print(starting_date)
print("Enter the ending date in formate YY/MM/DD")
year,month,day=(map(int,input().split("-")))
ending_date=date(year,month,day)
print(ending_date)
url='https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols=INR,GBP'.format(starting_date,ending_date)
url2='https://api.exchangeratesapi.io/latest?symbols=INR,GBP'
response = requests.get(url)
l = response.text
data = json.loads(l)

response2 = requests.get(url2)
f = response2.text
data2 = json.loads(f)
list_of_dates=[]
INR_rates=[]
GBP_rates=[]

for i in data['rates']:
    list_of_dates.append(i)
list_of_dates=sorted(list_of_dates)
for i in list_of_dates:
    INR_rates.append(data['rates'][i]['INR'])
    GBP_rates.append(data['rates'][i]['GBP'])
maximum_rate,minimum_rate = max(INR_rates),min(INR_rates)
file = open('t5.svg','w')
file.write('''<svg width="1000" height="1000" xmlns="http://www.w3.org/2000/svg">\n''')
file.write('''<rect width="100%" height="100%" fill="white" />\n''')
file.write("<line x1=\"100"  "\" y1=\"440" "\" x2=\"" +str(120 + len(INR_rates) * 15) + "\" y2=\" 440" + "\" stroke=\"" + str("mediumorchid") + "\" />\n")
file.write("<line x1=\"100"  "\" y1=\"440" "\" x2=\"100" + "\" y2=\"" +str(400 - 200 * (maximum_rate - minimum_rate) / (maximum_rate - minimum_rate))+ "\" stroke=\"" + str("mediumorchid") + "\" />\n")
x=[] 
y=[]
for i in range(len(INR_rates)):
    cx = 120 + i * 15 
    cy = 400 - 200 * (INR_rates[i] - minimum_rate)/(maximum_rate - minimum_rate)
    x.append(cx)
    y.append(cy)
    file.write('''<circle cx=''' + '''"'''+str(cx)+'''"''' + ''' cy=''' + '''"'''+str(cy) + '''"''' + ''' r="3"/> ''')
    file.write("<text x=\"" + str(cx-5) + "\" y=\"450\" fill=\"darkmagenta\" style=\"font: 12px sans-serif;\" transform=\"rotate(90," + str(cx-5) + ",450)\">" + list_of_dates[i] + "</text>\n")

a=(maximum_rate-minimum_rate)/5
new=minimum_rate
INR_rates=sorted(INR_rates)
for i in range(len(INR_rates)):
    if INR_rates[i]>=new:
        cy=400 - 200 * (INR_rates[i] - minimum_rate)/(maximum_rate - minimum_rate)
        file.write('''<text x=\"40\" y="'''+str(cy+4)+'''" fill=\"darkmagenta\">'''+str(INR_rates[i])+'''</text>\n''')
        new=INR_rates[i]+a
file.write("<text x=\"100\" y=\"570\" fill=\"darkmagenta\" style=\"font:24px sans-serif\">"+str(currency_symbol1)+"  Exchange rates"+"</text>\n")
file.write("<text x=\"100\" y=\"600\" fill=\"darkgoldenrod\">"+"Start Date: "+str(starting_date)[:11]+"</text>\n")
file.write("<text x=\"300\" y=\"600\" fill=\"darkgoldenrod\">"+"End Date: "+str(ending_date)[:11]+"</text>\n")
file.write("<text x=\""+str(120 + len(INR_rates) * 15)+"\" y=\"460\" fill=\"darkmagenta\" >"+"Dates "+"</text>\n")
file.write("<text x=\"40\" y=\"" +str(400 - 200 * (maximum_rate - minimum_rate) / (maximum_rate - minimum_rate)) + "\" fill=\"darkmagenta\" >"+"Rates "+"</text>\n")
file.write("<text x=\"100\" y=\"650\" fill=\"darkgoldenrod\">"+"Latest rate of "+str(currency_symbol1)+"  :  "+str(data2['rates'][currency_symbol1])+"</text>\n")
file.write("</svg>\n")
file.close()
maximum_rate2,minimum_rate2 = max(GBP_rates),min(GBP_rates)
file = open('t6.svg','w')
file.write('''<svg width="1000" height="1000" xmlns="http://www.w3.org/2000/svg">\n''')
file.write('''<rect width="100%" height="100%" fill="white" />\n''')
file.write("<line x1=\"100"  "\" y1=\"440" "\" x2=\"" +str(120 + len(GBP_rates) * 15) + "\" y2=\" 440" + "\" stroke=\"" + str("mediumorchid") + "\" />\n")
file.write("<line x1=\"100"  "\" y1=\"440" "\" x2=\"100" + "\" y2=\"" +str(400 - 200 * (maximum_rate2 - minimum_rate2) / (maximum_rate2 - minimum_rate2))+ "\" stroke=\"" + str("mediumorchid") + "\" />\n")
x2=[] 
y2=[]
for i in range(len(GBP_rates)):
    cx = 120 + i * 15 
    cy = 400 - 200 * (GBP_rates[i] - minimum_rate2)/(maximum_rate2 - minimum_rate2)
    x2.append(cx)
    y2.append(cy)
    file.write('''<circle cx=''' + '''"'''+str(cx)+'''"''' + ''' cy=''' + '''"'''+str(cy) + '''"''' + ''' r="3"/> ''')
    file.write("<text x=\"" + str(cx-5) + "\" y=\"450\" fill=\"darkmagenta\" style=\"font: 12px sans-serif;\" transform=\"rotate(90," + str(cx-5) + ",450)\">" + list_of_dates[i] + "</text>\n")

a=(maximum_rate2-minimum_rate2)/5
new=minimum_rate2
GBP_rates=sorted(GBP_rates)
for i in range(len(GBP_rates)):
    if GBP_rates[i]>=new:
        cy=400 - 200 * (GBP_rates[i] - minimum_rate2)/(maximum_rate2 - minimum_rate2)
        file.write('''<text x=\"40\" y="'''+str(cy+4)+'''" fill=\"darkmagenta\">'''+str(GBP_rates[i])+'''</text>\n''')
        new=GBP_rates[i]+a
file.write("<text x=\"100\" y=\"570\" fill=\"darkmagenta\" style=\"font:24px sans-serif\">"+str(currency_symbol2)+"  Exchange rates"+"</text>\n")
file.write("<text x=\"100\" y=\"600\" fill=\"darkgoldenrod\">"+"Start Date: "+str(starting_date)[:11]+"</text>\n")
file.write("<text x=\"300\" y=\"600\" fill=\"darkgoldenrod\">"+"End Date: "+str(ending_date)[:11]+"</text>\n")
file.write("<text x=\""+str(120 + len(GBP_rates) * 15)+"\" y=\"460\" fill=\"darkmagenta\" >"+"Dates "+"</text>\n")
file.write("<text x=\"40\" y=\"" +str(400 - 200 * (maximum_rate2 - minimum_rate2) / (maximum_rate2 - minimum_rate2)) + "\" fill=\"darkmagenta\" >"+"Rates "+"</text>\n")
file.write("<text x=\"100\" y=\"650\" fill=\"darkgoldenrod\">"+"Latest rate of "+str(currency_symbol2)+"  :  "+str(data2['rates'][currency_symbol2])+"</text>\n")
file.write("</svg>\n")
file.close()