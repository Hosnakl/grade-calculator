# Prompts the user for the grades on the tests.
# Each grade must be between 0 and 100 and is stored in a list
# The process is stopped when the user enters -1
# and then returns the list of tests.
def getGradeOfTests():
    listOfTests = []
    while True:
        try:
            testGrade = float(input("Type the grade of the test: (type -1 to quit) "))
            if 0 <= testGrade <= 100:
                listOfTests.append(testGrade)
            elif testGrade == -1:
                break
            else:
                print("Each grade must be between 0 and 100")
        except:
            print("Invalid input")
    return listOfTests


# Prompts the user for the grade on the assignments.
# The grade must be between 0 and 100 and is stored in a list
# The process is stopped when the user enters -1
# and then returns the list of tests.
def getGradeOfAssignments():
    listOfAssignments = []
    while True:
        try:
            assignmentGrade = float(input("Type the grade of the assignment: (type -1 to quit) "))
            if 0 <= assignmentGrade <= 100:
                listOfAssignments.append(assignmentGrade)
            elif assignmentGrade == -1:
                break
            else:
                print("Each grade must be between 0 and 100")
        except:
            print("Invalid input")
    return listOfAssignments


# Prompts the user for the weigth of Assignments
# This function will include call(s) to the input function
# Keep prompting until the number is a float >= 0 and <= 1
# Returns the weight of Test

def getWeightOfAssignments():
    while True:
        try:
            weightOfTest = float(input("What is weigth of assignments ? >"))
            if 1 < weightOfTest < 0:
                print("Number must be between 0 and 1")
            else:
                break
        except:
            print("Invalid input")

    return weightOfTest


# Prompts the user for the weigth of Tests
# This function will include call(s) to the input function
# Keep prompting until the number is a float >= 0 and <= 1
# Returns the weight of Test


def getWeightOfTests():
    while True:
        try:
            weightOfTest = float(input("What is weight of midterms ? >"))
            if 1 < weightOfTest < 0:
                print("Number must be between 0 and 1")
                continue
            else:
                break
        except:
            print("Invalid input")

    return weightOfTest


# Prompts the user for the weigth of the final
# This function will include call(s) to the input function
# Keep prompting until the number is a float >= 0 and <= 1
# Returns the weight of final


def getWeightOfFinal():
    while True:
        try:
            weightOfFinal = float(input("What is weigth of Final ? >"))
            if 1 < weightOfFinal < 0:
                print("Number must be between 0 and 1")
            else:
                break
        except:
            print("Invalid input")

    return weightOfFinal


# returns True if the sum of the 3 arguments is 1, False otherwise
# Assign the default values 0.4 0.35 0.25 to wAssign, wMidtern and wFinal respectively

def checkWeights(wAssign, wTest, wFinal):
    if wAssign + wTest + wFinal == 1:
        return True
    else:
        return False


# calculate and return the average grade of the assignments given a list of assignments
def calculateAverageAssignments(listOfAssignments):
    AvAssignment = sum(listOfAssignments) / len(listOfAssignments)
    return AvAssignment


# calculate and return the average grade of the tests given a list of tests

def calculateAverageTests(listOfTests):
    AvTest = sum(listOfTests) / len(listOfTests)
    return AvTest


# calculate the numeric grade as specified in the course outline

def calculateNumericGrade(AvAssignment, AvTest, final, wOfAssign, wOfTests, wFinal):
    numericGrade = float(AvAssignment * wOfAssign + AvTest * wOfTests + final * wFinal)
    return numericGrade


# convert the numeric grade to a letter according to the conversion table
# in the course outline


def calculateAlphaGrade(numericGrade):
    if 90 <= numericGrade <= 100:
        return "A+"
    elif 85 <= numericGrade <= 89:
        return "A"
    elif 80 <= numericGrade <= 84:
        return "A-"
    elif 77 <= numericGrade <= 79:
        return "B+"
    elif 73 <= numericGrade <= 76:
        return "B"
    elif 70 <= numericGrade <= 72:
        return "B-"
    elif 67 <= numericGrade <= 69:
        return "C+"
    else:
        return "F"


while True:
    # Get the weight value of the assignments (call the appropriate function)
    wA = getWeightOfAssignments()
    # Get the weight value of tests (call the appropriate function)
    wT = getWeightOfTests()
    # Get the weight value of the final (call the appropriate function)
    wF = getWeightOfFinal()

    # Check the sum of weight values is 1 (call the appropriate function)
    # Repeat the last four lines if not equal to 1
    if checkWeights(wA, wT, wF):
        break
    else:
        print("sum not equal to one")

# Get the grades of the assignments and calculate the average
AvgAssignments = calculateAverageAssignments(getGradeOfAssignments())

# Get the grades of the tests and calculate the average
AvgTests = calculateAverageTests(getGradeOfTests())

# Prompt and get the final grade
# Validate the input as a float between 0 and 100
while True:
    try:
        fT = float(input("What is grade of Final? >"))
        if 100 < fT < 0:
            print("Number must be between 0 and 100")
        else:
            break
    except:
        print("Invalid input")

# Calculate and display the final numeric grade (call the appropriate function)
finalNumeric = calculateNumericGrade(wA, wT, wF, fT, AvgAssignments, AvgTests)
print(finalNumeric)
# Calculate and display the final alphabetical grade (call the appropriate function)
print(calculateAlphaGrade(finalNumeric))
