import csv

def read_csv_file(filename):
    with open(filename, 'r', encoding='windows-1251') as file:
        reader = csv.DictReader(file, delimiter='\t')
        return list(reader)

data = read_csv_file('employees.csv')

print("Исходные данные из файла:")
for person in data:
    print(person)

cleaned_data = list(map(
    lambda x: {
        'name': x['Имя'],
        'age': int(x['Возраст']),
        'salary': int(x['Зарплата']),
        'department': x['Отдел']
    },
    data
))

print("\nОчищенные данные:")
for person in cleaned_data:
    print(person)

it_employees = list(filter(lambda x: x['department'] == 'IT', cleaned_data))
print("\nIT отдел:")
for emp in it_employees:
    print(f"{emp['name']} - {emp['age']} лет - {emp['salary']} руб")

increased_salary = list(map(
    lambda x: {**x, 'salary': int(x['salary'] * 1.1)},
    cleaned_data
))
print("\nЗарплата после повышения:")
for emp in increased_salary:
    print(f"{emp['name']}: {emp['salary']} руб")

