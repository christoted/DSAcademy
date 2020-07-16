# A collaborative data analysis effort by :
# Christopher Teddy
# Luis Anthonie Alkins
# Misael Jordan Enrico

import pandas as pd
import matplotlib.pyplot as plt
from EDA import Dataset

# Importing data and making object out of it
data    = pd.read_csv('used_car_data.csv')
dataset = Dataset(data)

# Removing unit of mileage
dataset.del_mileage_unit()

# Removing variable unit like 'bhp' and 'CC'
dataset.del_units('Power')
dataset.del_units('Engine')

# Adding Manufacturer column
dataset.add_manufacturer()

# Missing value info. Drops rows with at least one missing value.
dataset.missing_value(drop_nan = True,
                      export_data = True,
                      name_cleaned = 'cleaned_data.csv',
                      name_dropped = 'dropped_data.csv')

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
dataset.dist_below(160000)

# Nomor 5
# Plotting the distribution of kilometers driven
dataset.plot_dist('Kilometers_Driven', partitions = 1000)

# Nomor 6
# Plotting the boxplot of kilometers driven to identify outliers
dataset.plot_boxplot('Kilometers_Driven')

# Nomor 7
# Plotting the scatter of year with respect to kilometers driven and identify whether correlation is evident
dataset.plot_scatter('Year', 'Kilometers_Driven')

# Nomor 8
# Counting cars that is neither firsthand nor secondhand.
dataset.count_not_first(exclude_wear= ['First', 'Second'])

# Nomor 9
# Calculating average mileage by Fuel_Type
dataset.count_mileage_per_fuel('Fuel_Type', 'Mileage')

# Nomor 10
# Identifying which variables corelate with price of secondhand car
dataset.string2num(['Name', 'Manufacturer', 'Location', 'Fuel_Type', 'Transmission', 'Owner_Type'],
                   export_data = True,
                   name = 'numeric.csv')
dataset.heatmap_corr(save = True, filename = 'correlaton_matrix.png')