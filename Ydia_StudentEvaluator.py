#ACTIVITY 2 QUARTER 2 SEBASTIAN YDIA
#Sir who needs local variables haha  not me trust

# DEFINE FUNCTIONS
def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")
    print("==============================================================================")


def get_student_info():
    global i1,i2,i3, name #GLOBAL
    name = input("Enter Student Name: ")
    i1 = int(input("Enter Assessment 1: "))
    i2 = int(input("Enter Assessment 2: "))
    i3 = int(input("Enter Assessment 3: "))


def evaluate_performance():
    global average, level #GLOBAL
    average = (i1 + i2 + i3)/3
    if average >= 90:
        level = "Outstanding"
    elif average >= 85:
        level = "Very Satisfactory"
    elif average >= 80:
        level = "Satisfactory"
    elif average >= 75:
        level = "Fairly Satisfactory"
    else:
        level = "Needs Improvement"
    return level


def display_report():
    print(f'''STUDENT PERFORMANCE REPORT
Student Name: {name}
Assessment scores: {i1}, {i2}, {i3}
Average Score: {average:.2f}
Performace Level: {level}
''')


#ACTUAL PROGRAM
display_header()
get_student_info()
evaluate_performance()
display_report()