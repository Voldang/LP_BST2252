# -*- coding: utf-8 -*-

# Список студентов с правильным использованием u перед русскими строками
groupmates = [
    {
        "name": u"Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Анна",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": u"Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": u"Валентина",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    }
]

def print_students(students):
    """Функция для вывода списка студентов с русскими заголовками"""
    # Здесь тоже используем u перед русским текстом
    print u"Имя студента".ljust(15),
    print u"Группа".ljust(8),
    print u"Возраст".ljust(8),
    print u"Оценки".ljust(20)
    
    for student in students:
        print student["name"].ljust(15),
        print student["group"].ljust(8),
        print str(student["age"]).ljust(8),
        print str(student["marks"]).ljust(20)
    print "\n"

def filter_students_by_avg_mark(students, min_avg_mark):
    """Фильтрация студентов по среднему баллу"""
    filtered = []
    for student in students:
        marks = student["marks"]
        avg_mark = sum(marks) / float(len(marks))
        
        if avg_mark > min_avg_mark:
            filtered.append(student)
    
    return filtered

# ====== Вывод результатов ======
print u"Все студенты:"
print_students(groupmates)

print u"Студенты со средним баллом выше 4.0:"
good = filter_students_by_avg_mark(groupmates, 4.0)
print_students(good)

print u"Студенты со средним баллом выше 3.5:"
better = filter_students_by_avg_mark(groupmates, 3.5)
print_students(better)

print u"Студенты со средним баллом выше 3.0:"
all_above_3 = filter_students_by_avg_mark(groupmates, 3.0)
print_students(all_above_3)
