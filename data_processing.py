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


# Test Case 1: Calculate average temperature for all cities in Italy
italy_cities = cities_table.filter(lambda x: x['country'] == 'Italy')
italy_avg_temp = cities_table.aggregate('temperature', lambda temps: sum(temps) / len(temps), italy_cities)
print("The average temperature for all the cities in Italy:", italy_avg_temp)

# Test Case 2: Calculate average temperature for all cities in Sweden
sweden_cities = cities_table.filter(lambda x: x['country'] == 'Sweden')
sweden_avg_temp = cities_table.aggregate('temperature', lambda temps: sum(temps) / len(temps), sweden_cities)
print("The average temperature for all the cities in Sweden:", sweden_avg_temp)

# Test Case 3: Calculate min temperature in Italy
italy_min_temp = cities_table.aggregate('temperature', min, italy_cities)
print("The min temperature for all the cities in Italy:", italy_min_temp)

# Test Case 4: Calculate max temperature in Sweden
sweden_max_temp = cities_table.aggregate('temperature', max, sweden_cities)
print("The max temperature for all the cities in Sweden:", sweden_max_temp)