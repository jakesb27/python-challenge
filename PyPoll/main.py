import csv


vote_totals = {}

# open csv file and store in a list
with open('./Resources/election_data.csv', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)

for row in rows:
    if row['Candidate'] not in [key for key, value in vote_totals.items()]:
        vote_totals[row['Candidate']] = 1
    else:
        vote_totals[row['Candidate']] += 1

votes = len(rows)

for key, value in vote_totals.items():
    print(f"{key}: {value/votes} {value}")

print(max(vote_totals, key=vote_totals.get))
