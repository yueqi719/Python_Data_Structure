name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
counts = dict()
emails = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    line = line.split()
    emails.append(line[1])

for email in emails:
    counts[email] = counts.get(email,0) + 1

bigcount = None
bigemail = None
for email, count in counts.items():
    if bigcount is None or count > bigcount:
        bigemail = email
        bigcount = count

print(bigemail, bigcount)