test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

cd ../../src

# Success : All required arguments are given 
run test_succes1 python scatterplt.py --xfile 'Greece_|total_emission.txt' --yfile 'Greece_Rural population.txt' --xlabel 'x-var' --ylabel 'y-var' --outfile 'test_scatter.png'
assert_no_stderr
assert_exit_code 0

# Failure : Not all required arguments are given 
run test_fail1 python scatterplt.py --xfile 'Greece_|total_emission.txt'
assert_stderr
assert_exit_code 1

# Failure : File does not exist
run test_fail2 python scatterplt.py --xfile 'France_|total_emission.txt' --yfile 'France_Rural population.txt' --xlabel 'x-var' --ylabel 'y-var' --outfile 'test_scatter.png'
assert_stderr
assert_exit_code 1

