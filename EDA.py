import pandas            as pd
import numpy             as np
import matplotlib.pyplot as plt

from copy import deepcopy

class Dataset:
    def __init__(self, data):
        self.data                = data
        self.num_data            = np.shape(self.data)[0]
        self.nan_rows            = []
        self.unique_manufacturer = []

    def missing_value(self, drop_nan = False):

        row_nan       = self.data.isna().sum(axis = 1) != 0
        self.nan_rows = []

        for i in range(self.num_data):
            if row_nan[i] == 1:
                self.nan_rows.append(i)

        num_row_nan = row_nan.sum()

        print('\nNumber of row with missing value : ' + str(num_row_nan) + '\n')
        print('Missing value by column :')
        print(self.data.isna().sum(),'\n')

        if drop_nan == True:
            self.data     = self.data.drop(index = self.nan_rows).reset_index(drop = True)
            self.num_data = np.shape(self.data)[0]

        return self.nan_rows

    # def del_mileage_unit(self):
    #
    #     # We assume that the density of gasoline is 730Kg/m3 or 0.73Kg/l
    #     #
    #
    #     data_mileage = self.data.Mileage
    #     for i in range(self.num_data):


    def add_manufacturer(self):

        manufacturer = []

        for i in range(self.num_data):
            name = self.data.Name[i].split()[0]
            if name == 'ISUZU':
                name = 'Isuzu'
            manufacturer.append(name)

        self.data['Manufacturer'] = manufacturer

        self.unique_manufacturer = self.data.Manufacturer.unique()
        num_unique_manufacturer  = len(self.unique_manufacturer)

        print('\nNew manufacturer column added, which consists of ' + str(num_unique_manufacturer) + ' manufacturers.')
        print(self.unique_manufacturer)
        print()

    def count_manufacturer(self, export_data = False):

        manufacturer_count = self.data.Manufacturer.value_counts()
        manufacturer_count = pd.DataFrame({'Manufacturer': manufacturer_count.index, 'Count': manufacturer_count.values})

        print('\nNumber of car by manufacturer')
        print(manufacturer_count)

        if export_data == True:
            manufacturer_count.to_csv('jawaban_soal_1.csv', index = False)
            print('Output has been saved at jawaban_soal_1.csv\n')

        return(manufacturer_count)

    def count_used_per_city(self, export_data = False):

        dataset_used = deepcopy(self.data)
        drop_index   = []

        for i in range(self.num_data):
            if self.data.Owner_Type.iloc[i]  == 'First':
                drop_index.append(i)

        dataset_used   = dataset_used.drop(index = drop_index).reset_index(drop = True)
        location_count = dataset_used.Location.value_counts()
        location_count = pd.DataFrame({'Location': location_count.index, 'Count': location_count.values})

        print('\nCity with most secondhand car is : ' + str(location_count.iloc[0, 0]))
        print('Below is shown the number of used car per location')
        print(location_count)
        if export_data == True:
            location_count.to_csv('jawaban_soal_2.csv', index = False)
            print('Output has been saved at jawaban_soal_2.csv')
        print()

        return(location_count)

    def count_not_first(self, exclude_wear ='First'):

        dataset_used = deepcopy(self.data)
        drop_index = []

        for i, owner_type in enumerate(self.data.Owner_Type):
            if owner_type in exclude_wear:
                drop_index.append(i)

        dataset_used   = dataset_used.drop(index = drop_index).reset_index(drop = True)
        count_criteria = np.shape(dataset_used)[0]

        print('\nThe number of cars that is not ', end = '')
        for i, item in enumerate(exclude_wear):
            if i != len(exclude_wear) - 1:
                print(item, end = ' and ')
            else:
                print(item, end = ' ')
        print('ownership is ' + str(count_criteria) + '\n')

    # def plot_fuel_milage(self):
    #     fuel_types  = self.data['Fuel_Type'].unique()
    #     mean_milage = []
    #
    #     for i in range(self.num_data):
    #         mean_milage.append(self.data.loc[self.data['Fuel_Type'] == i].Mileage.mean())
    #
    #     plt.bar(fuel_types, height = mean_milage)
    #     plt.xlabel('Fuel types')
    #     plt.ylabel('Mean mileage ()')
    #     plt.

    def plot_dist(self, feature, partitions = 22, export_data = False, name = None):

        data_hist = self.data[feature]

        if export_data == True:
            freq_dist = data_hist.value_counts()
            freq_dist = pd.DataFrame({feature : freq_dist.index, 'count' : freq_dist.values}, dtype= float)
            freq_dist = freq_dist.sort_values(feature, axis = 0)
            freq_dist.to_csv(name, index=False)
            print('\nAnswer ' + name + ' has been saved.\n')

        plt.hist(data_hist, bins = partitions)
        plt.title('The histogram of ' + feature)
        plt.xlabel('Years')
        plt.ylabel('Frequency')
        plt.show()

    def plot_scatter(self, feature1, feature2):
        data_x = self.data[feature1]
        data_y = self.data[feature2]

        plt.scatter(data_x,data_y)
        plt.title('The scatter plot of ' + feature1 + ' and ' + feature2)
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()

    def dist_below(self, x = 50000):

        dist_below_x = (self.data.Kilometers_Driven < x).sum()
        print('\nThe number of cars with distance traveled below ' + str(x) + ' KM is : ' + str(dist_below_x) + '\n')
        return dist_below_x