test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

cd ../../src

# Success : All required arguments are given
run test_succes1 python extract_columns.py --filename 'Agro_co2_USA.csv' --col_title 'total_emission' --country 'United States of America'
assert_no_stderr
assert_exit_code 0

# Failure : Not all required arguments are given 
run test_fail1 python extract_columns.py --filename 'Agro_co2_USA.csv' 
assert_stderr
assert_exit_code 1

# Failure : File does not exist
run test_fail2 python extract_columns.py --filename 'Agro_co2.csv' --col_title 'total_emission' --country 'United States of America'
assert_stderr
assert_exit_code 1
