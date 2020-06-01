import os
import csv

totalvotes = 0
totalrows = 0
cand_list = []
cand_votes = []
percent = []
i = 0

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)

    for row in csv_reader:

        totalvotes = totalvotes + 1

        if row[2] in cand_list:
            i = cand_list.index(row[2])
            cand_votes[i] = cand_votes[i] + 1
        else:
            cand_list.append(row[2])
            cand_votes.append(1)

    for j in cand_votes:
        k = cand_votes.index(j)
        x = round(cand_votes[k] / totalvotes * 100, 4)
        percent.append(x)


    for y in cand_votes:
        max_votes = max(cand_votes)
        winner = cand_list[cand_votes.index(max_votes)]




print("Election Results ")
print("------------------------")
print("Total Votes: " + str(totalvotes))
print("----------------------------------")
print(str(cand_list[0]) + ": " + str(percent[0]) + "00% " + " (" + str(cand_votes[0]) + ")")
print(str(cand_list[1]) + ": " + str(percent[1]) + "00% " + " (" + str(cand_votes[1]) + ")")
print(str(cand_list[2]) + ": " + str(percent[2]) + "00% " + " (" + str(cand_votes[2]) + ")")
print(str(cand_list[3]) + ": " + str(percent[3]) + "00% " + " (" + str(cand_votes[3]) + ")")
print("----------------------------------")
print("Winner: " + str(winner))
print("----------------------------------")

outputpath = os.path.join("ElectionDataResults.txt")

# export the results as a text file
with open(outputpath, "w") as txtfile:
    txtfile.write('Election Results')
    txtfile.write('\n------------------------------------')
    txtfile.write(f'\nTotal Votes: {totalvotes}')
    txtfile.write('\n------------------------------------')
    for c in range(len(cand_list)):
        txtfile.write(f'\n{cand_list[c]}: {percent[c]}00%  ({cand_votes[c]})')
    txtfile.write('\n------------------------------------')
    txtfile.write(f'\nWinner: {winner}')
    txtfile.write('\n------------------------------------')

