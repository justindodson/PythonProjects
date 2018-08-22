from card_template import Student, ExcelStudent, Template, print_template
from excel_extractor import ExcelData

print()
print("Welcome to the CPR Card Template Creator")
# print()
print("________________________________________")
print()

# Basic menu
def menu():
    print("________________________________________")
    print()
    print("Please Select from on of the following options: ")
    print("1.) Create a new CPR/First Aid Card")
    print("2.) Batch upload using Excel Document")
    print("3.) Quit ")

# call the menu
menu()

# instantiate an empty selection variable
selection = input()

# begin while loop that runs as long as the value entered is not a 3 (quit)
while int(selection) != 3:

    # exit the while loop and terminate
    if int(selection) == 3:
        print("Good Bye")

    # Creates a single template and will prompt the user for each data input
    elif int(selection) == 1:
        print("        Card Template Creator")
        print("_______________________________________")
        file_name = input("Enter a name for the Created Template File: \n")
        student = Student()
        template = Template(student, file_name)
        template.create_template()

    # selection to export the data from an excel file
    elif int(selection) == 2:
        print("Creating Batch Cards from Excel File")
        print("_______________________________________")
        class_size = input("How many students in the class: ")
        batch_doc_name = input("Input the file name of the batch upload spreadsheet: ")

        # creates the ExcelData Document
        batch_doc = ExcelData(class_size, batch_doc_name)

        # empty list to store each created student object
        created_students = []

        # counter starting at one to represent each row in the document and count up to the class size
        # the class_size argument will tell the program when all the cells containing
        # students have been read.
        # the while loop will iterate each student's information in the excel
        # document, create that student object, and store the object in the list
        counter = 1
        while counter <= int(class_size):
            new_student = batch_doc.create_student(counter + 2)
            created_students.append(new_student)
            counter += 1

        # loop through each student object in the created_students list and
        # generate a template card for each one.
        for student in created_students:
            file_name = student.site_name + student.user
            template = Template(student, file_name)
            template.create_template()


    # extra option to for performing a console print of the Word template for
    # adjusting the format and layout of the document. (Developer used only)
    elif int(selection) == 0:
        print_template()

    # if invalid option, through an error and print the menu again.
    else:
        print("Select a Valid Menu Option (1, 2, or 3)")
        menu()

    # prompt for the user to create another template set
    # and terminate program if not 'y'
    selection = input("Would you like to create another template? [y/n]\n")
    if selection == 'y':
        menu()
        selection = input()
    else:
        print("Good Bye")
        break
