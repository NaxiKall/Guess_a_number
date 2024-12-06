"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    max_rand = 101
    min_rand = 1
    cut = (max_rand - min_rand) // 2
    cut_count = 0
    wrong_nums_list = list()
    while True:
        while cut_count != 2:
            cut_count += 1
            if int(cut) < number:
                min_rand = round(cut)
                cut += 1/2 * min_rand
            if int(cut) > number:
                max_rand = round(cut)
                cut -= 1/2 * max_rand
                if max_rand > 100:
                    max_rand = 100
            
        predict_number = np.random.random_integers(min_rand,max_rand)
        while predict_number in wrong_nums_list:
            predict_number = np.random.random_integers(min_rand,max_rand)
        count += 1
        if number == predict_number:
            break  # выход из цикла если угадали
        wrong_nums_list.append(predict_number)
    return count

#если больше, то от среза до максимума, если меньше, то от минимума к срезу
def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

# if __name__ == "__main__":
#     random_predict()
