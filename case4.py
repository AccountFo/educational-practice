import random

def get_guess(try_num):
    """Получаем число от игрока с проверкой диапазона"""
    while True:
        try:
            num = int(input(f"Попытка {try_num + 1}: Введите число от 1 до 100: "))
            if num < 1:
                print("Число должно быть не меньше 1!")
            elif num > 100:
                print("Число должно быть не больше 100!")
            else:
                return num
        except ValueError:
            print("Ошибка! Введите целое число")

def check_guess(num, target):
    """Проверяем догадку игрока"""
    if num < target:
        print("Загаданное число больше!")
        return False
    elif num > target:
        print("Загаданное число меньше!")
        return False
    return True

def show_result(won, target, tries):
    """Показываем результат игры"""
    if won:
        print(f"✅ Ура! Вы угадали число {target} за {tries} попыток!")
    else:
        print(f"❌ К сожалению, вы не угадали. Число было: {target}.")

def play_game():
    """Запускаем игру"""
    target_num = random.randint(1, 100)
    max_tries = 7
    
    print("Игра 'Угадай число от 1 до 100'")
    print(f"У вас есть {max_tries} попыток")

    for try_num in range(max_tries):
        guess = get_guess(try_num)
        
        if check_guess(guess, target_num):
            show_result(True, target_num, try_num + 1)
            return
    
    show_result(False, target_num, max_tries)

if __name__ == "__main__":
    play_game()