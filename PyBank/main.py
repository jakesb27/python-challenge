import csv


# script default variables
prev_month = 0
pl_change = 0
max_inc = 0
max_dec = 0
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
        pl_change = int(row['Profit/Losses']) - prev_month
        change_list.append(pl_change)
        prev_month = int(row['Profit/Losses'])


# calculate and format summary totals
months = len(rows)
profit_loss = "${:,.2f}".format(sum(int(row['Profit/Losses']) for row in rows))
avg_change = "${:,.2f}".format(round(sum(change_list)/len(change_list), 2))
increase_date = 'UNK-UN'
increase_amt = "${:,.2f}".format(0)
decrease_date = 'UNK-UN'
decrease_amt = "${:,.2f}".format(0)

summary = f"Financial Analysis\n" \
          f"----------------------------\n" \
          f"Total Months: {months}\n" \
          f"Total: {profit_loss}\n" \
          f"Average Change: {avg_change}\n" \
          f"Greatest Increase in Profits: {increase_date} ({increase_amt})\n" \
          f"Greatest Decrease in Profits: {decrease_date} ({decrease_amt})"

with open('./analysis/results.txt', 'w') as results:
    results.write(summary)

print(summary)
