# get current working directory; assumes the Agro file is in there 
import os 
cwd = os.getcwd()
file_name = cwd+'/Agrofood_co2_emission.csv'

country='United States of America'
country_column = 1

# if you want to look into the Savanna fires, you need column 3 
which_fires = 3

# import the module containing get_column() and call it for parameters set above 
import my_utils as mu
fires = mu.get_column(file_name,country_column,country,which_fires)

# convert the string list 'fires' into a float list 'fires_num'
# add all elements of 'fires_num' to get total number of fires for all years documented in the Agro file
fires_num = [ float(i) for i in fires ] 
fires_sum = sum(fires_num)
print('First, call get_column() for the Savanna fires : Their total number in '+country+' is '+str(fires_sum))

# then look into the Forest fires, which is column 4 
which_fires = 4 
fires = mu.get_column(file_name,country_column,country,which_fires)
fires_num = [ float(i) for i in fires ] 
fires_sum = sum(fires_num)
print('Then, call get_column() for the Forest fires: Their total number in '+country+' is '+str(fires_sum))
