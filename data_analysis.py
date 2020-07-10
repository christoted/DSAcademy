import pandas as pd
import numpy  as np
from   EDA import Dataset

# Importing data and making object out of it
data    = pd.read_csv('used_car_data.csv')
dataset = Dataset(data)

# Missing value info. Drops rows with at least one missing value.
dataset.missing_value(drop_nan = True)

# Removing unit of mileage
dataset.del_mileage_unit()

# Removing variable unit like 'bhp' and 'CC'
dataset.del_units('Power')
dataset.del_units('Engine')

# Check whether missing value still presist.
dataset.missing_value(drop_nan = True)

# Nomor 1
# Counting cars by manufacturer.
dataset.add_manufacturer()
dataset.count_manufacturer(export_data = True)

# Nomor 2
# Counting used cars by location.
dataset.count_used_per_city(export_data = True)

# Nomor 3
# Graphing the frequency of cars being sold by year.
dataset.plot_dist('Year', partitions = 22, export_data = True, name = 'jawaban_soal_3.csv')

# Nomor 4
# The number of cars with distance traveled below 100.000 KM.
dataset.dist_below(100000)

# Nomor 5

# Nomor 6

# Nomor 7
# Nanti uji signifikansi parameter regresi linear pake ANOVA
dataset.plot_scatter('Year', 'Kilometers_Driven')

# Nomor 8
# Counting cars that is neither firsthand nor secondhand.
dataset.count_not_first(exclude_wear= ['First', 'Second'])

# Nomor 9
# Calculating average mileage by Fuel_Type
dataset.count_mileage_per_fuel('Fuel_Type', 'Mileage')

# Nomor 10