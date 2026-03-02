groupmates = [
    {
        "name": "Павлюков",
        "group": "БСТ2257",
        "age": 21,
        "marks": [4, 5, 5, 4, 5]
    },
    {
        "name": "Иванов",
        "group": "БСТ2257",
        "age": 20,
        "marks": [3, 4, 3, 4, 3]
    },
    {
        "name": "Петрова",
        "group": "БСТ2257",
        "age": 21,
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": "Сидоров",
        "group": "БСТ2258",
        "age": 20,
        "marks": [3, 3, 4, 3, 4]
    },
    {
        "name": "Козлова",
        "group": "БСТ2258",
        "age": 19,
        "marks": [4, 4, 5, 4, 5]
    }
]


def print_students(students):
    print(
        "Имя студента".ljust(15),
        "Группа".ljust(10),
        "Возраст".ljust(10),
        "Оценки".ljust(20)
    )
    for student in students:
        print(
            student["name"].ljust(15),
            student["group"].ljust(10),
            str(student["age"]).ljust(10),
            str(student["marks"]).ljust(20)
        )
    print()


def filter_by_avg(students, min_avg):
    result = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg >= min_avg:
            result.append(student)
    return result


print_students(groupmates)

print("Студенты со средним баллом >= 4.0:")
filtered = filter_by_avg(groupmates, 4.0)
print_students(filtered)
