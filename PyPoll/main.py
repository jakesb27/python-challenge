import csv


# empty dictionary to store candidates information
vote_totals = {}

# open csv file and store in a list
with open('./Resources/election_data.csv', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)


for row in rows:

    # add candidate to dictionary if not listed and add one vote
    if row['Candidate'] not in [key for key, value in vote_totals.items()]:
        vote_totals[row['Candidate']] = 1
    else:
        # if candidate in dictionary, add 1 vote
        vote_totals[row['Candidate']] += 1

# create summary string for saving to txt file
summary = f"Election Results\n" \
          f"-------------------------\n" \
          f"Total Votes: {len(rows)}\n" \
          f"-------------------------\n"

for key, value in vote_totals.items():
    summary += f"{key}: {'{0:.3%}'.format(value/len(rows))} ({value})\n"

summary += f"-------------------------\n" \
           f"Winner: {max(vote_totals, key=vote_totals.get)}\n" \
           f"-------------------------"

# save text file with results
with open('./analysis/results.txt', 'w') as results:
    results.write(summary)

print(summary)
