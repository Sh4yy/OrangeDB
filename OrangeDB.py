import json
import os
from threading import Thread


class Orange:

    def __init__(self, file_path, auto_dump=True):
        """
        initialize a new Orange database
        :param file_path: path to the db file
        :param auto_dump: automatically store db on updates
        """
        self._file_path = os.path.expanduser(file_path)
        self._auto_dump = auto_dump
        self._db = None
        self._load()

    def _load(self):
        """
        load the database from local storage
        :returns: True on success
        """
        if os.path.exists(self._file_path):
            try:
                self._db = json.load(open(self._file_path, "r"))
            except ValueError:
                # in case the file is empty
                self._db = dict()
        else:
            self._db = dict()
        return True

    def dump(self, force=True):
        """
        dumps the current database into the file
        :param force: if set to true would ignore _auto_dump value
        """
        if force or self._auto_dump:
            thread = Thread(target=json.dump,
                            args=(self._db, open(self._file_path, "w")))
            thread.start()
            thread.join()
            return True

        return False

    def get(self, key, default=None):
        """
        get value assocaited with a key
        :param key: targeted key value
        :param default: default value
        :returns: value or default value
        """
        if key not in self._db:
            return default

        return self._db[key]

    def set(self, key, value, override=True):
        """
        set a new value for the given key
        :param key: targeted key
        :param value: associated value
        :param override: would not override if set to false
        :returns True: on success
        """
        if not override and key in self._db:
            return False

        self._db[key] = value
        self.dump(force=False)
        return True

    def delete(self, key):
        """
        delete the value associated with key
        :param key: targeted key
        :returns: True on success
        """
        if not key in self._db:
            return False

        del self._db[key]
        return True

    def clear(self):
        """
        clear the entire database
        :returns: True on success
        """
        self._db.clear()
        self.dump(force=False)
        return True

    def has(self, key):
        """
        check whether a value exists in database
        :param key: targeted key
        :returns: True if key exists
        """
        return key in self._db

    def pop(self, key, default=None):
        """
        pop an item from the database
        :param key: targeted key
        :param default: default value
        :returns: value or default
        """
        value = self._db.pop(key, default)
        self.dump(force=False)
        return value

    def copy(self):
        """make a copy of the database's dictionary"""
        return self._db.copy()

    def keys(self):
        """:returns: a list of the keys in the database"""
        return self._db.keys()

    def values(self):
        """:returns: a list of the values in the database"""
        return self._db.values()

    def items(self):
        """:returns: returns a list of tuples of key values"""
        return self._db.items()

    def __setitem__(self, key, value):
        """set a new item to the database"""
        return self.set(key, value)

    def __getitem__(self, key):
        """get an item from the database"""
        return self.get(key)

    def __len__(self):
        """get the size of the database"""
        return len(self._db)

    def __delitem__(self, key):
        """delete an item from the database"""
        return self.delete(key)

    def __iter__(self):
        """make an iterable from the database"""
        return iter(self._db)

    def __contains__(self, key):
        """check whether database contains a key"""
        return self.has(key)
