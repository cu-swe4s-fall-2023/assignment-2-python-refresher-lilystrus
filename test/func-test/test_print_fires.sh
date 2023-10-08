test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

cd ../../src

# Success : All required arguments are given and no operation is requested
run test_exit_codes python print_fires.py --country 'United States of America' --country_column 1 --file_name 'Agro_co2_USA.csv' --fires_column 4
assert_in_stdout 'Number'
assert_exit_code EX_OK=1

# Success : All required arguments are given and the mean is requested
run test_exit_codes python print_fires.py --country 'United States of America' --country_column 1 --file_name 'Agro_co2_USA.csv' --fires_column 4 --operation 'mean'
assert_in_stdout 'Mean'
assert_exit_code EX_OK=0

# Success : All required arguments are given and the median is requested
run test_exit_codes python print_fires.py --country 'United States of America' --country_column 1 --file_name 'Agro_co2_USA.csv' --fires_column 4 --operation 'median'
assert_in_stdout 'Median'
assert_exit_code EX_OK=0

# Success : All required arguments are given and the standard deviation is requested
run test_exit_codes python print_fires.py --country 'United States of America' --country_column 1 --file_name 'Agro_co2_USA.csv' --fires_column 4 --operation 'std'
assert_in_stdout 'Standard'
assert_exit_code EX_OK=0

# Failure : The wrong number of arguments is supplied 
run test_exit_codes python print_fires.py --file_name 'Agro_co2_USA.csv' --operation 'mean'
assert_stderr
assert_exit_code EX_USAGE=64

# Failure : An incorrect filename is supplied 
run test_exit_codes python print_fires.py --file_name 'Agrofood_co2_USA.csv' --operation 'mean'
assert_stderr
assert_exit_code EX_NOINPUT=66

# Failure : The user thinks the column numbering starts from zero
run test_exit_codes python print_fires.py --country 'United States of America' --country_column 0 --file_name 'Agro_co2_USA.csv' --fires_column 4 
assert_in_stdout 'Invalid input for Columns'
assert_exit_code EX_USAGE=64

# Failure : The user requests an unsupported operation
run test_exit_codes python print_fires.py --country 'United States of America' --country_column 1 --file_name 'Agro_co2_USA.csv' --fires_column 4 --operation 'variance'
assert_in_stdout 'Invalid input for requested operation'
assert_exit_code EX_USAGE=64