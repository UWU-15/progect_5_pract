def get_int_input(prompt):
    """
    Запрашивает у пользователя ввод целого числа, пока ввод не будет корректным.

    Аргументы:
        prompt (str): Сообщение, выводимое пользователю.

    Возвращаемое значение:
        int: Корректное целое число, введенное пользователем.

    Примеры:
        >>> get_int_input("Введите число:")
        Введите число: 10
        10
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число")
def get_float_input(prompt):
    """
    Запрашивает у пользователя ввод вещественного числа, пока ввод не будет корректным.

    Аргументы:
        prompt (str): Сообщение, выводимое пользователю.

    Возвращаемое значение:
        float: Корректное вещественное число, введенное пользователем.

    Примеры:
        >>> get_float_input("Введите число:")
        Введите число: 3.14
        3.14
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Пожалуйста, введите число")


            