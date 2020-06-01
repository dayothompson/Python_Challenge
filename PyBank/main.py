import os
import csv

totalrows = 0
totalincome = 0
first_rev = 867884
change_list = []
month_list = []

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)

    for row in csv_reader:
        totalincome = totalincome + (int(row[1]))
        totalrows = totalrows + 1


        change = int(row[1]) - first_rev
        first_rev = int(row[1])
        month = row[0]
        change_list.append(change)
        month_list.append(month)
        totalchange = sum(change_list)

        max_inc = max(change_list)
        min_dec = min(change_list)

        max_month = month_list[change_list.index(max_inc)]
        min_month = month_list[change_list.index(min_dec)]


    count = (len(change_list) - 1)
    average_change = totalchange / count



    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(totalrows))
    print("Total: $" + str(totalincome))
    print("Average Change: $" + str(round(average_change, 2)))
    print("Greatest Increase in Profits: " + str(max_month) + " ($" + (str(max_inc)) + ")")
    print("Greatest Decrease in Profits: " + str(min_month) + " ($" + (str(min_dec)) + ")")


outputpath = os.path.join('Report_Analysis.txt')


# export the results as a text file
with open(outputpath, "w") as txtfile:
    txtfile.write('Financial Analysis')
    txtfile.write('\n------------------------------------')
    txtfile.write(f'\nTotal Votes: {totalrows}')
    txtfile.write(f'\nTotal: ${totalincome}')
    txtfile.write(f'\nAverage Change: ${round(average_change, 2)}')
    txtfile.write(f'\nGreatest Increase in Profits: {max_month} (${max_inc})')
    txtfile.write(f'\nGreatest Decrease in Profits: {min_month} (${min_dec})')




















