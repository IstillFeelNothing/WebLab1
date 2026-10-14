import requests

API_URL = "http://localhost:8000/api/cars"


def fetch_cars():
    print(f"Звернення до сервера: {API_URL} ...\n")

    try:
        response = requests.get(API_URL, timeout=5)

        if response.status_code == 200:
            cars = response.json()

            print(f"{'ID':<12} | {'Марка':<12} | {'Країна':<10}")
            print("-" * 40)

            for car in cars:
                car_id = car.get("id", "N/A")
                name = car.get("name", "N/A")
                country = car.get("country", "N/A")
                print(f"{car_id:<12} | {name:<12} | {country:<10}")

            print("-" * 40)
            print(f"Успішно отримано записів: {len(cars)}")

        else:
            print(f"Помилка сервера! Код статусу: {response.status_code}")
            print("Відповідь:", response.text)

    except requests.exceptions.ConnectionError:
        print("Помилка підключення: сервер недоступний.")
        print(
            "Переконайся, що PHP-сервер запущено командою: php -S localhost:8000"
        )
    except requests.exceptions.Timeout:
        print("Помилка: час очікування відповіді від сервера вичерпано.")
    except Exception as e:
        print(f"Непередбачена помилка: {e}")


fetch_cars()