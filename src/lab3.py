from collections import defaultdict
from functools import reduce
import datetime

# =================================================================
# Лабораторна робота №3
# Варіант 9: Аналіз даних про трафік (маршрути, час, кількість автомобілів)
# =================================================================


traffic_data = [
    {"date": "2023-10-01", "route": "Вокзальна - КНУБА", "time_min": 15, "cars": 450},
    {"date": "2023-10-02", "route": "Севастопольська - КНУБА", "time_min": 10, "cars": 320},
    {"date": "2023-10-03", "route": "Шулявська - КНУБА", "time_min": 25, "cars": 850},
    {"date": "2023-10-01", "route": "Лобановського - КНУБА", "time_min": 35, "cars": 1200},
    {"date": "2023-10-02", "route": "Солом'янська - КНУБА", "time_min": 5, "cars": 150}
]


def add_record(data, record):
    """Додає новий запис про трафік."""
    data.append(record)
    print("Запис додано успішно.")

def remove_record(data, index):
    """Видаляє запис про трафік за індексом."""
    if 0 <= index < len(data):
        del data[index]
        print("Запис видалено успішно.")
    else:
        print("Невірний індекс.")

def update_record(data, index, key, value):
    """Оновлює інформацію про трафік."""
    if 0 <= index < len(data):
 
        if key in ['time_min', 'cars']:
            try:
                value = int(value)
            except ValueError:
                print(f"Невірний тип значення для ключа '{key}'. Очікується ціле число.")
                return
        data[index][key] = value
        print("Інформацію оновлено успішно.")
    else:
        print("Невірний індекс.")

def find_records_by_route(data, route):
    """Знаходить всі записи для конкретного маршруту (без урахування регістру)."""
    return list(filter(lambda x: route.lower() in x["route"].lower(), data))


def calculate_total_cars(data):
    """Обчислює загальну кількість зафіксованих автомобілів."""
    return reduce(lambda acc, record: acc + record["cars"], data, 0)

def calculate_average_time(data):
    """Обчислює середній час у дорозі."""
    times = [record["time_min"] for record in data]
    return sum(times) / len(times) if times else 0


def sort_records_by_date(data):
    """Сортує записи про трафік за датою."""
    return sorted(data, key=lambda x: datetime.datetime.strptime(x["date"], "%Y-%m-%d"))


def group_records_by_route(data):
    """Групує записи за маршрутами."""
    routes = defaultdict(list)
    for record in data:
        routes[record["route"]].append(record)
    return dict(routes)

def find_most_congested_route(data):
    """Знаходить маршрут з найбільшою кількістю автомобілів (сумарно)."""
    if not data:
        return None
    routes = defaultdict(int)
    for record in data:
        routes[record["route"]] += record["cars"]
    return max(routes, key=routes.get)


def print_menu():
    """Виводить меню опцій."""
    print("\n==== Меню аналізу трафіку до КНУБА ====")
    print("1. Показати всі записи")
    print("2. Додати новий запис")
    print("3. Видалити запис")
    print("4. Оновити інформацію про запис")
    print("5. Знайти записи за назвою маршруту")
    print("6. Обчислити загальну кількість автомобілів")
    print("7. Групувати записи за маршрутами")
    print("8. Сортувати записи за датою")
    print("9. Знайти найбільш завантажений маршрут")
    print("10. Обчислити середній час у дорозі")
    print("0. Вийти")

def main():
    """Головна функція програми."""
    global traffic_data
    while True:
        print_menu()
        choice = input("Оберіть опцію: ")

        if choice == "1":
            if not traffic_data:
                print("Немає даних про трафік.")
            for i, record in enumerate(traffic_data):
                print(f"{i}: {record}")
                
        elif choice == "2":
            try:
                date = input("Введіть дату (YYYY-MM-DD): ")
                datetime.datetime.strptime(date, "%Y-%m-%d") 
                route = input("Введіть назву маршруту: ")
                time_min = int(input("Введіть час у дорозі (хв): "))
                cars = int(input("Введіть кількість автомобілів: "))
                new_record = {"date": date, "route": route, "time_min": time_min, "cars": cars}
                add_record(traffic_data, new_record)
            except ValueError:
                print("Помилка введення. Перевірте формат дати та числових значень (час, кількість авто).")
                
        elif choice == "3":
            try:
                index = int(input("Введіть індекс запису для видалення: "))
                remove_record(traffic_data, index)
            except ValueError:
                print("Невірний індекс. Введіть число.")
                
        elif choice == "4":
            try:
                index = int(input("Введіть індекс запису для оновлення: "))
                if not (0 <= index < len(traffic_data)):
                    print("Невірний індекс.")
                    continue
                key = input("Введіть ключ для оновлення (date/route/time_min/cars): ")
                if key not in traffic_data[0]:
                    print("Невірний ключ.")
                    continue
                value = input("Введіть нове значення: ")
                update_record(traffic_data, index, key, value)
            except ValueError:
                print("Невірний індекс. Введіть існуючий числовий індекс.")
                
        elif choice == "5":
            route = input("Введіть назву маршруту для пошуку: ")
            results = find_records_by_route(traffic_data, route)
            if results:
                for record in results:
                    print(record)
            else:
                print(f"Записи для маршруту '{route}' не знайдено.")
                
        elif choice == "6":
            total = calculate_total_cars(traffic_data)
            print(f"Загальна кількість зафіксованих автомобілів: {total}")
            
        elif choice == "7":
            grouped = group_records_by_route(traffic_data)
            for route, records in grouped.items():
                print(f"\nМаршрут: {route}:")
                for record in records:
                    print(f"  {record}")
                    
        elif choice == "8":
            sorted_records = sort_records_by_date(traffic_data)
            for record in sorted_records:
                print(record)
                
        elif choice == "9":
            best_route = find_most_congested_route(traffic_data)
            if best_route:
                print(f"Найбільш завантажений маршрут: {best_route}")
            else:
                print("Немає даних для аналізу.")
                
        elif choice == "10":
            avg_time = calculate_average_time(traffic_data)
            print(f"Середній час у дорозі: {avg_time:.2f} хв.")
            
        elif choice == "0":
            print("Дякуємо за використання програми!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()