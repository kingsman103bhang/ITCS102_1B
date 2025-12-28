import os
import json

os.system('cls')

print('STUDENT INFORMATION SYSTEM')
print("=======================================")

# Empty dictionary
student_record = {}

while True:
    print("SELECT FOR THE FOLLOWING OPTIONS")
    print("A - ADD STUDENT RECORD")
    print("B - PRINT ALL STUDENT RECORD")
    print("C - SEARCH STUDENT RECORD")
    print("D - DELETE STUDENT RECORD")
    print("E - EDIT STUDENT RECORD")
    print("F - EXPORT STUDENT RECORD")
    print("G - IMPORT STUDENT RECORD")
    print("X - EXIT SYSTEM")
    print("=========================================")
    choice = input("SELECT FROM THE OPTIONS ABOVE ---> ").lower()

    if choice == 'a':
        os.system('cls')
        print("\nADDING STUDENT RECORD")
        id_no = input("Please input student ID number ---> ")
        first_name = input("Please input student First Name ---> ").upper()
        second_name = input("Please input student Second Name ---> ").upper()
        last_name = input("Please input student Last Name ---> ").upper()
        age = eval(input("Input student age ---> "))
        course = input("Input student Course ---> ").upper()
        section = input("Input student Section ---> ").upper()

        student_record[id_no] = [first_name,second_name,last_name, age, course,section]
        print("DATA SAVED SUCCESSFULLY")
        # Go back to the original menu
        continue
    elif choice == 'b':
        os.system('cls')
        print("PRINTING STUDENT RECORD")
        for i, j in student_record.items():
            print(f"STUDENT ID - {i}    |INFORMATION - {j}")
        continue
    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD")
        search_id = input("Input student id for search --> ").lower()
        for each_id in student_record.keys():
            if each_id in student_record.keys():
                print("==================================")
                print(f"\nRECORD FOUND for ID {search_id}")
                # to print the record for the search id
                for i in student_record[search_id]:
                    print(f"--- {i}")
                print("==================================")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'd':
        os.system('cls')
        print("DELETE STUDENT RECORD")
        search_id = input("Input student id for search --> ").lower()
        for each_id in student_record.keys():
            if each_id in student_record.keys():
                print("==================================")
                print(f"\nRECORD FOUND for ID {search_id}")
                # to print the record for the search id
                for i in student_record[search_id]:
                    print(f"--- {i}")
                print("==================================")
                student_record.pop(search_id)
                print("\nRECORD DELETE")
            elif search_id != student_record.items():
                print("NO RECORD FOUND")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'e':
        os.system('cls')
        print("EDIT/MODIFYG STUDENT RECORD")
        search_id = input("Input student id for search --> ").lower()
        for each_id in student_record.keys():
            if each_id in student_record.keys():
                print("==================================")
                print(f"\nRECORD FOUND for ID {search_id}")
                # to print the record for the search id
                for i in student_record[search_id]:
                    print(f"--- {i}")
                print("==================================")
                # new set of value for searched id
                first_name = input("Please input student First Name ---> ").upper()
                second_name = input("Please input student Second Name ---> ").upper()
                last_name = input("Please input student Last Name ---> ").upper()
                age = eval(input("Input student age ---> "))
                course = input("Input student Course ---> ").upper()
                section = input("Input student Section ---> ").upper()
                student_record[search_id][0] = first_name
                student_record[search_id][1] = second_name
                student_record[search_id][2] = last_name
                student_record[search_id][3] = age
                student_record[search_id][4] = course
                student_record[search_id][5] = section
            else:
                print("NO RECORD FOUND")
        continue
    elif choice == 'f':
        os.system("cls")
        print("EXPORT STUDENT RECORD")
        # json JavaScript Object Notation
                # w = write
        with open('student_record.json', 'w') as new_file:
            json.dump(student_record,new_file, indent=4)
        print("EXPORT SUCCESSFUL")
        continue
    elif choice == 'g':
        os.system("cls")
        print("IMPORT STUDENT RECORD")
                # r = read
        with open('student_record.json', 'r') as new_file:
            imported_student = json.load(new_file)
        student_record = imported_student
        print("IMPORT SUCCESSFUL")
        continue
    elif choice == 'x':
        break
    else:
        print("INVALID CHOICE")
        continue