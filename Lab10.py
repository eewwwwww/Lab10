import pandas as pd

ps1 = pd.Series( [1,3,5,7,9])
ps2 = pd.Series( [2,4,6,8,10])
#ii)
ps = ps1 + ps2
my = pd.Series(ps)
print(my)

#iii)
ps = ps2 - ps1
on = pd.Series(ps)
print(on)

#iv)
ps = ps2 * ps1
off = pd.Series(ps)
print(off)

#v)
ps = ps2 / ps1
myvar = pd.Series(ps)
print(myvar)

#5)Compare the elements in the above series (compare will output Boolean result)
print(ps2 == ps1)
print(ps2 > ps1)
print(ps2 < ps1)

#6. Create a panda series with dictionary:
dict = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40, 'e': 50}
psd = pd.Series(dict)
print(psd)

#7. Create a numPy Array first before converting it to panda Series:
import numpy as np
np_array = np.array([10, 20, 30, 40, 50,])
print(np_array)

ps_numArray = pd.Series(np_array)
print(ps_numArray)

#8. Convert a panda series object to numeric:
s1 = pd.Series([10, '20', 'python', '40', '50'])
print(s1)

s2 = pd.to_numeric(s1, errors='coerce')
print(s2)

#9. Add new data to the s2 series:
s2 = s2.append(pd.Series([60, 70]))
print(s2)

#10. Sort the value of s2 series to sorted_s2:
sorted_s2 = s2.sort_values()
print(sorted_s2)

#11. Re-index sorted_s2 series:
sorted_s2.index = [1,2,3,4,5,6,7]
print(sorted_s2)

#12. Calculate the mean, median and standard deviation
print(round(sorted_s2.mean(),2))

print(sorted_s2.median())

print(round(sorted_s2.std(),2))

#13. Convert the above series to a list:
var1 = s2.values.tolist()
print(var1)
print(type(var1))

#14. Convert the above list to numpy array:
npArray = np.array(var1)
print(npArray)
print(type(npArray))

#15. Combine a series of list to panda series and store only the distinct color:
import pandas as pd
colorList = pd.Series([
    ['Red', 'Blue', 'Yellow'],
    ['Red', 'white'],
    ['Black']])
print(colorList)

s = colorList.apply(pd.Series).stack().reset_index(drop=True)
print(s)

#16. Create a dataframe using a single list or list of list:
list = [1,2,3,4,5]
df = pd.DataFrame(list)
print(df)

import pandas as pd
listOflist = [['Mike', 5], ['Peter', 10], ['Thomas, 15']]
df = pd.DataFrame(listOflist,columns=['Name', 'Age'])
print(df)

#17. Create a dataframe using a dictionary data structure:
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Bloemfontein"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98] }
brics = pd.DataFrame(dict)
print(brics)

#18. Change or set the index for brics.
# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]
# Print out brics with new index values
print(brics)