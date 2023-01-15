import csv


# script default variables
prev_month = 0
pl_change = 0
max_inc = 0
max_inc_date = ""
max_dec = 0
max_dec_date = ""
change_list = []

# open csv file and store in a list
with open('./Resources/budget_data.csv', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)

# iterate over list to get profit/loss data
for row in rows:

    # skip the first record
    if prev_month == 0:
        prev_month = int(row['Profit/Losses'])
    else:
        # calculate profit/loss change and append to list
        pl_change = int(row['Profit/Losses']) - prev_month
        change_list.append(pl_change)
        prev_month = int(row['Profit/Losses'])

        # check if profit/loss change is greater or less than current max
        if pl_change > max_inc:
            max_inc = pl_change
            max_inc_date = row['Date']
        if pl_change < max_dec:
            max_dec = pl_change
            max_dec_date = row['Date']


# calculate and format summary totals
months = len(rows)
profit_loss = "${:,}".format(sum(int(row['Profit/Losses']) for row in rows))
avg_change = "${:,}".format(round(sum(change_list)/len(change_list), 2))
increase_amt = "${:,}".format(max_inc)
decrease_amt = "${:,}".format(max_dec)

# create summary string for saving to txt file
summary = f"Financial Analysis\n" \
          f"----------------------------\n" \
          f"Total Months: {months}\n" \
          f"Total: {profit_loss}\n" \
          f"Average Change: {avg_change}\n" \
          f"Greatest Increase in Profits: {max_inc_date} ({increase_amt})\n" \
          f"Greatest Decrease in Profits: {max_dec_date} ({decrease_amt})"

# save text file with results
with open('./analysis/results.txt', 'w') as results:
    results.write(summary)

print(summary)
