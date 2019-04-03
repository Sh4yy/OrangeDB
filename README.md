![Frame](https://user-images.githubusercontent.com/23535123/55519457-e965b600-5645-11e9-857b-cf47dc99f160.png)

A simple and  lightweight key-value based database.
Based on Python's json library and inspired by PickleDB and Redis.

# How it's used
```python
from OrangeDB import Orange

# initialize a new database
db = Orange('mydata.db', auto_dump=True)

# set a new value to a key
db.set('name', 'Shayan')

# get the value set for a key
db.get('name', default='Unknown')

# delete the value set for the key
db.delete('name')

# check whether a key exists
db.has('name')

# dump the database to the file
db.dump()
```
