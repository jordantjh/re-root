# Root Fun Challenge
Programming Language: Python 3

## How to run the application
You will need to have Python 3 already installed on your machine, then

cd into the project folder
```
cd root-challenge
```
install dependencies
```
pip3 install -r requirements.txt
```
then execute *solution.py* with the input file *input1.txt* from the directory *inputs*
```
python3 solution.py inputs/input1.txt
```

## Assumptions
1. Assume each file line can only be either a blank line or one of the two formats specified in the problem statement.
2. Assume driver names are unique in a given .txt file, repeating names refers to the same person.
3. Assume "Driver" command will precede "Trip" commands for a particular driver.
4. Assume "Driver" command for the same driver name will only appear once in a .txt file.

## How I tested the application
Unit tested some edge cases including missing input file command-line argument, input file not found, division by zero when a trip has 0 travel time, empty input file, input file with blank lines in between commands, unknown input line format, etc.

Written a unit test for Driver class (inside directory 'models') that tests whether
the constructor sets an object's values correctly.

Written a unit test for the helper function 'find_time_delta' that tests whether
the function returns the correct difference between a start time and an end time, in hour unit.


## Running the tests
* To run the test for Driver class: 
Go to the root of the project, then
```
cd models
```
```
python3 -m unittest test_driver.py
```

* To run the test for helper function 'find_time_delta': 
Go to the root of the project, then
```
python3 -m unittest test_generate_report.py
```

## (Optional) Design Choices
1. I have refactored Driver class into directory 'models' because the Driver model should be a 
reusable component for other projects in the company.
2. I like to put test files in the same directory as the file they test so that executing the corresponding test file in the command line becomes convenient. 