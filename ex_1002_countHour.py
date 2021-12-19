name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
lst = list()
lh = list()

for line in handle:
    if not line.startswith('From '):
        continue
    line = line.split()
    lst.append(line[5])
    

for hours in lst:
    hours = hours.split(":")
    lh.append(hours[0])

for hour in lh:
    counts[hour] = counts.get(hour,0) + 1
#print(counts)


for k, v in sorted([(k,v) for k,v in counts.items()]):
    print (k,v)
