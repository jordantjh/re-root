# Re-Root
Programming Language: Python 3

## How to run the application
You will need to have Python 3 already installed on your machine, then

cd into the project folder
```
cd re-root
```
install dependencies (mainly just PyTest)
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
I have fragmented the solution code into many individual classes and methods and unit-tested most of them to ensure they run as expected. Some of the edge cases the tests cover include missing input file command-line argument, input file not found, division by zero when a trip has 0 travel time, empty input file, input file with blank lines in between commands, unknown input line format, etc. A total of 14 test suites have been written.

## Running the tests
Navigate to the root of the project, then simply do
```
pytest
```

## (Optional) Design Choices
1. I have refactored the report printing functionality into a standalone class 'Report' because this gives us a more granular control for testing and also makes updating or extending the printing functionality easier in the future.
2. I like to put test files in the same directory as the file they test so that we can easily access the corresponding test files when we work on the code.