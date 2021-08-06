import matplotlib.lines
import numpy as np
import pandas as pd
# Import the cars.csv data: cars
cars = pd.read_csv('mtcars.csv')
# Print out cars
print(cars)

#20. Using head() to read first 5 rows and tail() to read last 5 rows:
print(cars.head())
print(cars.tail())

#21. Use columns to read only the columns header:
print(cars.columns)

#22. Display the original index:
print(cars.index)

#23. Create another dataframe by spliting the Car Brand and Model
car = cars['model'].str.split(' ', n = 1, expand = True)
print(car.head())

#24. Assign the new car brand and models back to the original dataframe.
cars = cars.assign(car_brand=car[0])
cars = cars.assign(car_model=car[1])
print(cars[cars['car_brand'] == 'Mazda'])

#25. Change the index to Car model:
cars.index = cars['model']
del cars['model']
print(cars.index)

#26. Summarize the first 6 column:
print(cars.iloc[:, :6].describe())

#27. Display the Car new info for 10 records:
print(cars.head(10))

#28. Find the mean for the dataframe columns:
print(cars.mean())

#29. Using matplotlib to plot a graph relationship between mile per gallon (mpg) to horse power(hp):
import matplotlib.pyplot as plt
plt.scatter(cars['mpg'], cars['hp'])
print(plt.show());

# #30. Using matplotlib to plot a bar chart to shows the horse power of each car model.
ax = cars[['car_model', 'hp']].plot(kind='bar', title = "Horse Power comparison", figsize=(10, 10), legend=True, fontsize=12)
print(plt.show());

# #31. Plot a histogram to show the category of Horse Power in most cars.
ax = cars['hp'].plot(kind='hist', title ="Range in HP", figsize=(10, 10), legend=True, fontsize=12)
print(plt.show());

#32. Saving the histogram diagram in a png format in the current directory of program executed.
my_fig = ax.get_figure()
my_fig.savefig("Car_Range_HP.png")
print(plt.show());
#33
ps = cars['mpg'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Models', fontsize=5)
plt.ylabel('Miles per gallon', fontsize=15)
plt.xticks(index, ps.index, fontsize=10, rotation=90)
plt.title('Miles per gallon of Cars')
plt.bar(ps.index, ps.values)
plt.show();

#38
def main():
    cars = pd.read_csv('mtcars.csv')
    car = cars['model'].str.split(' ', n = 1, expand = True)
    cars= cars.assign(car_brand=car[0])
    cars= cars.assign(car_model=car[1])
    cars.index = cars['model']
    del cars['model']

    plt.scatter(cars['mpg'], cars['hp'])
    plt.savefig("scatterDiagram_mpg_hp.png")

    ax = cars[['car_model', 'hp']].plot(kind='bar', title ="Horse Power comparison", figsize=(15, 15), legend=True, fontsize=12)
    my_fig = ax.get_figure()
    my_fig.savefig("horse_power_comparison.png")

    ax = cars['hp'].plot(kind='hist', title ="Range in HP", figsize=(10, 10), legend=True, fontsize=12)
    my_fig = ax.get_figure()
    my_fig.savefig("car_Range_HP.png")

if __name__== '__main__':
    main()
#40
from scipy.stats import linregress
stats = linregress(cars['mpg'], cars['hp'])
m = stats.slope
b = stats.intercept

# change the default figure size
plt.figure(figsize=(5,5))
plt.scatter(cars['mpg'], cars['hp'])
#set the linewidth on the regression line to
plt.plot(cars['mpg'], m * cars['mpg'] + b, color="red", linewidth=3)
plt.show()
