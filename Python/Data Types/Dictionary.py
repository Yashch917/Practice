D={'company':'Maruti','Model':'Swift','Year':2023,'Place':'Pune'}
print(D)
print(type(D))

print(D['Place'])

print(D.get('company'))

D['Year']=2025
print(D)

print(D.update({'Place':'Nagpur'}))
print(D)

D.pop('Place')
print(D)

print(D.keys())

print(D.values())

print(D.items())