while True:
    print("Student Grading System")
    print("1. Add Student Marks")
    print("2. Generate Report Card")
    print("3. Exit")

    choice = input("Enter Your Choice (1 - 3)")

    if choice == '1':

        name = input("Enter Your Name: ")
        maths = input("Enter Maths Marks: ")
        science = input("Enter Science Marks: ")

        with open("students.txt" , "a") as file:
            file.write(f"{name},{maths},{science}\n")
            print(f"{name} Marks added successfully!") 

    elif choice == '2':

        try:
            with open("students.txt" , "r") as file:
                print("Result Card: ")
                for line in file:
                    data = line.strip().split(',')

                    name = data[0]
                    maths = int(data[1])
                    science = int(data[2])

                    total = maths + science
                    average = total / 2

                    if average >= 80:
                        grade = "A"

                    elif average >= 60:
                        grade = "B"

                    else:
                        grade = "C"

                    print(f"Student: {name} | Average: {average} | Grade: {grade}")

        except FileNotFoundError:
            print("students.txt File is not exist, firstly add student marks")

        except Exception as e:
            print(f"random error {e}")
    
    elif choice == '3':
        print("Exiting Program! ")
        break
    
    else:
        print("Invalid Choice, please select from (1 - 3)")
