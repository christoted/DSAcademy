import pandas as pd
from   EDA import Dataset

data    = pd.read_csv('used_car_data.csv')
dataset = Dataset(data)

# Missing value info. Drops rows with at least one missing value.
dataset.missing_value(drop_nan = True)

# Check whether missing value still presist.
# dataset.missing_value()

# Adding manufacturer.
dataset.add_manufacturer()

# Nomor 1
# Counting cars by manufacturer.
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
# Tiati bahan bakarnya ada yg satuannya KM/L dan KM/Kg. Harus disamain dulu.
# Masih string pula...
# dataset.plot_scatter('Fuel_Type', 'Mileage')

# Nomor 10
