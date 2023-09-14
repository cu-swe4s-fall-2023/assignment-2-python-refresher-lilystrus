country='United States of America'
country_column = 1
# for Savanna files use 3, for Forest fires use 4 (2 and 3 respectively when passing to get_column() )
# here assume fires are Forest fires 
fires_column = 4

# get current working directory; assumes the Agro file is in there 
import os 
cwd = os.getcwd()
file_name = cwd+'/Agrofood_co2_emission.csv'

# import the module containing get_column() and call it for parameters set above 
import my_utils as mu
fires = mu.get_column(file_name,country_column-1,country,fires_column-1)

# convert the string list 'fires' into a float list 'fires_num'
# add all elements of 'fires_num' to get total number of fires for all years documented in the Agro file
fires_num = [ float(i) for i in fires ] 
fires_sum = sum(fires_num)
print('The total number of (forest) fires in '+country+' is '+str(fires_sum))
