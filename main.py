from utils import (
                    find_student_with_highest_avg_grade_by_subject,
                    find_avg_grade_by_groups,
                    find_top_students_by_avg_grade,
                    find_avg_grade_for_all_grades,
                    find_teachers_vs_subjects,
                    find_students_by_group,
                    find_grades_by_groups_and_subject,
                    find_subjects_for_student,
                    find_avg_grade_by_teacher,
                    find_subjects_for_student_by_teacher,
                    find_grades_last_day,
                    find_avg_grades_for_student_by_teacher)

def main_menu():
    print("Оберіть опцію:")
    print("1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.")
    print("2. Знайти студента із найвищим середнім балом з певного предмета.")
    print("3. Знайти середній бал у групах з певного предмета.")
    print("4. Знайти середній бал на потоці (по всій таблиці оцінок).")
    print("5. Знайти які курси читає певний викладач.")
    print("6. Знайти список студентів у певній групі.")
    print("7. Знайти оцінки студентів у окремій групі з певного предмета.")
    print("8. Знайти середній бал, який ставить певний викладач зі своїх предметів.")
    print("9. Знайти список курсів, які відвідує студент.")
    print("10. Список курсів, які певному студенту читає певний викладач")

    print("11. Середній бал, який певний викладач ставить певному студентові.")
    print("12. Оцінки студентів у певній групі з певного предмета на останньому занятті")

    print("0. Вийти")

def process_user_choice(choice):
    if choice == '1':
        top_students = find_top_students_by_avg_grade()
        print("Топ студентів з найвищими середніми балами:")
        print(top_students)
    elif choice == '2':
        student_highest_avg_grade = find_student_with_highest_avg_grade_by_subject()
        print("Студент з найвищим балом за кожним предметом:")
        print(student_highest_avg_grade)
    elif choice == '3':
        avg_grade_by_groups = find_avg_grade_by_groups()
        print(f"Середній бал у групах з кожного предмета:")
        print(avg_grade_by_groups)
    elif choice == '4':
        avg_grades_from_grade = find_avg_grade_for_all_grades()
        print(f"Середній бал на потоці:")
        print(avg_grades_from_grade)
    elif choice == '5':
        teachers_subjects = find_teachers_vs_subjects()
        print(f"Якi курси читають викладачі:")
        print(teachers_subjects)
    elif choice == '6':
        students_by_group = find_students_by_group()
        print(f"Студенти по групам:")
        print(students_by_group)
    elif choice == '7':
        grades_by_subjects = find_grades_by_groups_and_subject()
        print(f"Оцінки студентів по групам і предметам:")
        print(grades_by_subjects)

    elif choice == '8':
        avg_grade_by_subject = find_avg_grade_by_teacher()
        print(f"Середній бал викладача по своїх предметах:")
        print(avg_grade_by_subject)
    elif choice == '9':
        students_by_subjects = find_subjects_for_student()
        print(f"Студенти по предметам:")
        print(students_by_subjects)
    elif choice == '10':
        subjects_for_student_by_teacher = find_subjects_for_student_by_teacher()
        print(f"Список курсів, які студенту читає викладач:")
        print(subjects_for_student_by_teacher)

    elif choice == '11':
        avg_grade = find_avg_grades_for_student_by_teacher()
        print(f"Студенти по предметам:")
        print(avg_grade)
    elif choice == '12':
        grades = find_grades_last_day()
        print(f"Список курсів, які студенту читає викладач:")
        print(grades)


if __name__ == '__main__':
    while True:
        main_menu()
        user_choice = input("Ваш вибір (0 для виходу): ")
        if user_choice == '0':
            print("Дякую за використання програми. До побачення!")
            break
        process_user_choice(user_choice)
