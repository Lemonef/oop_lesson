import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))
        
countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))


class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        self.table_database.append(table)

    def search(self, table_name):
        for table in self.table_database:
            if table.table_name == table_name:
                return table
        return None
        
class Table:
        
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table
        
    def filter(self, condition):
        filtered_list = []
        for item in self.table:
            if condition(item):
                filtered_list.append(item)
        return filtered_list
    
    def aggregate(self, aggregation_function, aggregation_key):
        values = []
        for item in self.table:
            if aggregation_key in item:  # Ensure the key exists
                values.append(float(item[aggregation_key]))
        
        if values:  # Only perform aggregation if there are values
            return aggregation_function(values)
        return None  # Return None if no values found

    def __str__(self):
        return f"Table({self.table_name}, {len(self.table)} rows)"
    
    
cities_table = Table("Cities", cities)
countries_table = Table("Countries", countries)

db = TableDB()
db.insert(cities_table)
db.insert(countries_table)