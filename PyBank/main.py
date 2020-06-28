#the module we'll use!
import csv

# opening & reading the csv file
with open ('Resources/budget_data.csv') as file:
    reader = csv.DictReader(file)
#set any variables I'll need to reference (this list is expanding as needed :p)
    count = 0
    netTotal = 0
    diffSum = 0
    prevProfit = 0
    greatestIncrease = 0
    greatestDecrease = 0
#The total number of months included in the dataset
    for row in reader:
        profit = int(row['Profit/Losses'])
        if count != 0:
            diff = profit - prevProfit
#The greatest increase in profits (date and amount) over the entire period
            if diff > greatestIncrease:
                greatestIncrease = diff
#The greatest decrease in losses (date and amount) over the entire period
            if diff < greatestDecrease:
                greatestDecrease = diff
#If either is correct, the value resets, otherwise, it increment by diff amout to get the avg.
            diffSum += diff
#Go to the next row
        count += 1
#The net total amount of "Profit/Losses" over the entire period
        netTotal += profit
#Save this value to use it ti calculate diff        
        prevProfit = profit

#The average of the changes in "Profit/Losses" over the entire period
    avgChange = diffSum/(count-1)
#Output all of this!        
    print("the financial analysis of PyBank:")
    print(count," months.") 
    print(netTotal, "$ is the net total")
    print(avgChange, "$ is the averga chanage")
    print(greatestIncrease, "$ is the greatest increase")
    print(greatestDecrease, "$ is the greatest decrease")

#Now, the damn text file
with open("MyPyBankOutput.txt", "a") as f:
    print("the financial analysis of PyBank:", file=f)
    print(count," months.", file=f) 
    print(netTotal, "$ is the net total", file=f)
    print(avgChange, "$ is the averga chanage", file=f)
    print(greatestIncrease, "$ is the greatest increase", file=f)
    print(greatestDecrease, "$ is the greatest decrease", file=f)


#In addition, your final script should both print the analysis to the terminal 
# and export a text file with the results.