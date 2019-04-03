# Orange DB 

A simple and  lightweight key-value based database.
Based on Python's json library.

# How it's used
```python
from OrangeDB import Orange

# initialize a new database
# Orange(database_name, auto_dump=True)
orange = Orange('mydata.orng')

# set a new value to a key
# orange.set(key, value)
orange.set('name', 'Shayan')

# get the value set for a key
# orange.get(key)
my_name = orange.get('name')

# delete the value set for the key
# orange.delete(key)
orange.delete('name')

# check whether a key exists
# orange.has(key)
# key in orange
orange.has('name')

# automatically dump the database
# orange.dump(force=True)
orange.dump()

# clear the entire database
# orange.clear()
orange.clear()
```
