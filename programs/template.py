import pprint
message = 'hello turtlepops.'
count = {}

for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1
    
print(pprint.pprint(count))