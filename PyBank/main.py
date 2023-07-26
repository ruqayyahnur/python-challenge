import os
import csv

CSV_PATH = os.path.join("Resources", "budget_data.csv")


total_months = 0
prev_revenue = 0
net_total_revenue = 0
months = []
revenue_changes_list = []
greatest_increase = ["",0]
greatest_decrease = ["", 0]
rev_avg = 0

 

#read the csv file
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    #print(header)

    for row in csv_reader:
        #print(row)
        #calculate totals
        total_months = total_months + 1
        net_total_revenue = net_total_revenue + int(row[1])

        #calculate revenue change
        revenue_changes = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])
        revenue_changes_list = revenue_changes_list + [revenue_changes] 
        months = months + [row[0]]

        #determine greatest increase in profits
        if(revenue_changes > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_changes
        if(revenue_changes < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_changes

#calculat the average outside the loop
rev_avg = sum(revenue_changes_list) / len(revenue_changes_list)

# print(rev_avg)
# print(greatest_increase)
# print(net_total_revenue)
# print(revenue_changes)
# print(revenue_changes_list)
# print(months)



print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_total_revenue}")
print(f"Average Change:  ${rev_avg}")
print(f"Greatest Increase in Profits:  {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Losses:  {greatest_decrease[0]} (${greatest_decrease[1]})")

budget_file = os.path.join("budget_data.txt")

with open(budget_file, 'w') as text:

    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write(f"Total Months:  {total_months}\n")
    text.write(f"Total:  ${net_total_revenue}\n")
    text.write(f"Average Change:  ${rev_avg}\n")
    text.write(f"Greatest Increase in Profits:  {greatest_increase[0]} (${greatest_increase[1]})")
    text.write(f"Greatest Decrease in Losses:  {greatest_decrease[0]} (${greatest_decrease[1]})")