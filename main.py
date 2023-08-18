
from TestCase import *

i = -10
passed_tests = 0
inputObjectAB = TestCase("Find A and B: ", i, 1)
invalid_A = False
while passed_tests < 10:
    inputObjectAB.set_A(i)
    invalid_A = inputObjectAB.FindFailedTests()
    if(invalid_A == True):
        print("Invalid A = ", inputObjectAB.get_a())
        passed_tests = 0
    else:
        passed_tests += 1
    i += 1


