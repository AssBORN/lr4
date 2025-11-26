import csv

def read_csv_file(filename):
    with open(filename, 'r', encoding='windows-1251') as file:
        reader = csv.DictReader(file, delimiter='\t')
        return list(reader)

data = read_csv_file('employees.csv')

print("Исходные данные из файла:")
for person in data:
    print(person)

it_employees = list(filter(lambda x: x['Отдел'] == 'IT', data))
print("\nIT отдел:")
for emp in it_employees:
    print(f"{emp['Имя']} - {emp['Возраст']} лет - {emp['Зарплата']} руб")

increased_salary = list(map(
    lambda x: {**x, 'Зарплата': int(int(x['Зарплата']) * 1.1)},
    data
))
print("\nЗарплата после повышения:")
for emp in increased_salary:
    print(f"{emp['Имя']}: {emp['Зарплата']} руб")


