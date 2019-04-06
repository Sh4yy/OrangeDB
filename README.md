![Frame](https://user-images.githubusercontent.com/23535123/55519457-e965b600-5645-11e9-857b-cf47dc99f160.png)

A simple and  lightweight key-value based database.
Based on Python's json library and inspired by PickleDB and Redis.

# How it's used
```python
from OrangeDB import Orange

# initialize a new database
db = Orange('database.orng')

# set a new value to a key
db.set('name', 'Shayan')
>>> True

# get the value set for a key
db.get('name', default='Unknown')
>>> 'Shayan'

# delete the value set for the key
db.delete('name')
>>> True

# check whether a key exists
db.has('name')
>>> False

# create a child database
users = db.child('app/users/')
users.set('sh4yy', {'name': 'Shayan'})
>>> True

# dump the database to the file
db.dump()
>>> True
```

## Todo
- Dictionary Methods

### Notes
Why Orange? It's the new theme for my projects, to be named after fruits!
