#Alex Jones
#2290441
#Assignment2

# sources used
# https://www.geeksforgeeks.org/inserting-variables-to-database-table-using-python/
# https://www.sqlitetutorial.net/sqlite-python/update/
# https://www.python-course.eu/sql_python.php
# https://www.jetbrains.com/help/pycharm/connecting-to-a-database.html
# https://www.tutorialspoint.com/How-to-catch-ImportError-Exception-in-Python
# https://datatofish.com/create-database-python-using-sqlite3/

import sqlite3
import sys

#establish connection
connection = sqlite3.connect('Students.db')
cursor = connection.cursor()

def create_connection(db_file):
    conn = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Exception as e:
        print(e)

    return connection

#creates a table
def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS Students(StudentID INT Primary Key, FirstName VARCHAR(32), LastName VARCHAR(32), GPA Numeric, Major VARCHAR(16), FacultyAdvisor VARCHAR(32), isDeleted boolean)')

#choices for user to choose from
def options():
    print(" ")
    print("Enter the number of the task you wish to do.")
    print("(1) to display All Students and their attributes.")
    print("(2) to create a new student")
    print("(3) to update a Student's Major or advisor")
    print("(4) to delete a Student record")
    print("(5) to search/display students by Major, GPA, and Advisor")
    print("(6) to exit")
    user_input = raw_input("Enter 1,2,3,4,5, or 6: ")

    if (user_input == "1"):
        Display()
        options()
    elif (user_input == "2"):
        Create()
        options()
    elif (user_input == "3"):
        Update()
        options()
    elif (user_input == "4"):
        Delete()
        options()
    elif (user_input == "5"):
        Search()
        options()
    elif (user_input == "6"):
        exit()
    else:
        print("Incorrect input. Please enter a correct number")
        options()

#prints all students in database with all their info
def Display():
     cursor.execute('SELECT * FROM Students WHERE isDeleted = 1')
     print("fetchall:")
     result = cursor.fetchall()
     for r in result:
         print(r)
     return result

#adds a new student to db
def Create():
    id = raw_input("What is the student id: ")
    F_name = raw_input("What is the student's first name: ")
    L_name = raw_input("What is the student't last name: ")
    GPA = raw_input("What is the student's GPA: ")
    Major = raw_input("What is the student's major: ")
    Advisor = raw_input("What is the name of their Faculty Advisor: ")
    cursor.execute("INSERT INTO Students (StudentID, FirstName, LastName, GPA, Major, FacultyAdvisor, isDeleted) VALUES(?,?,?,?,?,?,?)", (id, F_name, L_name, GPA, Major, Advisor, 1))

#changes a value in the database
def Update():
    y_or_no = raw_input("Do you want to update student's major? (y/n): ")
    if(y_or_no == "n"):
        y_or_no = raw_input("Do you want to update student's Advisor? (y/n): ")
        if(y_or_no == "n"):
            options() #exits this choice
        elif(y_or_no == "y"):
            stud_id = raw_input("What is the student id of the student who's advisor you want to update?: ")
            new_advisor = raw_input("What is the new adivisor's name?: ")
            cursor.execute("UPDATE Students SET FacultyAdvisor = ? WHERE StudentID = ?", (new_advisor, stud_id))
        else:
            print("Incorrect input")
            Update()
    elif(y_or_no == "y"):
            stu_id = raw_input("What is the student id of the student who's major you want to update?: ")
            new_major = raw_input("What is the new major?: ")
            cursor.execute("UPDATE Students SET Major = ? WHERE StudentID = ?", (new_major, stu_id))
    else:
        print("Incorrect input")
        options()

#changes isDeleted to 0 which means it will not show up in the print all  (soft deleted)
def Delete():
    delete_int = 0;
    studID_delete = raw_input("what is the student id of the student you wish to remove?: ")
    cursor.execute('UPDATE Students SET isDeleted = ? WHERE StudentID = ?', (delete_int, studID_delete))

#searches for student by major, gpa, or advisor
def Search():
    print("What do you want to search by?")
    choice = raw_input("Enter (m) to search by major, (g) to search by gpa, or (a) to search by advisor: ")
    if(choice == "m"):
        inputM = raw_input("What major do you want to look up?: ")
        cursor.execute('SELECT * FROM Students WHERE isDeleted = ? AND Major = ?', (1, inputM))
        print("students:")
        result = cursor.fetchall()
        for r in result:
            print(r)
        return result
    elif(choice == "g"):
        inputG = raw_input("What gpa do you want to look up?: ")
        cursor.execute('SELECT * FROM Students WHERE isDeleted = ? AND GPA = ?', (1, inputG))
        print("students:")
        result = cursor.fetchall()
        for r in result:
            print(r)
        return result
    elif(choice == "a"):
        inputA = raw_input("What advisor do you want to look up?: ")
        cursor.execute('SELECT * FROM Students WHERE isDeleted = ? AND FacultyAdvisor = ?', (1, inputA))
        print("students:")
        result = cursor.fetchall()
        for r in result:
            print(r)
        return result
    else:
        print("Incorrect input. Try again.")
        Search();

#main driver
def main():
    database = r"C:Students.db"
    sql_create_Students_table = "CREATE TABLE Students (StudentID INT Primary Key, FirstName VARCHAR(32), LastName VARCHAR(32), GPA Numeric, Major VARCHAR(16), FacultyAdvisor VARCHAR(32), isDeleted boolean);"
    connection = create_connection(database)
    if connection is not None:
        create_table() #create table
    else:
        print("Error!")

#calls these two functions to get started
main()
options()
