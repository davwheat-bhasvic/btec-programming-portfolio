_grades = [
    ["A*", "90"],
    ["A", "83"],
    ["B", "72"],
    ["C", "60"],
    ["D", "49"],
    ["E", "30"],
]

# Fixes the string-based marks
grades = []
for g in _grades:
    grades.append([g[0], int(g[1])])


def getMarksForGrade(grade):
    marks = 0

    for g in grades:
        if g[0] == grade:
            marks = g[1]

    return marks


def isValidGrade(grade):
    for g in grades:
        if g[0] == grade:
            return True

    return False


g = input("Enter grade: ")

if not isValidGrade(g):
    print("Invalid grade")
else:
    print(f"Marks for {g}: {getMarksForGrade(g)}")
