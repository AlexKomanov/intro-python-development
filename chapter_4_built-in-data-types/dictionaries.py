ages = {'kevin': 59, 'alex': 29, 'bob': 40}

print(ages)
print(ages['kevin'])

ages['kayla'] = 21
print(ages)

del ages['kevin']
print(ages)

print(ages.pop('alex'))
print(ages)

print(ages.get('bob'))

print(list(ages.keys()))
print(list(ages.values()))

weights = dict(alex=160, bob=240, kayla=135)
print(weights)

colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
print(colors)



