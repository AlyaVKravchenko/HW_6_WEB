from connection import create_connection
from typing import Union


def perform_query_from_file(file_path: str, params: Union[tuple, None] = None):
    with open(file_path, 'r') as file:
        query_str = file.read()

    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            if params is not None:
                cur.execute(query_str, params)
            else:
                cur.execute(query_str)
            result = cur.fetchall()
            cur.close()
            return result
        else:
            print("Error: can't create the database connection")
            return None


def find_top_students_by_avg_grade():
    """1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    query_file_path = "queries/query_1.sql"
    return perform_query_from_file(query_file_path)


def find_student_with_highest_avg_grade_by_subject():
    """2. Знайти студента із найвищим середнім балом з обраного предмета."""
    query_file_path = "queries/query_2.sql"
    return perform_query_from_file(query_file_path)


def find_avg_grade_by_groups():
    """3. Знайти середній бал у групах з певного предмета"""
    query_file_path = "queries/query_3.sql"
    return perform_query_from_file(query_file_path)


def find_avg_grade_for_all_grades():
    """4. Знайти середній бал на потоці (по всій таблиці оцінок):"""
    query_file_path = "queries/query_4.sql"
    return perform_query_from_file(query_file_path)


def find_teachers_vs_subjects():
    """5. Знайти які курси читає певний викладач:"""
    query_file_path = "queries/query_5.sql"
    return perform_query_from_file(query_file_path)


def find_students_by_group():
    """6. Знайти список студентів у певній групі:"""
    query_file_path = "queries/query_6.sql"
    return perform_query_from_file(query_file_path)


def find_grades_by_groups_and_subject():
    query_file_path = "queries/query_7.sql"
    return perform_query_from_file(query_file_path)


def find_avg_grade_by_teacher():
    """8. Знайти середній бал, який ставить певний викладач зі своїх предметів:"""
    query_file_path = "queries/query_8.sql"
    return perform_query_from_file(query_file_path)


def find_subjects_for_student():
    """9. Знайти список курсів, які відвідує студент:"""
    query_file_path = "queries/query_9.sql"
    return perform_query_from_file(query_file_path)


def find_subjects_for_student_by_teacher():
    """10. Список курсів, які певному студенту читає певний викладач:"""
    query_file_path = "queries/query_10.sql"
    return perform_query_from_file(query_file_path)

def find_avg_grades_for_student_by_teacher():
    """11. Середній бал, який певний викладач ставить певному студентові:"""
    query_file_path = "queries/query_e1.sql"
    return perform_query_from_file(query_file_path)


def find_grades_last_day():
    """12. Оцінки студентів у певній групі з певного предмета на останньому занятті."""
    query_file_path = "queries/query_e2.sql"
    return perform_query_from_file(query_file_path)




