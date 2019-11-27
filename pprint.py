import pprint
message = 'i want to quit my job'
count = {}

for charater in message:
    count.setdefault(character, 0)
    