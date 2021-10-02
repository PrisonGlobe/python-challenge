import csv
import math


myMonth = []
myProfit = []
myMonthProfit = []
totalnum =-1


with open("resources/budget_data.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        totalnum+=1
        if totalnum == 0:
            pass
        else:
            myList = row[0].split(",")
            myMonth.append(myList[0])
            myProfit.append(int(myList[1]))
            
for i in range(len(myMonth)-1):
    myMonthProfit.append(myProfit[i+1]-myProfit[i])
    
maxProfit = max(myMonthProfit)
minProfit = min(myMonthProfit)

file = open("analysis/myfile.txt", "w")

file.write("Financial Analysis")
file.write("\n")
file.write("----------------------------")
file.write("\n")
file.write(f"Total Months: {len(myMonth)}")
file.write("\n")
file.write(f"Total: ${sum(myProfit)}")
file.write("\n")
file.write(f"Average  Change: ${round(sum(myMonthProfit)/len(myMonthProfit),2)}")
file.write("\n")
file.write(f"Greatest Increase in Profits: {myMonth[myMonthProfit.index(max(myMonthProfit)) + 1]} (${(str(maxProfit))})")
file.write("\n")
file.write(f"Greatest Decrease in Profits: {myMonth[myMonthProfit.index(max(myMonthProfit)) + 1]} (${(str(minProfit))})")

file.close()

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(myMonth)}")
print(f"Total: ${sum(myProfit)}")
print(f"Average  Change: ${round(sum(myMonthProfit)/len(myMonthProfit),2)}")
print(f"Greatest Increase in Profits: {myMonth[myMonthProfit.index(max(myMonthProfit)) + 1]} (${(str(maxProfit))})")
print(f"Greatest Decrease in Profits: {myMonth[myMonthProfit.index(max(myMonthProfit)) + 1]} (${(str(minProfit))})")

