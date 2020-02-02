from .table import Table, Record
from .index import Index
from src.bits import Bits

class Query:
    """
    # Creates a Query object that can perform different queries on the specified table 
    """

    def __init__(self, table):
        self.table = table
        pass

    """
    # internal Method
    # Read a record with specified RID
    """

    def delete(self, key):
        self.table.setSpecialVal(key)
        

    """
    # Insert a record with specified columns
    """

    def insert(self, *columns):
        schema_encoding = '0' * self.table.num_columns
        print(columns.length)
        # self.table.put(self.table.get_next_rid(),None,columns[0],schema_encoding,columns)
        self.table.put(self.table.get_next_rid(),None,columns[0],Bits('11111'),columns)
        # pass

    """
    # Read a record with specified key
    """

    def select(self, key, query_columns):
        pass

    """
    # Update a record with specified key and columns
    """

    def update(self, key, *columns):

        pass

    """
    :param start_range: int         # Start of the key range to aggregate 
    :param end_range: int           # End of the key range to aggregate 
    :param aggregate_columns: int  # Index of desired column to aggregate
    """

    def sum(self, start_range, end_range, aggregate_column_index):
        pass
