import operator


def readStudentDetais():
    studentsMarks = {}
    print("Enter Number Students")
    numberOfStudents = int(input())
    for student in range(0, numberOfStudents):
        print("Enter Student name")
        studentName = input()
        print("Enter student marks")
        studentscore = int(input())
        studentsMarks[studentName] = studentscore
    return studentsMarks


def rankStudents(studentRecord):
    try:
        print()
        sortedStudentRecord = sorted(studentRecord.items(), key = operator.itemgetter(1), reverse=True)
        print(sortedStudentRecord)
        print("{} has scrored rank 1 with {} marks".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
        print("{} has scrored rank 1 with {} marks".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
        print("{} has scrored rank 1 with {} marks".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
        return sortedStudentRecord
    except IndexError:
        print("Enter a minimum of 3 Students")
        quit()    

def rewardStudents(sortedStudentRecord, reward):
    print("{} has received cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
    print("{} has received cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
    print("{} has received cash reward of ${}".format(sortedStudentRecord[2][0], reward[2]))


def appreciateStudents(sortedStudentRecord):
    for record in sortedStudentRecord:
        if record[1] >= 950:
            print("Great job {} scroring marks {}".format(record[0], record[1]))
        else:
            break

studentRecord = readStudentDetais()
sortedStudentRecord = rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
appreciateStudents(sortedStudentRecord)
