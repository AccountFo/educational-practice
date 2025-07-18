import math

MAX_NUM = 1500  #Ограничение для ввода для быстрого расчета (чтобы не выйти за дефолтный лимит Python)

def get_valid_number():

    """
    Запрос числа и проверка на корректность.   
    Возвращает:
        int: Число от 0 до MAX_NUM.
    """

    while True:
        user_num = input(f"Введите число от 0 до {MAX_NUM}: ")
        try:
            num = int(user_num)
            if num < 0:
                print("Ошибка! Число не может быть отрицательным")
            elif num > MAX_NUM:
                print(f"Ошибка! Число не должно превышать {MAX_NUM}")
            else:
                return num
        except ValueError:
            print("Ошибка! Введите целое число")

def main():
    """Основная функция: запрос числа и вывод его факториала."""
    input_num = get_valid_number()
    fact_result = math.factorial(input_num) #
    print(f"Факториал числа {input_num} равен {fact_result}")


if __name__ == "__main__":
    main()