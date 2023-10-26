test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

cd ../../src

# Success : All required arguments are given
run test_succes1 python combine_plots.py --p1 'China_Average Temperature '+u'\xb0'+'C_vs_Emissions.png', --p2 'China_Rural population_vs_Emissions.png' --p3 'China_Urban population_vs_Emissions.png' --p4 'China_Forestland_vs_Emissions.png' --title 'Title' --outfile 'test_combine.png'
assert_no_stderr
assert_exit_code 0

# Failure : Not all required arguments are given 
run test_fail1 python combine_plots.py --p1 'China_Average Temperature '+u'\xb0'+'C_vs_Emissions.png'
assert_stderr
assert_exit_code 1

# Failure : File does not exist
run test_fail2 python combine_plots.py -p1 'France_Average Temperature '+u'\xb0'+'C_vs_Emissions.png', --p2 'China_Rural population_vs_Emissions.png' --p3 'China_Urban population_vs_Emissions.png' --p4 'China_Forestland_vs_Emissions.png' --title 'Title' --outfile 'test_combine.png'
assert_stderr
assert_exit_code 1