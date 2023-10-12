# best practices 

This repository demonstrates how to use best practices when writing source code. The specific features demonstrated here are :

1) The use of docstrings and comments for documentation of functions, programs and specific blocks of code

2) The use of a parser to read user input from the command line instead of sys.argv[]

3) The proper use of whitespaces, indentation and blank lines that will make your code PEP8 compatible

4) The use of the try,except error handling method for reading files and converting values from one type to    
   another
   
5) How to write code using functions that do only one thing, and calling other functions within functions if 
   a function needs to do more than one thing. 

6) The use of a main() function in programs that contain code in functions and code that needs to be executed   
   every time you call the program.

# unit and functional testing

A unit test for the library my_utils has been added, as well as a functional test using the Stupid Simple baSh Testing framework (https://github.com/ryanlayer/ssshtest). Major changes from the previous version include :

1) A unit test python file (under test/unit-test) that checks the behavior of all functions of the my_utils library. It checks for file read, user input errors and errors in calculations. 

2) A functional test file that uses the ssshtest framework. Both success and fail runs are tested using the directives assert_in_stdout, assert_exit_code and assert_stderr.

3) Changes to my_utils for the option to output the mean, median or standard deviation of the yearly fires as requested by the user. 

4) Improved error messages.

5) A work-around for sys.path.append() that allows importing libraries and opening files while running from different folders than these of the libraries/files. Need to investigate with sys.path.append() is not working locally. 

# Continous Integration with GitHub Actions

1) A Tests.yml was added to the repository in branch ci. It checks that unit tests, functional tests and style checks on the files of Assignment 4 are able to run on a pristine OS on a machine other than that of the developer of the repository. Specifically, the presumed environment does not have pip and pycodestyle installed. 

2) Conda installs but is not able to locate pycodestyle. Mamba does not install at all. In the case of Mambe, the tests do not run at all, they quote an error on line 1, which is not altered when Mamba is used. We therefore resorted to using pip install pycodestyle and installing pip before that. 