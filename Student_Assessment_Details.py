def main_menu():
    print("="*60)
    print("\nWelcome to the Student and Assessment Managemenet System")
    print("\n<A> add details of a student\n<I> insert assignment marks of a student\n<S> search assessment marks for a student\n<Q> quit\n")
    print("="*60)
    choice = input("\nPlease select an option from the above : ")
    if choice == "A":
        add_student()
    elif choice == "I":
        insert_marks()
    elif choice == "S":
        search_marks()
    elif choice == "Q":
        quit()
    else:
        print("Invalid Input.!\n Please try again")
        main_menu()

     
def add_student():
    try:
        student_ID = int(input("\nPlease enter the student ID : "))
        if check_student_ID_exist(student_ID):
            print("ID already exist\nTry again.")
            add_student()
        else:
            student_name = input("Please enter the student name : ")
            course = input("Please enter the course : ")
            write_std_detail(student_ID,student_name,course)
            print("\n\nThank You!\n")
            print("The details of the student you entered are as follows : \n")
            print("Student ID : ",student_ID,"\nStudent name : ",student_name,"\nCoursse : ",course)
            print("\nThe record has been successfully added to the student.txt file.")
            flag = True
            while True:
                continue_add = input("\nDo you want to enter details for another student(Y/N) ? ")
                if continue_add == "Y":
                    flag = False
                    add_student()
                elif continue_add == "N":
                    flag = False
                    main_menu()
                else:
                    print("Invalid Input!")
                    continue
    except(ValueError):
        print("\nPlease Enter Integer Number")
        add_student()


def insert_marks():
    try:
        student_ID = int(input("\nPlease enter the student ID : "))
        if check_assessment_ID_exist(student_ID):
            print("Student ID already exist.")
            insert_marks()
        else:
            subject_code = input("Please enter the subject code : ")
            assessment_no = int(input("Please enter the assessment number : "))
            assessment_marks = int(input("Please enter assessment marks : "))
            write_assess_marks(student_ID,subject_code,assessment_no,assessment_marks)
            print("\n\nThank You!\n")
            print("The details of the student you entered are as follows : \n")
            print("Student ID : ",student_ID,"\nSubject code : ",subject_code,"\nAssessment number : ",assessment_no,"\nAssessment marks : ",assessment_marks)
            print("\nThe record has been successfully added to the assessment.txt file.")
            flag = True
            while True:
                continue_marks = input("\nDo you want to enter marks for another student(Y/N) ? ")
                if continue_marks == "Y":
                    flag = False
                    insert_marks()
                elif continue_marks == "N":
                    flag = False
                    main_menu()
                else:
                    print("Invalid Input!")
                    continue
    except(ValueError):
        print("\nPlease Enter Integer Number")
        insert_marks()


def search_marks():
    try:
        student_ID = int(input("\nPlease enter the student ID you want to search assessment marks for : "))
        if not check_student_ID_exist(student_ID):
            print("Sorry ID does not exist!")
        else:
            value_found = access_details(student_ID)
            print("\nThank You!\n")
            print("A student has been found : ")
            print("Student ID : ",value_found[0][0],"\nStudent name : "," ".join(value_found[0][1:-1]),"\nCourse : ",value_found[0][-1])
            print("\nSubject Code\tAssessment Number\tMarks")
            print(""+value_found[1][1],"\t\t",value_found[1][2],"\t\t\t",value_found[1][3])
            flag = True
            while True:
                continue_search = input("\nDo you want to search assessment marks for another student (Y/N)? ")
                if continue_search == "Y":
                    flag = False
                    search_marks()
                elif continue_search == "N":
                    flag = False
                    main_menu()
                else:
                    print("Invalid Input!")
                    continue
    except(ValueError):
        print("\nInvalid student ID! ")
        search_marks()
       
def write_std_detail(student_ID,student_name,course):
    std_file = open("students.txt",'a')
    std_value = str(student_ID)+" "+student_name+" "+course+"\n"
    std_file.write(std_value)
    std_file.close()


def write_assess_marks(student_ID,subject_code,assessment_no,assessment_marks):
    assess_file = open("assessments.txt",'a')
    assess_value = str(student_ID)+" "+subject_code+" "+str(assessment_no)+" "+str(assessment_marks)+"\n"
    assess_file.write(assess_value)
    assess_file.close()


def check_student_ID_exist(student_ID):
    try:
        std_ = []
        with open("students.txt") as students:
            for line in students:
                std_.append(line)
            for value in std_:
                std = value.split(" ")
                if int(std[0])==student_ID:
                    return True
            else:
                return False
        students.close()
    except:
        print("New file created")


def check_assessment_ID_exist(student_ID):
    try:
        ass_ = []
        with open("assessments.txt") as assessments:
            for line in assessments:
                ass_.append(line)
            for value in ass_:
                ass = value.split(" ")
                if int(ass[0])==student_ID:
                    return True
            else:
                return False
        assessments.close()
    except:
        print("New file Created")


def access_details(student_ID):
    std_ = []
    with open("students.txt") as students:
        for line in students:
            std_.append(line)
    ass_ = []
    with open("assessments.txt") as assess:
        for line in assess:
            ass_.append(line)
    for value in std_:
        std = value.split(" ")
        if int(std[0])==student_ID:
            break
    for value in ass_:
        ass = value.split(" ")
        if int(ass[0])==student_ID:
            break
    return std,ass
    students.close()
    assess.close()
    

if __name__=="__main__":
    main_menu()


    
