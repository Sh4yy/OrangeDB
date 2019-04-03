from OrangeDB import Orange

db = Orange('mydata.orng')

db.set('name', 'shayan')
print(db.get('name'))

db.delete('name')
print(db.get('name'))
