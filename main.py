from formula_1 import calculate_sh
from formula_2 import calculate_arctan
import utils

def main():
    """
    Основная функция программы, реализующая меню пользователя и вычисления.

    Подробное описание:
    Эта функция предоставляет пользователю интерактивное меню для выбора функций,
    ввода значений и получения результатов. Она также обрабатывает ошибки ввода
    и выводит соответствующие сообщения.

    Аргументы:
        Нет

    Возвращаемое значение:
        Нет

    Исключения:
        Нет

    Примеры:
        >>> main()
        (Запускается меню, пользователь взаимодействует)
    """
    while True:
        print("\nМеню:")
        print("1. Вычислить для функции sh(x)")
        print("2. Вычислить для функции arctg(x)")
        print("0. Выйти")

        choice = utils.get_int_input("Выберите пункт меню: ")

        if choice == 0:
            print("Программа завершена")
            break
        elif choice == 1:
            x = utils.get_float_input("Введите значение x: ")
            try:
                result = calculate_sh(x)
                print(f"sh({x}) ≈ {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")
            except TypeError as e:
                 print(f"Ошибка: {e}")
        elif choice == 2:
             x = utils.get_float_input("Введите значение x: ")
             try:
                result = calculate_arctan(x)
                print(f"arctg({x}) ≈ {result}")
             except ValueError as e:
                print(f"Ошибка: {e}")
             except TypeError as e:
                print(f"Ошибка: {e}")
        else:
            print("Некорректный выбор. Попробуйте еще раз")

if __name__ == "__main__":
    main()