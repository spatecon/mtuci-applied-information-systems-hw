var groupmates = [
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
];

var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length)
        str = str + ' ';
    return str;
};

var printStudents = function(students){
    console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 8),
        rpad("Возраст", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i<=students.length-1; i++){
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['age'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n');
};

var filterByGroup = function(students, group) {
    var result = [];
    for (var i = 0; i < students.length; i++) {
        if (students[i]['group'] === group) {
            result.push(students[i]);
        }
    }
    return result;
};

printStudents(groupmates);
console.log("Студенты группы БСТ2257:");
printStudents(filterByGroup(groupmates, "БСТ2257"));
