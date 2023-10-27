test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

cd ../../src

# Success : All required arguments are given
run test_succes1 python extract_columns.py --filename 'Agro_co2_Afgha.csv' --col_title 'total_emission' --country 'Afghanistan'
assert_no_stderr

# Failure : Not all required arguments are given 
run test_fail1 python extract_columns.py --filename 'Agro_co2_Afgha.csv' 
assert_stderr

# Failure : File does not exist
run test_fail2 python extract_columns.py --filename 'Agro_co2.csv' --col_title 'total_emission' --country 'Afghanistan'
assert_stderr
