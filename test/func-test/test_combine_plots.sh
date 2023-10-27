test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

cd ../../src

# Success : All required arguments are given
run test_succes1 python combine_plots.py --p1 't1.png', --p2 't2.png' --p3 't3.png' --p4 't4.png' --title 'Title' --outfile 'test_combine.png'
assert_no_stderr

# Failure : Not all required arguments are given 
run test_fail1 python combine_plots.py --p1 't1.png' 
assert_stderr

# Failure : File does not exist
run test_fail2 python combine_plots.py -p1 'France_Average Temperature '+u'\xb0'+'C_vs_Emissions.png', --p2 'China_Rural population_vs_Emissions.png' --p3 'China_Urban population_vs_Emissions.png' --p4 'China_Forestland_vs_Emissions.png' --title 'Title' --outfile 'test_combine.png'
assert_stderr