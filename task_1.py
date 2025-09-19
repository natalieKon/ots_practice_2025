# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: Кондратьева Наталья Владимировна

def get_system_info():
    """
    Эта функция должна вернуть словарь с информацией о вашей "системе".
    """
    # TODO: Заполните словарь вашими реальными данными
    system_info = {
        "student_name": "Кондратьева Наталья Владимировна",
        "academic_group": "ИВТИИбд-14",
        "github_link": "https://github.com/natalieKon"
    }
    return system_info

# Вывод информации для проверки
if __name__ == "__main__":
    info = get_system_info()
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")
