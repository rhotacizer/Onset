import csv

class Table():
    '''A Table is an object which represents a 2-dimensional CSV file. Both rows
    and columns can be accessed via their key as in a dictionary. This means that
    keys cannot appear as both a row and column label.'''

    def __init__(self, filename):
        self._internal_table = self.load_from_filename(filename)

    def load_from_filename(self, filename):
        '''Load a CSV file into a list of lists. The following CSV:
            ,a,b,c
           d,1,2,3
           e,4,5,6
           f,7,8,9
        would become the list:
           [['', 'a', 'b', 'c'],
            ['d', '1', '2', '3'] ...]'''
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            return [row for row in reader]

    def get_row(self, key):
        '''Gets a list containing all elements of the row specified by key.
        Returns a ValueError if the row doesn't exist.'''
        for row in self._internal_table:
            if row[0] == key:
                return row[1:]
        raise ValueError('Row not found')

    def get_column(self, key):
        '''Gets a list containing all elements of the column specified by key.
        Returns a ValueError if the column doesn't exist.'''
        for i, column in enumerate(self._internal_table[0]):
            if column == key:
                return [row[i] for row in self._internal_table[1:]]
        raise ValueError('Column not found')

    def __getitem__(self, key):
        '''Returns the row or column linked to the given key, accessed using
        subscript notation.'''
        if not isinstance(key, str):
            raise TypeError('Key must be a string')

        try:
            return self.get_row(key)
        except ValueError:
            try:
                return self.get_column(key)
            except ValueError:
                raise ValueError('Key not found in table')